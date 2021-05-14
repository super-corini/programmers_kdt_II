from flask import request
from sqlalchemy import exc
from flask_restx import Namespace, Resource, fields
from models import db, Weapon

api = Namespace('weapon', description='Handle weapons')

weapon_model = api.model('Weapon', {
    'name': fields.String,
    'stock': fields.Integer
})
message_model = api.model('Message', {
    'message': fields.String
})


@api.route('')
class WeaponAPI(Resource):
    @api.expect(weapon_model)
    @api.marshal_with(weapon_model)
    @api.response(400, 'Weapon name exists in db', weapon_model)
    def post(self):
        """Create weapon"""
        request_weapon = request.get_json()
        request_name = request_weapon['name']
        new_weapon = Weapon(name=request_name,
                            stock=request_weapon['stock'])  
        try:
            db.session.add(new_weapon)
            db.session.commit()
            return new_weapon.serialize
        except exc.IntegrityError:
            db.session.rollback()
            curr_weapon = Weapon.query.filter_by(name=request_name).first()
            return curr_weapon, 400    
        

    @api.marshal_with(weapon_model, as_list=True)
    def get(self):
        """List all weapons"""
        return [w.serialize for w in Weapon.query.all()]


    @api.doc(params={'name': 'weapon name'})
    @api.expect(weapon_model)
    @api.marshal_with(weapon_model)
    @api.response(404, 'There is no data with name', message_model)
    def put(self):
        """Change weapon's name and stock given by name"""
        request_name = request.args.get('name', type=str)
        request_data = request.get_json()
        weapon = Weapon.query.filter_by(name=request_name).first_or_404(description=f'There is no data with {request_name}')
        for key, value in request_data.items():
            setattr(weapon, key, value)
            db.session.commit()
        return weapon.serialize

    @api.doc(params={'name': 'weapon name'})
    @api.marshal_with(weapon_model)
    @api.response(404, 'There is no data with name', message_model)
    def delete(self):
        """Delete a weapon given its name"""
        request_name = request.args.get('name', type=str)
        weapon = Weapon.query.filter_by(name=request_name).first_or_404(description=f'There is no data with {request_name}')
        db.session.delete(weapon)
        db.session.commit()
        return weapon.serialize


@api.route('/init')
class WeaponInit(Resource):
    @api.marshal_with(message_model)
    def delete(self):
        """Initialize weapon database"""
        deleted = Weapon.query.delete()
        db.session.commit()
        return {'message': f'deleted {deleted} recodes in db.'}