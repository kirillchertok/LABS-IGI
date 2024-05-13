from .modelsServices.productService import ProductService
from .modelsServices.orderService import OrderService
from ..infrastracture.graphic_functions import GraphicFunction
from datetime import datetime
from collections import Counter

class AdminService:
    orders = None
    products = None
    sales = list()

    @staticmethod
    def get_popular_products():
        return ProductService.get_all_py_param('buyed')
    
    @staticmethod
    def get_year_income():
        return float(sum([order['orderInfo']['amount_of_money'] for order in AdminService.orders if order['orderInfo']['created'].year == datetime.now().year]))

    @staticmethod
    def get_price_list():
        prices = ProductService.get_all_py_param('price')
        AdminService.products = prices
        return AdminService.products
    
    @staticmethod
    def get_orders_counter(condion=None):
        orders = AdminService.orders if condion is None else [order for order in AdminService.orders if condion(order)]
        if condion is not None and len(orders) == 0:
            return orders
        products = list()
        for order in orders:
            products.extend(order['allProducts'])
        counter = Counter(products)
        for product in AdminService.products:
            if product not in counter.keys() and product.amount > 0:
                counter[product] = 0
        return counter.most_common()

    @staticmethod
    def get_order_for_stat():
        AdminService.orders = OrderService.get_all_orders()
        customers = dict()
        for order in AdminService.orders:
            city = order['orderInfo']['delivery_adress'].split(',')[0]
            customer = order['customer']
            if city not in customers.keys():
                customers[city] = [customer]
            else:
                customers[city].append(customer)
        GraphicFunction.draw_orders_cities(customers)
        return customers
    
    @staticmethod
    def get_month_volume():
        counters = dict()
        months = list()
        sales = list()
        incomes = list()
        for i in range(1, datetime.now().month + 1):
            month_name = datetime(1, i, 1).strftime('%B')
            counters[month_name] = AdminService.get_orders_counter(lambda o: o['orderInfo']['delivery_date_test'].month == i)
            months.append(month_name[:3] if len(month_name) > 4 else month_name)
            month_sale = 0
            month_incomes = 0
            for book, sale in counters[month_name]:
                month_sale += sale
                month_incomes += float(sale * book.price)
            sales.append(month_sale)
            incomes.append(month_incomes)
        GraphicFunction.draw_incomes_stats(months, sales, incomes)
        AdminService.sales = sales
        return counters
    
    
