from werkzeug.security import safe_str_cmp #importing string comparison library to cover older systems
from user import User

users = [
    User(1, 'bob', 'asdf')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    # if user and user.password == password: this works in new python but not older versions
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)




# We remap this into objects since we made user objects in user.py
# users = [
#     {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'
#     }
# ]

# username_mapping = {'bob': {
#     'id': 1,
#     'username': 'bob',
#     'password': 'asdf'
#     }   
# }

# userid_mapping = { 1: {
#     'id': 1,
#     'username': 'bob',
#     'password': 'asdf'
#     }
# } 