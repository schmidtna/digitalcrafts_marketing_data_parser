class User:
    def __init__(self, _id, username, password):
        self.id = _id # id is a py keyword so we use _id
        self.username = username
        self.password = password