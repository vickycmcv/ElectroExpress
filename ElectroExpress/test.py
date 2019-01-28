from utils import (remove_product, generate_bill, remove_purchase_list,
                   look_for_device)

def test_buy_one_product():
    bill_number = '123456'
    prod_ids = '1'
    products = {1: {'device': 'mobile'}}

    buy_real = generate_bill(bill_number, prod_ids, products)
    buy_expected = {'123456': ['1']}

    assert buy_real == buy_expected


def test_buy_two_products():
    bill_number = '234567'
    prod_ids = ['1', '2']
    products = {1: {'device': 'mobile'}, 2: {'device': 'mobile'}}


    buy_real = generate_bill(bill_number, prod_ids, products)
    buy_expected = {'234567': ['1', '2']}

    assert buy_real == buy_expected


def test_buy_product_not_in_stock():
    bill_number = '345678'
    prod_ids = ['1', '3']
    products = {1: {'device': 'mobile'}, 2: {'device': 'mobile'}}


    buy_real = generate_bill(bill_number, prod_ids, products)
    buy_expected = {}

    assert buy_real == buy_expected


def test_remove_purchase():
    purchases = {'123456': ['1', '2', '3']}
    number = '123456'
    
    purchases_real = remove_purchase_list(number, purchases) 
    purchases_expected = {}
    
    assert purchases_real == purchases_expected


def test_remove_purchase_does_not_exit():
    purchases = {'123456': ['1', '2', '3']}
    number = '1234567'
    
    purchases_real = remove_purchase_list(number, purchases) 
    purchases_expected = {'123456': ['1', '2', '3']}
    
    assert purchases_real == purchases_expected


def test_remove_one_product():
    purchases = {'123456': ['1', '2', '3']}
    prod_id = '2'
    number = '123456'
    
    purchases_real = remove_product(number, prod_id, purchases) 
    purchases_expected = {'123456': ['1', '3']}
    
    assert purchases_real['123456'] == purchases_expected['123456']


def test_remove_one_product_does_not_remove_other_bill():
    purchases = {'123456': ['1', '2', '3'], '234567': ['4','2']}
    prod_id = '2'
    number = '123456'
    
    purchases_real = remove_product(number, prod_id, purchases) 
    purchases_expected = {'123456': ['1', '3'], '234567': ['4','2']}
    
    assert '234567' in purchases_real
    assert purchases_real['234567'] == purchases_expected['234567']


def test_filter_by_device():
    device = 'mobile'
    products = {1: {'product_type': 'mobile'}, 2: {'product_type': 'tablet'}}

    filtered_product_real = look_for_device(device, products)
    filtered_product_expected = {1: {'product_type': 'mobile'}}

    assert filtered_product_real == filtered_product_expected
