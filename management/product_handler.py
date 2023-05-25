from menu import products


def get_product_by_id(id: int):
    for item in products:
        if item['_id'] == id:
            return item
    return {}


def get_products_by_type(type: str):
    same_type_products = []
    for item in products:
        if item['type'] == type:
            same_type_products.append(item)
    return same_type_products
