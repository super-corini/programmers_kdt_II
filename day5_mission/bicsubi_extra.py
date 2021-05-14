import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask, request#, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Resource, Api, fields #reqparse

app = Flask(__name__) # Flask App 생성한다


## Swagger ######################
api = Api(app, version='1.0', title='API Title', description='API Description') # API 만든다
ns  = api.namespace('bicsubi', description='namespace Description') # /goods/ 네임스페이스를 만든다
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'  # None, list, full



# REST Api에 이용할 데이터 모델을 정의한다
# model_goods = api.model('bicsubi_model', {
#     'name': fields.String(readOnly=True, required=True, description='name', help='name of weapon'),
#     'stock': fields.Integer(required=True, description='stock', help='number of stocks')
# })
########
@ns.route('/whoami')
class GetName(Resource):
    def get(self):
        '''Who am I'''
        try:
            val1 = {"name": "marquis08"}
        except KeyError:
            return {'result': 'ERROR_PARAMETER'}, 500

        # result = {'result': 'ERROR_SUCCESS', 'value': int(val1) + int(val2)}
        return val1, 200

@ns.route('/echo/<string:text>')
class GetEcho(Resource):
    '''Echo'''
    def echo(self, text):
        return {'value': text}

# @app.route('/echo/<')
# def print_string():
# 	str_json = {
# 		"value" : request.args.get('string')
# 	}
# 	return jsonify(str_json)
# @ns.route('/echo?string="string"', methods=['GET'])
# class GetName(Resource):
#     def get(self):
#         '''get all string subdir'''
#         try:
#             val1 = {"value": "string"}
#         except KeyError:
#             return {'result': 'ERROR_PARAMETER'}, 500

#         # result = {'result': 'ERROR_SUCCESS', 'value': int(val1) + int(val2)}
#         return val1, 200

class WeaponsDAO(object):
    '''Weapons Data Access Object'''
    def __init__(self):
        self.counter = 0
        self.rows    = []

    def get(self, name):
        '''READ: Get by name'''
        for row in self.rows:
            if row['name'] == name:
                return row
        api.abort(404, "{} doesn't exist".format(name))

    def create(self, data):
        '''CREATE: add New weapon'''
        row = data
        # row['id'] = self.counter = self.counter + 1 # increase id
        # if row['stock'] != 0:
        #     row['stock'] = row['stock'] + 1
        # row['stock'] = self.counter = self.counter + 1 # increase stocks
        # row['name'] = data[]
        self.rows.append(row)
        return row

    def update(self, name, data):
        '''UPDATE: Modify name or stock'''
        row = self.get(name)
        row.update(data)
        return row

    def delete(self, name):
        '''DELETE: delete certain weapon by name'''
        row = self.get(name)
        self.rows.remove(row)

DAO = WeaponsDAO() # DAO 객체를 만든다
# DAO.create({'name': 'BTC','stock':1}) # 샘플 1 데이터 만든다
# DAO.create({'name': 'ETH','stock':1}) # 샘플 2 데이터 만든다


@ns.route('/weapons/') # 네임스페이스 x.x.x.x/goods 하위 / 라우팅
class GoodsListManager(Resource):
    @ns.marshal_list_with(model_goods)
    def get(self):
        '''GET: fetch all data in list'''
        return DAO.rows

    @ns.expect(model_goods)
    @ns.marshal_with(model_goods, code=201)
    def post(self):
        '''POST: add new name and stock'''
        # request.json[파라미터이름]으로 파라미터값 조회할 수 있다
        print('input name & stock: ', request.json['name'],request.json['stock'])
        return DAO.create(api.payload), 201


@ns.route('/weapons/<string:name>') 
@ns.response(404, 'Cannot find name.')
@ns.param('name', 'Please insert name.')
class GoodsRUDManager(Resource):
    @ns.marshal_with(model_goods)
    def get(self, name):
        '''READ: Fetch data by name'''
        return DAO.get(name)

    def delete(self, name):
        '''DELETE: by name'''
        DAO.delete(name)
        return '', 200

    @ns.expect(model_goods)
    @ns.marshal_with(model_goods)
    def put(self, name):
        '''UPDATE: by name'''
        return DAO.update(name, api.payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
