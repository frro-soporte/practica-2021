from werkzeug.security import check_password_hash

from models.user import user
       

def get_user(id):
    return user.query.get(id)
class Auth():

    def __init__(self,id, roleId, firstName, lastName, address, phone, docNumber, mail, userName, userPass):
        self.id = id
        self.roleId = roleId
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.phone = phone
        self.docNumber = docNumber
        self.mail = mail
        self.userName = userName
        self.userPass = userPass

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
    def is_active(self):
        return True
    
    def get_id(self):
        return self.id