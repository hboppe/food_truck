from menu import products
from collections import Counter


def get_product_by_id(id: int):
    if not type(id) is int:
        raise TypeError('product id must be an int')

    found_item = [item for item in products if item['_id'] == id]

    return found_item[0] if found_item else {}


def get_products_by_type(type_name: str):
    if not type(type_name) is str:
        raise TypeError('product type must be a str')

    same_type_products = [item for item in products if item['type'] == type_name]

    return same_type_products


def add_product(menu: list, **product: dict):
    if menu:
        product_id = max(item['_id'] for item in menu) + 1
    else:
        product_id = 1

    product['_id'] = product_id
    menu.append(product)
    return product


def menu_report():
    product_count = len(products)
    total_price = sum([item['price'] for item in products])
    average_price = round(total_price / product_count, 2)
    types = [item['type'] for item in products]
    most_common = Counter(types).most_common(1)

    return f'Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common[0][0]}'


def add_product_extra(menu: list, *keys: tuple, **product: dict):
    product_keys = list(product.keys())
    product_keys_values = []
    for key in keys:
        if key in product_keys:
            product_keys_values.append((key, product[key]))
        else:
            raise KeyError(f'field {key} is required')
    if menu:
        product_id = max(item['_id'] for item in menu) + 1
    else:
        product_id = 1
    product = dict(product_keys_values)
    print(product)
    product['_id'] = product_id
    menu.append(product)
    return product

