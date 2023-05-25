from menu import products


def get_product_by_id(id: int):
    found_item = [item for item in products if item['_id'] == id]

    return found_item[0] if found_item else {}


def get_products_by_type(type: str):
    same_type_products = [item for item in products if item['type'] == type]

    return same_type_products


def add_product(menu: list, **product: dict):
    id_default = 1
    if len(menu) > 0:
        for item in menu:
            if item['_id'] > id_default:
                id_default = item['_id'] + 1
    product['_id'] = id_default
    menu.append(product)
    return product
