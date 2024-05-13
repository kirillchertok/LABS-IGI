from ..models import Order, OrderInfo, Customer, Product, Discount
from datetime import datetime
from django.utils.timezone import make_aware
import math

class OrderRepository:
    @staticmethod
    def delete_products_from_order(order):
        for product in order.products.all():
            db_product = Product.objects.get(id=product.id)
            db_product.amount += 1
            db_product.buyed -= 1
            db_product.save()
        order.products.clear()

    @staticmethod
    def change_all_orders_status():
        orders = Order.objects.all()
        for order in orders:
            if order.orderinfo.status == False and order.orderinfo.delivery_date.date() == datetime.today().date():
                db_info = OrderInfo.objects.get(order=order)
                db_info.status = True
                db_info.save()

    @staticmethod
    def change_users_orders_status(user):
        orders = Order.objects.filter(customer=user)
        for order in orders:
            if order.orderinfo.status == False and order.orderinfo.delivery_date.date() <= datetime.today().date():
                db_info = OrderInfo.objects.get(order=order)
                db_info.status = True
                db_info.save()            

    @staticmethod
    def get_all():
        try:
            OrderRepository.change_all_orders_status()
            db_orders = Order.objects.all()
            orders = list()
            for order in db_orders:
                orders.append(
                    {
                        'orderId': order.id,
                        'allProducts': order.products.all(),
                        'customer': {
                            'name': order.customer.name,
                            'phone': order.customer.phone,
                            'email': order.customer.email
                        },
                        'orderInfo': {
                            'status': order.orderinfo.status,
                            'delivery_date': order.orderinfo.delivery_date.date().strftime('%d/%m/%Y'),
                            'delivery_adress': order.orderinfo.delivery_address,
                            'amount_of_money': order.orderinfo.amount_of_money,
                            'created': order.created_at.date(),
                            'delivery_date_test': order.orderinfo.delivery_date.date(),
                            'discount': order.orderinfo.discount
                        }
                    }
                )
            return orders    
        except:
            return None
        
    @staticmethod
    def get_users(user):
        try:
            OrderRepository.change_users_orders_status(user)
            db_orders = user.order_set.all()
            orders = list()
            for order in db_orders:
                orders.append(
                    {
                        'orderId': order.id,
                        'nextId': order.id + 1,
                        'allProducts': order.products.all(),
                        'orderInfo': {
                            'status': order.orderinfo.status,
                            'delivery_date': order.orderinfo.delivery_date.date().strftime('%d/%m/%Y'),
                            'delivery_adress': order.orderinfo.delivery_address,
                            'discount': order.orderinfo.discount,
                            'amount_of_money': order.orderinfo.amount_of_money,
                            'method': order.get_absolute_url
                        }
                    }
                )
            return orders    
        except:
            return None

    @staticmethod
    def get_one_by_id(id: int):
        try:
            order = Order.objects.filter(id=id).first()
            if order is None:
                return None
            return  {
                        'orderId': order.id,
                        'allProducts': order.products.all(),
                        'orderInfo': {
                            'status': order.orderinfo.status,
                            'delivery_date': order.orderinfo.delivery_date.date(),
                            'delivery_adress': order.orderinfo.delivery_address,
                            'amount_of_money': order.orderinfo.amount_of_money,
                            'created': order.created_at.date(),
                            'discount': order.orderinfo.discount,
                            'method': order.get_absolute_url
                        }
                    }   
        except:
            return None

    @staticmethod
    def create(email: str, products: list[str], date: datetime, adress: str, discount_code: str):
        try:
            if discount_code != '':
                discount = Discount.objects.filter(code=discount_code).first()
                discount_amount = discount.amount
            user = Customer.objects.filter(email=email).first()
            if user is None:
                return None
            order = Order.objects.create(customer=user)
            order_amount_of_money = 0
            for prd in products:
                product = Product.objects.filter(id=int(prd)).first()
                if product is not None and product.amount != 0:
                    order_amount_of_money += product.price
                    order.products.add(product)
                    product.amount -= 1
                    product.buyed += 1
                    product.save()
            order.save()
            order_amount_of_money_with_discount = order_amount_of_money*(1 - (discount_amount/100)) if discount_code != '' else order_amount_of_money
            orderInfo = OrderInfo.objects.create(order=order, delivery_date=(date), delivery_address=adress, amount_of_money=order_amount_of_money_with_discount, discount=Discount.objects.filter(code='0000').first() if discount_code == '' else discount)
            orderInfo.save()
            return order
        except:
            return None

    @staticmethod
    def update(id: int, products: list[str], date: datetime, adress: str, discount_code=""):
        try:
            discount = Discount.objects.filter(code=discount_code).first().amount
            order = Order.objects.get(id=id)
            if order is None:
                return None
            OrderRepository.delete_products_from_order(order)
            order_info = OrderInfo.objects.get(order=order)
            order_amount_of_money = 0
            for prd in products:
                product = Product.objects.get(order=order)
                if product is not None and product.amount != 0:
                    order_amount_of_money += product.price
                    order.products.add(product)
                    product.amount -= 1
                    product.save()
            order.save()
            order_info.order = order
            order_info.delivery_date = date
            order_info.delivery_address = adress
            order_info.amount_of_money = order_amount_of_money*(1-discount)
            order_info.discount = discount*100
            order_info.save()
            return order
        except:
            return None
        
    @staticmethod
    def delete(id: int):
        try:
            order = Order.objects.filter(id=id).first()
            order_info = OrderInfo.objects.get(order=order.id)
            if order is None:
                return None
            if order_info is None:
                return None
            OrderRepository.delete_products_from_order(order)
            order_info.delete()
            order.delete()
            return order
        except:
            return None  