from models.db_models import UserDetails
from flask import jsonify
from common import db,app

class PostgreConnector:

    def register_newuser(self,name,email,phone_number,location,password):

        try:
            with app.app_context():
              
                success = True
                useremail = UserDetails.query.filter(UserDetails.email==email).all()
                if useremail:
                    print("User email exists")
                    success = False
                    return jsonify({"message":"The email already exists"}),success
                User = UserDetails(username=name,email=email,phone=phone_number,place=location,user_password=password)
                db.session.add(User)
                db.session.commit()
                return User.to_dict(), success
        except Exception as e:
            raise
