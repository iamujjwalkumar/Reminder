from Dataaccesslayer.postgreutilties import PostgreConnector

sql_connector = PostgreConnector()

def register_user(data):
    try:
        name = data.get('name')
        email = data.get("email")
        phone_number = data.get("phone_number")
        location = data.get("location")
        password = data.get("password")
        result, success = sql_connector.register_newuser(name,email,phone_number,location,password)
        return result, success
    except Exception as e:
        raise


