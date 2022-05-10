class EmailAlreadyExists(Exception):

    msg = "Email already exists !"

    def __init__(self):
        super().__init__(self.msg)
