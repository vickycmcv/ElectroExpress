from datetime import datetime



def look_for_device(device, products):
    """
    Look for products of a given device (str) in products (dict of dicts)
    """
    device_products ={}
    for prod_id, prod in products.items():
        if prod['product_type'].lower() == device:
            device_products[prod_id] = prod
    return device_products


def look_for_brand(brand, products):
    """ 
    Look for products of the given brand (str) in products (dict of dicts).
    """
    brand_products = {}
    for prod_id, prod in products.items():
        if prod['brand'].lower() == brand:
            brand_products[prod_id] = prod
    return brand_products


def look_for_price_lowereq(price, products):
    """ 
    Look for products of the with a price lower than the given price (number)
    in products (dict of dicts).
    """
    price_lowereq_products = {}
    for prod_id, prod in products.items():
        if prod['price'] <= price:
            price_lowereq_products[prod_id] = prod
    return price_lowereq_products


def generate_bill(bill_number, prod_ids, products):
        """
        Check if the prod_ids (list) are in the stock (dic). If they are, it 
        generate a bill (dic of lists). If not, it gives a empty bill
        """
        bill = {}
        prod_id_list = []
        for individual_id in prod_ids:
                if int(individual_id) in products.keys():
                        prod_id_list.append(individual_id)
                        bill = {bill_number: prod_id_list}
                else:
                        bill = {}
        return bill

