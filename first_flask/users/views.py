from flask import Blueprint, jsonify,request

mod=Blueprint('users',__name__,url_prefix='/santosh')

import json
with open ('first_flask\\data.json','r') as data:
    print(data)


@mod.route('/',methods=['GET'])
def fetchall():
    return 'List of users.'

@mod.route('/user_id',methods=['GET'])
def show(user_id):
    # print(user_id)
    # response={
    #     "user_id":user_id
    # }
    response={x for x in data if x['id']==int(user_id)}
    return jsonify((response))

@mod.route('/fetch_user/',methods=['GET'])
def frtch_user():
    user_id=request.args.get('user_id')
    user_detail=[x for x in data if x['id']==int(user_id)]
    user_detail=user_detail[0] if user_detail else {}
    return jsonify(user_detail)


@mod.route('/creat_user', methods=['POST'])
def create_user1():
    user_data=request.get_json()
    name=user_data['name']
    password = user_data['password']

    new_user_id=data[-1]['id']+1
    response=user_data
    response['id']=new_user_id
    response['name']=name
    response['password']=password


    data.append(response)
    json.dump(data,open('first_flask\\data.json','w'))
    return 'data saved successfully'

@mod.route('/create_user_form',methods=['POST'])
def create_user2():
    name=request.form.get('name')
    password=request.form.get('password')
    new_user_id=data[-1]['id'] + 1
    response={

        'id':new_user_id,
        'name':name,
        'password':password
    }
    data.append(response)
    json.dump(data, open('first_flask\\data.json', 'w'))
    return 'data saved successfully from Form'

#
# @mod.route('/update_user/<user_id>/',method=['PUT'])
# def update_user(user_id):
#     user_data=request.get_json()
#     for d in data:
#         if d['id'] = int('user_id'):
#             if 'name' in user_data:
#                 d['name']=user_data['name']
#             if 'password' in user_data:
#                 d['password']=user_data['password']
#     json.dump(data,open('first_flask\\data.json', 'w'))
#
#
#
# @mod.route('/delete/<user_id>/',method=['DELETE'])
# def delete_user(user_id):
#     user_data=request.get_json()
#     for d in data:
#         if d['id'] = int('user_id'):
#             if 'name' in user_data:
#                 d['name']=user_data['name']
#             if 'password' in user_data:
#                 d['password']=user_data['password']
#     json.dump(data,open('first_flask\\data.json', 'w'))
