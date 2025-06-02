from common import db

class UserDetails(db.Model):
    __tablename__ = 'user_details'
    __table_args__ = {'schema':'users'}

    username = db.Column(db.String)
    email = db.Column(db.String,primary_key=True)
    phone = db.Column(db.String)
    place = db.Column(db.String)
    user_password = db.Column(db.String)


    def to_dict(self):
        return {
            "name":self.username,
            "email":self.email,
            "phone_number":self.phone,
            "location":self.place,
            "password":self.user_password
        }