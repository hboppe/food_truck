from management.product_handler import get_product_by_id, get_products_by_type, add_product
from management.tab_handler import calculate_tab
from menu import products

if __name__ == "__main__":
    # Seus prints de teste aqui
    print(get_product_by_id(28))
    print(get_products_by_type('drink'))
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    print(add_product(products, **new_product))
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food",
    }
    # Observe que passamos uma lista vazia como menu
    print(add_product([], **new_product))
