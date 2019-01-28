from datetime import datetime



def look_for_device(device, products):
    """
    Look for products of a given device (str) in products (dict of dicts)
    """
    device_products ={}
    for prod_id, prod in products.items():
        if prod['product_type'].lower() == device.lower():
            device_products[prod_id] = prod
    return device_products


def look_for_brand(brand, products):
    """ 
    Look for products of the given brand (str) in products (dict of dicts).
    """
    brand_products = {}
    for prod_id, prod in products.items():
        if prod['brand'].lower() == brand.lower():
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


def remove_purchase_list(number, purchases):
        """
        Check if the given bill number is on PURCHASE. If it is, it delete the
        bill from PURCHASE. If not, it gives the entire PURCHASE.
        """
        if number in purchases.keys():
                purchases.pop(number)
        return purchases


def remove_product(number, prod_id, purchases):
        """
        Check in a given bill number the exactly prod_id which it has to be
        removed.
        """ 
        products = purchases[number]
        if prod_id in products:
                products.remove(prod_id)
        return purchases

