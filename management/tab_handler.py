from menu import products


def calculate_tab(products_ordered: dict):
    total_amount = 0
    for item in products_ordered:
        for item_list in products:
            if item_list['_id'] == item['_id']:
                total_amount += (item_list['price'] * item['amount'])
    return {'subtotal': f'${round(total_amount, 2)}'}
