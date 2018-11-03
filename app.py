from flask import Flask, flash, render_template, request, redirect, url_for, session, abort
import stripe
import os
import numpy as np
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *


app = Flask(__name__)

pub_key = 'pk_test_SF586n7bKRisyBDkWxVyTrbL'
stripe.api_key = 'sk_test_TMqJO4DLuAnqqSHRJsVwePH9'

@app.route('/')
def index():
    # Define home page (hot drinks page)
    barista_flag = np.load('barista_flag.npy')[0]

    if barista_flag == 1:
        # Open JSON menu
        with open('menu/hot_drinks.json') as f:
            hot_drinks = json.load(f)
        order = ["Hot Coffees","Hot Teas","Other"]
        return render_template('index.html', pub_key=pub_key, food_items=hot_drinks, order=order)

    else:
        return redirect(url_for('closed'))

@app.route('/cold')
def cold():
    # Define cold drinks page
    barista_flag = np.load('barista_flag.npy')[0]

    if barista_flag ==1:
        # Open JSON menu
        with open('menu/cold_drinks.json') as f:
            cold_drinks = json.load(f)
        order = ["Iced Coffees","Iced Teas","Lemonades"]
        return render_template('index.html',pub_key=pub_key,food_items=cold_drinks,order=order)

    else:
        return redirect(url_for('closed'))

@app.route('/food')
def food():
    # Define food page
    barista_flag = np.load('barista_flag.npy')[0]

    if barista_flag == 1:
        # Open JSON menu
        with open('menu/food.json') as f:
            food = json.load(f)
        order = ["Savory","Sweet"]
        return render_template('index.html',pub_key=pub_key,food_items=food,order=order)

    else:
        return redirect(url_for('closed'))

@app.route('/closed')
def closed():
    # Define "we're closed" page
    # To be redirected to when no barista is logged in
    return render_template('closed.html')

@app.route('/barista')
def login():
    # Define barista dashboard / login route
    # Send to login page if not logged in else to dashboard
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # Create barista login flag
        np.save("barista_flag",np.array([1]))

        # Get orders from database
        engine = create_engine('sqlite:///drinks.db', echo=True)
        DBSession = sessionmaker(bind=engine)
        dbsession = DBSession()

        data = dbsession.query(User).all()
        drinks = []
        for row in data:
            drinks.append([row.id,row.name])

        return render_template('dashboard.html', drinks=drinks) # Barista dash

@app.route('/login', methods=['POST'])
def do_admin_login():
    # Check credentials
    if request.form['password'] == '1000calories' and request.form['username'] == 'thinmint':
        session['logged_in'] = True
        return redirect(url_for('login'))

    else:
        return render_template('login.html')

@app.route("/logout")
def logout():
    # Log barista out
    session['logged_in'] = False

    # Clear barista flag
    np.save("barista_flag",np.array([0]))

    return redirect(url_for('login'))

@app.route("/refresh", methods=['POST'])
def update():
    # Remove finished drink from database of orders
    # To be called when barista presses 'done' on an order
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

    return redirect(url_for('login')) # Barista dash

@app.route('/thanks')
def thanks():
    # Define thanks page
    return render_template('thanks.html')

@app.route('/pay/<string:order_name>/<string:order_amount>', methods=['POST'])
def pay(order_name,order_amount):
    # Create payment
    # Stripe payment button calls this

    # Create stripe charge
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=int(order_amount),
        currency='usd',
        description=order_name
    )
    print("\n pay " + order_amount + " for " + order_name + " \n")

    # Add order to database
    engine = create_engine('sqlite:///drinks.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    user = User(order_name)
    session.add(user)
    session.commit()

    # Push to thanks page
    return redirect(url_for('thanks'))

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
