


from flask import Flask, request, jsonify, render_template, flash
from BusinessLayer.businesslayer import register_user
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from common import db, app, api






@app.route('/app/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        
        data = {
            'name': request.form.get('username'),
            'email': request.form['email'],
            'phone_number': request.form['phone'],
            'location': request.form['location'],
            'password': request.form['password']
        }
        result, success = register_user(data)
        if success == False:
            return({"message":"User already exists"})
        else:
            return({"message":"User registered successfully"})
    return render_template('register_user.html')

@app.route('/test')
def test():
    return render_template('register_user.html')

if __name__== "__main__":
    app.run(debug=True)