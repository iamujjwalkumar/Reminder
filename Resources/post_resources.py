from flask import request, jsonify, render_template, flash
from flask_restful import Resource
from BusinessLayer.businesslayer import register_user



class Register(Resource):
    def post(self):
        """Resource class to register a user"""
        if request.method == 'POST':
            data = {
                'name' : request.form.get('username'),
                'email' : request.form['email'],
                'phone_number':request.form['phone'],
                'location':request.form['location'],
                'password':request.form['password']   
            }
            result,success = register_user(data)
            flash(result["message"], 'success' if success else 'failed')

        return render_template('register.html')