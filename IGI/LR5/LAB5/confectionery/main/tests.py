from django.test import TestCase
from .forms import *
from .models import *
from .services.authService import *
from .services.modelsServices.customerService import *
from .services.modelsServices.employeeService import *
from .services.modelsServices.orderService import *
from .services.modelsServices.productService import *

class SignUpFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.form_data = {
            'name': 'Test User',
            'phone': '+375291234567',
            'email': 'test@test.com',
            'password': 'test123Test',
            'confirm': True
        }

    def test_form_valid(self):
        form = SignUpForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        self.form_data['confirm'] = False
        form = SignUpForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_phone_invalid(self):
        self.form_data['phone'] = '1234567890'
        form = SignUpForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_clean(self):
        form = SignUpForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data)

class SignInFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.form_data = {
            'email': 'test@test.com',
            'password': 'test123Test'
        }

    def test_form_valid(self):
        form = SignInForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        self.form_data['password'] = ''
        form = SignInForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_clean(self):
        form = SignInForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data)

class NewProductFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.form_data = {
            'name': 'testproduct',
            'price': 12,
            'smallDescription': 'asdadasdadsad',
            'mainDescription': 'qewqeqeweqeweqewqeqeqreqweqeqtertqteywqerqwqreqwe',
            'amount': 100,
            'type': 'Торт'
        }

    def test_form_valid(self):
        form = NewProductForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        self.form_data['name'] = ''
        form = NewProductForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_phone_invalid(self):
        self.form_data['price'] = -10
        form = NewProductForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_clean(self):
        form = NewProductForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data)

class AddDiscountFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.form_data = {
            'code': '0000',
            'amount': 22
        }

    def test_form_valid(self):
        form = AddDiscountForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        self.form_data['code'] = ''
        form = AddDiscountForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_clean(self):
        form = AddDiscountForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data)

class UpdateInfFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.form_data = {
            'name': 'Test User',
            'phone': '+375291234567',
            'email': 'test@test.com',
            'password': 'test123Test'
        }

    def test_form_valid(self):
        form = UpdateInfForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        self.form_data['name'] = ''
        form = UpdateInfForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_phone_invalid(self):
        self.form_data['phone'] = '1234567890'
        form = UpdateInfForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_clean(self):
        form = UpdateInfForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data)

class OrderFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        type = ProductType.objects.create(type='TestType')
        product = Product.objects.create(name='testproduct', price=12, description='qweqsdadqdqweqdsq', amount=3, type=type, buyed=0)
        cls.form_data = {
            'products': [str(product.id)],
            'date': datetime.now().date() + timedelta(days=1),
            'address': 'Minsk, Ylica 29',
            'sale_code': ''
        }

    def test_form_valid(self):
        form = OrderForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        self.form_data['address'] = ''
        form = OrderForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_date(self):
        self.form_data['date'] = datetime.now().date()
        form = OrderForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_books(self):
        self.form_data['products'] = list()
        form = OrderForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_sale_code(self):
        self.form_data['sale_code'] = 'qewqew'
        form = OrderForm(data=self.form_data)
        self.assertFalse(form.is_valid())

class ProductTypeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ProductType.objects.create(type='TestType')

    def test_type_label(self):
        type = ProductType.objects.get(id=1)
        field_label = type._meta.get_field('type').verbose_name
        self.assertEqual(field_label, 'type')

    def test_object_name_product_type(self):
        type = ProductType.objects.get(id=1)
        expected_object_name = f'{type.id} {type.type} {type.created_at} {type.updated_at}'
        self.assertEqual(expected_object_name, str(type))

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        type = ProductType.objects.create(type='TestType')
        Product.objects.create(name='testproduct', price=12, description='qweqsdadqdqweqdsq', amount=3, type=type, buyed=0)
    
    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_description_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_amount_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('amount').verbose_name
        self.assertEqual(field_label, 'amount')

    def test_type_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('type').verbose_name
        self.assertEqual(field_label, 'type')

    def test_buyed_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('buyed').verbose_name
        self.assertEqual(field_label, 'buyed')

    def test_absolute_url(self):
        product = Product.objects.get(id=1)
        abs_url = product.get_absolute_url()
        self.assertEqual(abs_url, '/products/1')

    def test_object_name_product(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.id} {product.name} {product.price} {product.description} {product.amount} {product.buyed} {product.type} {product.created_at} {product.updated_at}'
        self.assertEqual(expected_object_name, str(product))

class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Customer.objects.create(name='TestCustomer', phone='+375291234567', email='test@test.com', password='password1')

    def test_name_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_label_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_phone_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'phone')

    def test_phone_label_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('phone').max_length
        self.assertEqual(max_length, 13)

    def test_email_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_password_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('password').verbose_name
        self.assertEqual(field_label, 'password')

    def test_password_label_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('password').max_length
        self.assertEqual(max_length, 300)

    def test_object_name_customer(self):
        customer = Customer.objects.get(id=1)
        expected_object_name = f'{customer.id} {customer.name} {customer.phone} {customer.email} {customer.password} {customer.created_at} {customer.updated_at}'
        self.assertEqual(expected_object_name, str(customer))

class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Employee.objects.create(name='TestCustomer', phone='+375291234567', email='test@test.com', password='password1', is_admin=False)

    def test_name_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_label_length(self):
        employee = Employee.objects.get(id=1)
        max_length = employee._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_phone_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'phone')

    def test_phone_label_length(self):
        employee = Employee.objects.get(id=1)
        max_length = employee._meta.get_field('phone').max_length
        self.assertEqual(max_length, 13)

    def test_email_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_password_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('password').verbose_name
        self.assertEqual(field_label, 'password')

    def test_password_label_length(self):
        employee = Employee.objects.get(id=1)
        max_length = employee._meta.get_field('password').max_length
        self.assertEqual(max_length, 300)

    def test_is_admin_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('is_admin').verbose_name
        self.assertEqual(field_label, 'is admin')

    def test_object_name_employee(self):
        employee = Employee.objects.get(id=1)
        expected_object_name = f'{employee.id} {employee.name} {employee.phone} {employee.email} {employee.password} {employee.is_admin} {employee.created_at} {employee.updated_at}'
        self.assertEqual(expected_object_name, str(employee))

class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        customer = Customer.objects.create(name='TestCustomer', phone='+375291234567', email='test@test.com', password='password1')
        type = ProductType.objects.create(type='TestType')
        product = Product.objects.create(name='testproduct', price=12, description='qweqsdadqdqweqdsq', amount=3, type=type, buyed=0)
        order = Order.objects.create(customer=customer)
        order.products.add(product)

    def test_customer_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('customer').verbose_name
        self.assertEqual(field_label, 'customer')

    def test_products_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('products').verbose_name
        self.assertEqual(field_label, 'products')

    def test_object_name_order(self):
        order = Order.objects.get(id=1)
        expected_object_name = f'{order.id} {order.customer} {order.created_at} {order.updated_at}'
        self.assertEqual(expected_object_name, str(order))    

class OrderInfModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        customer = Customer.objects.create(name='TestCustomer', phone='+375291234567', email='test@test.com', password='password1')
        type = ProductType.objects.create(type='TestType')
        product = Product.objects.create(name='testproduct', price=12, description='qweqsdadqdqweqdsq', amount=3, type=type, buyed=0)
        order = Order.objects.create(customer=customer)
        order.products.add(product)
        discount = Discount.objects.create(code='2222', amount=22)
        OrderInfo.objects.create(order=order, status=False, discount=discount, delivery_date=datetime.now(), delivery_address='Test Address', amount_of_money=100)

    def test_customer_label(self):
        orderinfo = OrderInfo.objects.get(id=1)
        field_label = orderinfo._meta.get_field('order').verbose_name
        self.assertEqual(field_label, 'order') 

    def test_status_label(self):
        orderinfo = OrderInfo.objects.get(id=1)
        field_label = orderinfo._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    def test_discount_label(self):
        orderinfo = OrderInfo.objects.get(id=1)
        field_label = orderinfo._meta.get_field('discount').verbose_name
        self.assertEqual(field_label, 'discount')

    def test_delivery_date_label(self):
        orderinfo = OrderInfo.objects.get(id=1)
        field_label = orderinfo._meta.get_field('delivery_date').verbose_name
        self.assertEqual(field_label, 'delivery date')

    def test_delivery_address_label(self):
        orderinfo = OrderInfo.objects.get(id=1)
        field_label = orderinfo._meta.get_field('delivery_address').verbose_name
        self.assertEqual(field_label, 'delivery address')

    def test_amount_of_money_label(self):
        orderinfo = OrderInfo.objects.get(id=1)
        field_label = orderinfo._meta.get_field('amount_of_money').verbose_name
        self.assertEqual(field_label, 'amount of money')

    def test_object_name_orderInfo(self):
        orderinfo = OrderInfo.objects.get(id=1)
        expected_object_name = f'{orderinfo.id} {orderinfo.order} {orderinfo.delivery_date} {orderinfo.delivery_address} {orderinfo.amount_of_money} {orderinfo.status} {orderinfo.discount} {orderinfo.created_at} {orderinfo.updated_at}'
        self.assertEqual(expected_object_name, str(orderinfo))

class CustomerServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Customer.objects.create(name='TestCustomer', phone='+375291234567', email='test@test.com', password='password1')

    def test_get_all(self):
        customers = CustomerService.get_all_users()
        self.assertIsNotNone(customers)
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0].name, 'TestCustomer')
        self.assertEqual(customers[0].phone, '+375291234567')
        self.assertEqual(customers[0].email, 'test@test.com')
        self.assertEqual(customers[0].password, 'password1')

    def test_get_one_by_id(self):
        customer = CustomerService.get_one_user_by_id(1)
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, 'TestCustomer')
        self.assertEqual(customer.phone, '+375291234567')
        self.assertEqual(customer.email, 'test@test.com')
        self.assertEqual(customer.password, 'password1')

    def test_get_one_by_email(self):
        customer = CustomerService.get_one_user_by_email('test@test.com')
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, 'TestCustomer')
        self.assertEqual(customer.phone, '+375291234567')
        self.assertEqual(customer.email, 'test@test.com')
        self.assertEqual(customer.password, 'password1')

    def test_update_all_inf(self):
        customer = CustomerService.update_user_inf('test@test.com','TestCustomer', '+375291234567', 'test1@test.com', 'password1')
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, 'TestCustomer')
        self.assertEqual(customer.phone, '+375291234567')
        self.assertEqual(customer.email, 'test1@test.com')
        self.assertEqual(customer.password, 'password1')

    def test_change_password(self):
        customer = CustomerService.change_user_password(1, 'password2')
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, 'TestCustomer')
        self.assertEqual(customer.phone, '+375291234567')
        self.assertEqual(customer.email, 'test@test.com')
        self.assertEqual(customer.password, 'password2')

    def test_delete(self):
        customer = CustomerService.delete_one_user_by_id(1)
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, 'TestCustomer')
        self.assertEqual(customer.phone, '+375291234567')
        self.assertEqual(customer.email, 'test@test.com')
        self.assertEqual(customer.password, 'password1')

class AuthServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Customer.objects.create(name='Test Customer', phone='+375291111111', email='test@customer.com', password='testpassword')
        Employee.objects.create(name='Test Employee', phone='+375292222222', email='test@employee.com', password='testpassword', is_admin=True)

    def test_sing_up(self):
        new_customer, role = AuthService.sign_up('someName', '+375290000000', 'lox@lox.com', '123pass123')
        self.assertIsNotNone(new_customer)
        self.assertIsNotNone(role)
        self.assertEqual(role, 'user')
        self.assertEqual(new_customer.name, 'someName')
        self.assertEqual(new_customer.phone, '+375290000000')
        self.assertEqual(new_customer.email, 'lox@lox.com')

    def test_sign_in_customer(self):
        user, role = AuthRepository.sign_in('test@customer.com', 'testpassword')
        self.assertIsNotNone(user)
        self.assertIsNotNone(role)
        self.assertEqual(role, 'user')
        self.assertEqual(user.name, 'Test Customer')
        self.assertEqual(user.phone, '+375291111111')
        self.assertEqual(user.email, 'test@customer.com')
        
    def test_sign_in_employee(self):
        user, role = AuthRepository.sign_in('test@employee.com', 'testpassword')
        self.assertIsNotNone(user)
        self.assertIsNotNone(role)
        self.assertEqual(role, 'admin')
        self.assertEqual(user.name, 'Test Employee')
        self.assertEqual(user.phone, '+375292222222')
        self.assertEqual(user.email, 'test@employee.com')

class EmployeeServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Employee.objects.create(name='TestCustomer', phone='+375291234567', email='test@test.com', password='password1', is_admin=False)

    def test_get_all(self):
        customers = EmployeeService.get_all_employees()
        self.assertIsNotNone(customers)
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0].name, 'TestCustomer')
        self.assertEqual(customers[0].phone, '+375291234567')
        self.assertEqual(customers[0].email, 'test@test.com')
        self.assertEqual(customers[0].password, 'password1')

    def test_get_one_by_id(self):
        customer = EmployeeService.get_one_employee_by_id(1)
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, 'TestCustomer')
        self.assertEqual(customer.phone, '+375291234567')
        self.assertEqual(customer.email, 'test@test.com')
        self.assertEqual(customer.password, 'password1')

    def test_get_one_by_email(self):
        customer = EmployeeService.get_one_employee_by_email('test@test.com')
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, 'TestCustomer')
        self.assertEqual(customer.phone, '+375291234567')
        self.assertEqual(customer.email, 'test@test.com')
        self.assertEqual(customer.password, 'password1')

    def test_update_all_inf(self):
        customer = EmployeeService.update_employee_inf('test@test.com','TestCustomer', '+375291234567', 'test1@test.com', 'password1')
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, 'TestCustomer')
        self.assertEqual(customer.phone, '+375291234567')
        self.assertEqual(customer.email, 'test1@test.com')
        self.assertEqual(customer.password, 'password1')

    def test_delete(self):
        customer = EmployeeService.delete_one_employee_by_id(1)
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, 'TestCustomer')
        self.assertEqual(customer.phone, '+375291234567')
        self.assertEqual(customer.email, 'test@test.com')
        self.assertEqual(customer.password, 'password1')

class ProductServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        type = ProductType.objects.create(type='TestType')
        Product.objects.create(name='testproduct', price=12, description='qweqsdadqdqweqdsq', amount=3, type=type, buyed=0)

    def test_get_all(self):
        products = ProductService.get_all_products()
        self.assertIsNotNone(products)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, 'testproduct')
        self.assertEqual(products[0].price, 12)
        self.assertEqual(products[0].description, 'qweqsdadqdqweqdsq')
        self.assertEqual(products[0].amount, 3)
        self.assertEqual(products[0].type.type, 'TestType')
        self.assertEqual(products[0].buyed, 0)

    def test_get_one_by_id(self):
        product = ProductService.get_one_product_by_id(1)
        self.assertIsNotNone(product)
        self.assertEqual(product.name, 'testproduct')
        self.assertEqual(product.price, 12)
        self.assertEqual(product.description, 'qweqsdadqdqweqdsq')
        self.assertEqual(product.amount, 3)
        self.assertEqual(product.type.type, 'TestType')
        self.assertEqual(product.buyed, 0)

    def test_create(self):
        product = ProductService.create_product(name='testproduct2', price=122, description='qweqsdadqdqweqdsqzzz', amount=33, type='TestType')
        self.assertIsNotNone(product)
        self.assertEqual(product.name, 'testproduct2')
        self.assertEqual(product.price, 122)
        self.assertEqual(product.description, 'qweqsdadqdqweqdsqzzz')
        self.assertEqual(product.amount, 33)
        self.assertEqual(product.type.type, 'TestType')
        self.assertEqual(product.buyed, 0)

    def test_update(self):
        product = ProductService.update_product(1 ,name='testproductUpdated', price=12, description='qweqsdadqdqweqdsq', amount=3, type='TestType')
        self.assertIsNotNone(product)
        self.assertEqual(product.name, 'testproductUpdated')
        self.assertEqual(product.price, 12)
        self.assertEqual(product.description, 'qweqsdadqdqweqdsq')
        self.assertEqual(product.amount, 3)
        self.assertEqual(product.type.type, 'TestType')
        self.assertEqual(product.buyed, 0)

    def test_update(self):
        product = ProductService.delete_product(1)
        self.assertIsNotNone(product)
        self.assertEqual(product.name, 'testproduct')
        self.assertEqual(product.price, 12)
        self.assertEqual(product.description, 'qweqsdadqdqweqdsq')
        self.assertEqual(product.amount, 3)
        self.assertEqual(product.type.type, 'TestType')
        self.assertEqual(product.buyed, 0)

class OrderServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        customer = Customer.objects.create(name='TestCustomer', phone='+375291234567', email='test@test.com', password='password1')
        type = ProductType.objects.create(type='TestType')
        product = Product.objects.create(name='testproduct', price=12, description='qweqsdadqdqweqdsq', amount=3, type=type, buyed=1)
        order = Order.objects.create(customer=customer)
        order.products.add(product)
        discount = Discount.objects.create(code='2222', amount=22)
        discount = Discount.objects.create(code='1111', amount=22)
        discount = Discount.objects.create(code='3333', amount=22)
        discount = Discount.objects.create(code='4444', amount=22)
        discount = Discount.objects.create(code='0000', amount=22)
        OrderInfo.objects.create(order=order, status=False, discount=discount, delivery_date=datetime.now(), delivery_address='Test Address', amount_of_money=100)

    def test_get_all(self):
        orders = OrderService.get_all_orders()
        self.assertIsNotNone(orders)
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]['orderId'], 1)
        self.assertEqual(orders[0]['customer']['name'], 'TestCustomer')
        self.assertEqual(orders[0]['orderInfo']['amount_of_money'], 100)

    def test_get_one(self):
        order = OrderService.get_one_order_by_id(1)
        self.assertIsNotNone(order)
        self.assertEqual(order['orderId'], 1)
        self.assertEqual(order['orderInfo']['status'], False)
        self.assertEqual(order['orderInfo']['amount_of_money'], 100)
    
    def test_get_users_orders(self):
        user = Customer.objects.get(id=1)
        order = OrderService.get_all_users_orders(user)
        self.assertIsNotNone(order)
        self.assertEqual(len(order), 1)
        self.assertEqual(order[0]['orderId'], 1)
        self.assertEqual(order[0]['orderInfo']['amount_of_money'], 100)

    def test_create_order(self):
        order = OrderService.create_order('test@test.com', ['1'],  datetime.now() + timedelta(days=1), 'Asd, Some adress 3', '')
        self.assertIsNotNone(order)
        self.assertEqual(order.id, 2)
        self.assertEqual(order.customer.name, 'TestCustomer')

    def test_cancel_order(self):
        order = OrderService.cancel_order(1)
        self.assertIsNotNone(order)
        self.assertEqual(order.customer.name, 'TestCustomer')

class AccountViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        employee = Employee.objects.create(name='TestCustomer', phone='+375291234567', email='test@employee.com', password='password1', is_admin=False)
        customer = Customer.objects.create(name='TestCustomer', phone='+375291234567', email='test@customer.com', password='password1')
        type = ProductType.objects.create(type='TestType')
        product = Product.objects.create(name='testproduct', price=12, description='qweqsdadqdqweqdsq', amount=3, type=type, buyed=1)
        order = Order.objects.create(customer=customer)
        order.products.add(product)
        discount = Discount.objects.create(code='2222', amount=22)
        discount = Discount.objects.create(code='1111', amount=22)
        discount = Discount.objects.create(code='3333', amount=22)
        discount = Discount.objects.create(code='4444', amount=22)
        discount = Discount.objects.create(code='0000', amount=22)
        OrderInfo.objects.create(order=order, status=False, discount=discount, delivery_date=datetime.now(), delivery_address='Test Address', amount_of_money=100)

    def test_get_valid(self):
        session = self.client.session
        session['role'] = 'user'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.get('/account')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/account.html')

    def test_get_redirect(self):
        response = self.client.get('/account')
        self.assertEqual(response.status_code, 302)

    def test_post_save_valid(self):
        session = self.client.session
        session['role'] = 'user'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.post(reverse('account'), data={'action': 'saveMe', 'name': 'New name',
                                                              'phone': '+375291111111', 'email': 'test@employee.com',
                                                              'password': 'testPassword1'})
        self.assertEqual(response.status_code, 302)

    def test_post_save_invalid(self):
        session = self.client.session
        session['role'] = 'user'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.post(reverse('account'), data={'action': 'saveMe', 'name': '',
                                                              'phone': '+375291111111', 'email': 'test@employee.com',
                                                              'password': 'testPassword1'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/account.html')

class SignInViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        employee = Employee.objects.create(name='TestCustomer', phone='+375291234567', email='test@employee.com', password='password1', is_admin=False)
        customer = Customer.objects.create(name='TestCustomer', phone='+375291234567', email='test@customer.com', password='password1')
        type = ProductType.objects.create(type='TestType')
        product = Product.objects.create(name='testproduct', price=12, description='qweqsdadqdqweqdsq', amount=3, type=type, buyed=1)
        order = Order.objects.create(customer=customer)
        order.products.add(product)
        discount = Discount.objects.create(code='2222', amount=22)
        discount = Discount.objects.create(code='1111', amount=22)
        discount = Discount.objects.create(code='3333', amount=22)
        discount = Discount.objects.create(code='4444', amount=22)
        discount = Discount.objects.create(code='0000', amount=22)
        OrderInfo.objects.create(order=order, status=False, discount=discount, delivery_date=datetime.now(), delivery_address='Test Address', amount_of_money=100)

    def test_get_valid(self):
        session = self.client.session
        session['role'] = 'user'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.get('/sign-in')
        self.assertEqual(response.status_code, 302)

    def test_post_save_valid(self):
        response = self.client.post(reverse('sign-in'), {'email': 'test@customer.com', 'password': 'password1',})
        self.assertEqual(response.status_code, 302)

    def test_post_save_invalid(self):
        response = self.client.post(reverse('sign-in'), {'email': 'test@customer.com', 'password': 'qwe'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/login.html')

class AdminPageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        employee = Employee.objects.create(name='TestCustomer', phone='+375291234567', email='test@employee.com', password='password1', is_admin=True)
        customer = Customer.objects.create(name='TestCustomer', phone='+375291234567', email='test@customer.com', password='password1')
        type = ProductType.objects.create(type='TestType')
        product = Product.objects.create(name='testproduct', price=12, description='qweqsdadqdqweqdsq', amount=3, type=type, buyed=1)
        order = Order.objects.create(customer=customer)
        order.products.add(product)
        discount = Discount.objects.create(code='2222', amount=22)
        discount = Discount.objects.create(code='1111', amount=22)
        discount = Discount.objects.create(code='3333', amount=22)
        discount = Discount.objects.create(code='4444', amount=22)
        discount = Discount.objects.create(code='0000', amount=22)
        OrderInfo.objects.create(order=order, status=False, discount=discount, delivery_date=datetime.now(), delivery_address='Test Address', amount_of_money=100)

    def test_get_valid(self):
        session = self.client.session
        session['role'] = 'admin'
        session['user'] = 'test@employee.com'
        session.save()
        response = self.client.get('/admin-page')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/admin.html')

    def test_get_invalid(self):
        session = self.client.session
        session['role'] = 'user'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.get('/admin-page')
        self.assertEqual(response.status_code, 302)

class ProductViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        employee = Employee.objects.create(name='TestCustomer', phone='+375291234567', email='test@employee.com', password='password1', is_admin=True)
        customer = Customer.objects.create(name='TestCustomer', phone='+375291234567', email='test@customer.com', password='password1')
        type = ProductType.objects.create(type='TestType')
        product = Product.objects.create(name='testproduct', price=12, description='qweqsdadqdqweqdsq', amount=3, type=type, buyed=1)
        order = Order.objects.create(customer=customer)
        order.products.add(product)
        discount = Discount.objects.create(code='2222', amount=22)
        discount = Discount.objects.create(code='1111', amount=22)
        discount = Discount.objects.create(code='3333', amount=22)
        discount = Discount.objects.create(code='4444', amount=22)
        discount = Discount.objects.create(code='0000', amount=22)
        OrderInfo.objects.create(order=order, status=False, discount=discount, delivery_date=datetime.now(), delivery_address='Test Address', amount_of_money=100)

    def test_get_valid(self):
        session = self.client.session
        session['role'] = 'user'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/products.html')

    def test_post_invalid(self):
        session = self.client.session
        session['role'] = 'user'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.post(reverse('products'), data={'action': 'saveMe', 'name': 'adsadsd',
                                                              'phone': '+375291111111', 'email': 'test@employee.com',
                                                              'password': 'testPassword1'})
        self.assertEqual(response.status_code, 302)