from menu import products


def get_product_by_id(id: int):
    found_item = [item for item in products if item['_id'] == id]

    return found_item[0] if found_item else {}


def get_products_by_type(type: str):
    same_type_products = [item for item in products if item['type'] == type]

    return same_type_products


def add_product(menu: list, **product: dict):
    if menu:
        product_id = max(item['_id'] for item in menu) + 1
    else:
        product_id = 1

    product['_id'] = product_id
    menu.append(product)
    return product
