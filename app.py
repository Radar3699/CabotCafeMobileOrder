from flask import Flask, flash, render_template, request, redirect, url_for, session, abort
import stripe
import os
import numpy as np

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
import json


app = Flask(__name__)

pub_key = 'pk_test_SF586n7bKRisyBDkWxVyTrbL'
stripe.api_key = 'sk_test_TMqJO4DLuAnqqSHRJsVwePH9'

@app.route('/')
def index():
    # Open JSON menu
    with open('menu/hot_drinks.json') as f:
        hot_drinks = json.load(f)
    order = ["Hot Coffees","Hot Teas","Other"]

    return render_template('index.html', pub_key=pub_key, food_items=hot_drinks, order=order)

@app.route('/barista')
def login():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        engine = create_engine('sqlite:///drinks.db', echo=True)
        DBSession = sessionmaker(bind=engine)
        dbsession = DBSession()

        data = dbsession.query(User).all()
        drinks = []
        for row in data:
            # print("ID", row.id)
            # print("name",row.name)
            drinks.append([row.id,row.name])

        # print("TEST",drink)
        return render_template('dashboard.html', drinks=drinks) # Barista dash

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == '1000calories' and request.form['username'] == 'thinmint':
        session['logged_in'] = True

        # Get database data
        engine = create_engine('sqlite:///drinks.db', echo=True)
        DBSession = sessionmaker(bind=engine)
        dbsession = DBSession()
        data = dbsession.query(User).all()
        drinks = []
        for row in data:
            # print("ID", row.id)
            # print("name",row.name)
            drinks.append([row.id,row.name])

        # return render_template('dashboard.html',drinks=drinks) # Barista dash
        return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

@app.route("/refresh", methods=['POST'])
def update():
    print(" \n Removing \n ", request.form['id'])
    id_to_remove = int(request.form['id'])

    # Remove from database
    engine = create_engine('sqlite:///drinks.db', echo=True)
    DBSession = sessionmaker(bind=engine)
    dbsession = DBSession()

    drink = dbsession.query(User).get(id_to_remove)
    print(" Removing drink: ", drink)
    dbsession.delete(drink)
    dbsession.commit()

    # Get database data
    data = dbsession.query(User).all()
    drinks = []
    for row in data:
        drinks.append([row.id,row.name])

    dbsession.close()

    # return render_template('dashboard.html',drinks=drinks) # Barista dash
    return redirect(url_for('login'))


@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/cold')
def cold():
    with open('menu/cold_drinks.json') as f:
        cold_drinks = json.load(f)
    order = ["Iced Coffees","Iced Teas","Lemonades"]
    return render_template('index.html',pub_key=pub_key,food_items=cold_drinks,order=order)

@app.route('/food')
def food():
    with open('menu/food.json') as f:
        food = json.load(f)
    order = ["Savory","Sweet"]
    return render_template('index.html',pub_key=pub_key,food_items=food,order=order)

@app.route('/pay', methods=['POST'])
def pay():

    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=19900,
        currency='usd',
        description='The Product'
    )

    return redirect(url_for('thanks'))

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
