from app import app, db
from flask import Flask
from .models import TransactionEntry
import random

@app.route('/')
def hello():

	transaction_id = None

	product_id = 45
	price = "%.2f" % random.uniform(0.01, 100.00)
	quantity = 5

	#creates an entry in the Transaction Entry table
	transaction_entry = TransactionEntry(transaction_id = transaction_id, product_id = product_id, price = price, quantity = quantity)

	db.session.add(transaction_entry)

	db.session.commit()

<<<<<<< HEAD
	return "Entry added to db successfully."
=======
	a = Employee.query.filter_by(first_name = "harsha").all()

	return str(len(a))

@app.route('/lookup', method=['GET'])
def lookup(lookup_code):
	 product = db.session.query(Product).filter_by(ItemLookupCode = lookup_code).first()
	 

>>>>>>> a51ac2ef38a15a7ca3184155dbc89b36441c6cb1
