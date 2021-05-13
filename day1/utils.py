# find index by id
# 해당 id 가 반드시 존재한다고 가정
def find_index_by_id(lst, id):
    for i, dic in enumerate(lst):
        if dic['id'] == int(id):
            return i