import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pawtyplanner.settings')
import django
django.setup()
from pawtyplannerbackend.models import Product, Design, Order, ProductOrder


def populate():
    products = [
        {'name': 'Pawty Cone Hat', 'price': 9.99},
        {'name': 'Pawty Crown', 'price': 9.99},
        {'name': 'Peamutt Butter Popcorn', 'price': 9.99}
    ]

    designs = [
        {'name': 'Polka Dot'},
        {'name': 'Rainbow'},
        {'name': 'Sparkly'},
        {'name': 'Peanut Butter'}
    ]

    orders = [
        {'order_number': 1},
        {'order_number': 2},
        {'order_number': 3}
    ]

    product_orders = [
        {'product_name': 'Pawty Cone Hat', 'design_name': 'Rainbow', 'quantity': 2, 'order_number': 1},
        {'product_name': 'Pawty Crown', 'design_name': 'Sparkly', 'quantity': 1, 'order_number': 1},
        {'product_name': 'Pawty Cone Hat', 'design_name': 'Polka Dot', 'quantity': 1, 'order_number': 2},
        {'product_name': 'Peamutt Butter Popcorn', 'design_name': 'Peanut Butter', 'quantity': 4, 'order_number': 2},
        {'product_name': 'Pawty Crown', 'design_name': 'Rainbow', 'quantity': 4, 'order_number': 3},
        {'product_name': 'Peamutt Butter Popcorn', 'design_name': 'Peanut Butter', 'quantity': 1, 'order_number': 3},
    ]

    print('Adding products')
    for product in products:
        add_product(product['name'], product['price'])

    print('Adding designs')
    for design in designs:
        add_design(design['name'])

    print('Adding orders')
    for order in orders:
        add_order(order['order_number'])

    print('Adding product orders')
    for product_order in product_orders:
        add_product_order(product_order['product_name'], product_order['design_name'],
                          product_order['quantity'], product_order['order_number'])


def add_product(name, price):
    product = Product.objects.get_or_create(name=name, price=price)
    return product


def add_design(name):
    design = Design.objects.get_or_create(name=name)
    return design


def add_order(order_number):
    order = Order.objects.get_or_create(order_number=order_number, price=0)
    return order


def add_product_order(product_name, design_name, quantity, order_number):
    product = Product.objects.get(name=product_name)
    design = Design.objects.get(name=design_name)
    order = Order.objects.get(order_number=order_number)
    Order.objects.filter(pk=order.pk).update(price=order.price+product.price*quantity)
    product_order = ProductOrder.objects.get_or_create(product=product, design=design,
                                                       quantity=quantity, order=order)
    return product_order


if __name__ == '__main__':
    print('Starting The Pawty Planner population script...')
    populate()
    print('The Pawty Planner has been populated!')
