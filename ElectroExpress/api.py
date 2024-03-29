import flask
from flask import request, jsonify

from utils import (look_for_brand, look_for_price_lowereq, look_for_device, 
                   generate_bill, remove_purchase_list, remove_product)

from datetime import datetime



app = flask.Flask(__name__)
app.config["DEBUG"] = True


PRODUCTS = {
    0:{'product_type': 'tablet',
       'brand': 'Samsung',
       'model': 'Galaxy_Phone',
       'price': 180.00},

    1:{'product_type': 'tablet',
       'brand': 'Xiaomi',
       'model': 'mipad',
       'price': 165.00},

    2:{'product_type': 'tablet',
       'brand': 'Apple',
       'model': 'ipad',
       'price': 210.00},

    3:{'product_type': 'mobile',
       'brand': 'Samsung',
       'model': 'Galaxy_phone',
       'price': 580.00},

    4:{'product_type': 'mobile',
       'brand': 'Xiaomi',
       'model': 'mimobile',
       'price': 250.00},

    5:{'product_type': 'mobile',
       'brand': 'Apple',
       'model': 'iphone',
       'price': 890.00},
}

PURCHASES = {}


################################## API ####################################### 
@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to ElectoExpress</h1>"


@app.route('/stock', methods=['GET'])
def stock():
    """
    Query stock. Parameters:
    - brand
    - price_lowereq
    ...
    """
    products = PRODUCTS
    if 'device' in request.args:
        product_type = request.args['device']
        products = look_for_device(product_type, products)
    if 'brand' in request.args:
        brand = request.args['brand']
        products = look_for_brand(brand, products)
    if 'price_lowereq' in request.args:
        price = float(request.args['price_lowereq'])
        products = look_for_price_lowereq(price, products)
    
    return jsonify(products)


@app.route('/buy', methods=['GET'])
def buy():
   """
   Select id product/s for buying it/them and generate a bill. 
   Introduce the bills on the purchases dict.
   """
   if 'id' in request.args: 
      prod_ids = request.args['id'].split(":")
      bill_number = str(f'{datetime.now():%Y%m%d%H%M%S}')
      bill = generate_bill(bill_number, prod_ids, PRODUCTS)
   if len(bill) > 0:
      PURCHASES.update(bill)

   return jsonify(bill)


@app.route('/purchases', methods=['GET'])
def purchases_list():
   """ 
   Shows the updated purchases dict.
   """
   return jsonify(PURCHASES)


@app.route('/remove', methods=['GET'])
def remove():
   """
   Remove purchases with a given bill number
   """
   if 'bill_number' in request.args:
      number = request.args['bill_number']
      
      if 'id' in request.args:
         prod_id = request.args['id']
         remove_bill = remove_product(number, prod_id, PURCHASES)
      else:
         remove_bill = remove_purchase_list(number, PURCHASES)

   return jsonify(remove_bill)
   
app.run()
