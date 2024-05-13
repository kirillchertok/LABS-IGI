from django.http import Http404
from translate import Translator
from datetime import datetime, timezone
from django.shortcuts import render,redirect
from calendar import month
from django.views import View
from main.infrastracture.data_validators import *
from .services.authService import *
from .services.modelsServices.customerService import *
from .services.modelsServices.employeeService import *
from .services.modelsServices.orderService import *
from .services.modelsServices.productService import *
from .services.modelsServices.productTypeService import *
from .services.modelsServices.discountService import *
from .services.adminService import AdminService
from .services.apiService import ApiService

from .forms import SignInForm, SignUpForm, UpdateInfForm, OrderForm, NewProductForm, AddDiscountForm

def index(request):
    cat_fact = ApiService.get_cat_facts()['fact']
    translator= Translator(from_lang="en", to_lang="ru")
    translation = translator.translate(cat_fact)
    return render(request, 'main/index.html', {
        'cat_fact': translation
    })

class SignInView(View):
    def get(self, request):
        if request.session.get('role') is not None and request.session.get('role') != '':
            return redirect('account')
        else:
            form = SignInForm()
            return render(request, 'main/login.html', {
                'form': form,
                'role': request.session.get('role')
            })
        
    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            try:
                user, role = AuthService.sign_in(form.data['email'], form.data['password'])
                if user is None:
                    form.add_error(None, 'Пользователь не найден')
                else:
                    request.session['role'] = role
                    request.session['user'] = user.email
                    request.session.modified = True
                    return redirect('account')
            except:
                form.add_error(None, 'Ошибка входа')
        return render(request, 'main/login.html', {
                'form': form,
                'role': request.session.get('role')
            }) 
        
class SignUpView(View):
    def get(self, request):
        if request.session.get('role') is not None and request.session.get('role') != '':
            return redirect('account')
        else:
            form = SignUpForm(initial={
                'phone':'+37529'
            })
            return render(request, 'main/registration.html', {
                'form': form,
                'role': request.session.get('role')
            })
        
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user, role = AuthService.sign_up(form.data['name'], form.data['phone'], form.data['email'], form.data['password'])
                if user is None:
                    form.add_error(None, 'Ошибка регистрации')
                else:
                    request.session['role'] = role
                    request.session['user'] = user.email
                    request.session.modified = True
                    return redirect('account')
            except:
                form.add_error(None, 'Ошибка регистрации')
        return render(request, 'main/login.html', {
                'form': form,
                'role': request.session.get('role')
            })  

class LogOutView(View):
    def get(self, request):
        request.session.clear()
        session_validator(request.session)
        return redirect('main')

class AccountView(View):
    def get_user_data(self, request):
        try:
            email = request.session.get('user')
            role = request.session.get('role')
            if response_validator(email, request):
                return None, None, None
            user_data = CustomerService.get_one_user_by_email(email) if role == 'user' else EmployeeService.get_one_employee_by_email(email)
            if response_validator(user_data, request):
                return None, None, None
            if role == 'user':
                user_orders = OrderService.get_all_users_orders(user_data)
                if response_validator(user_orders, request):
                    return None, None, None
            datetime_utc = datetime.now(timezone.utc)
            datetime_local = datetime_utc.astimezone()
            user_orders = user_orders if role == 'user' else OrderService.get_all_orders()
            full_user_inf = {
                'name': user_data.name,
                'email': user_data.email,
                'phone': user_data.phone,
                'orders': user_orders,
                'time_inf': {
                    'timezone': str(datetime_local.tzinfo).split(" ")[0],
                    'date_utc': datetime_utc.strftime('%d/%m/%Y %H:%M'),
                    'date_local': datetime_local.strftime('%d/%m/%Y %H:%M'),
                    'calendar': month(datetime_local.year, datetime_local.month)
                } 
            }
            return user_data, role, full_user_inf
        except:
            return None, None, None

    def get(self, request):
        user_data, role, full_user_inf = self.get_user_data(request)
        user_ip = ApiService.get_user_ip()['ip']
        if response_validator(user_data, request):
            return redirect('main')
        return render(request, 'main/account.html',{
            'form': None,
            'role': role,
            'user': full_user_inf,
            'ip': user_ip
        })    

    def post(self, request):
        user_data, role, full_user_inf = self.get_user_data(request)
        if response_validator(user_data, request):
            return redirect('main')
        if request.POST.get('action') == 'editUserInf':
            form = UpdateInfForm(initial={
                'name': user_data.name,
                'phone': user_data.phone,
                'email': user_data.email
            })
            return render(request, 'main/account.html',{
                'form': form,
                'role': role,
                'user': full_user_inf
            })
        if request.POST.get('action') == 'closeChangeField':
            return render(request, 'main/account.html',{
                'form': None,
                'role': role,
                'user': full_user_inf
            })
        form = UpdateInfForm(request.POST)
        if form.is_valid():
            try:
                if role == 'user':
                    updated_user = CustomerService.update_user_inf(user_data.email, form.data['name'], form.data['phone'], form.data['email'], form.data['password'])
                else:
                    updated_user = EmployeeService.update_employee_inf(user_data.email, form.data['name'], form.data['phone'], form.data['email'], form.data['password'])
                if updated_user is not None:
                    request.session['user'] = updated_user.email
                    request.session.save()
                    return redirect('account')
                else:
                    form.add_error(None, 'Ошибка редактирования')
            except:
                form.add_error(None, 'Ошибка редактирования')
        else:
            return render(request, 'main/account.html',{
                'form': None,
                'role': role,
                'user': full_user_inf
            })
        

class AllProductsView(View):
    def get_all(self):
        try:
            return ProductService.get_all_py_param('price')
        except:
            return None

    def get(self, request):
        if request.session.get('role') is None or request.session.get('role') == '':
            return redirect('sign-in')
        else:
            products = self.get_all()
            for product in products:
                product.description = product.description.split('\n')[0]
            if response_validator(products, request):
                return redirect('main')
            return render(request, 'main/products.html', {
                'form': None,
                'role': request.session.get('role'),
                'products': products
            })

    def post(self, request):
        if request.session.get('role') is None or request.session.get('role') == '':
            return redirect('sign-in')
        else:
            if request.session.get('role') != 'admin':
                return redirect('products')
            if request.POST.get('action') == 'create':
                form = NewProductForm()
                return render(request, 'main/products.html', {
                'form': form,
                'role': request.session.get('role'),
                'products': None
                })
            form = NewProductForm(request.POST)
            if form.is_valid():
                try:
                    description = form.data['smallDescription'] + '\n' + form.data['mainDescription']
                    product = ProductService.create_product(form.data['name'], float(form.data['price']), description, int(form.data['amount']), form.data['type'])
                    if product is not None:
                        return redirect('products')
                    else:
                        form.add_error(None, 'Ошибка создания')
                except:
                    form.add_error(None, 'Ошибка создания')
            return render(request, 'main/products.html', {
                'form': form,
                'role': request.session.get('role'),
                'products': None
                })

class ProductDetailView(View):
    def get_product_by_id(self, id):
        return ProductService.get_one_product_by_id(id)

    def get(self, request, id):
        if request.session.get('role') is None or request.session.get('role') == '':
            return redirect('main')
        product = self.get_product_by_id(id)
        if response_validator(product, request):
            return Http404('Продукт не найдена')
        return render(request, 'main/product-detail.html', {
            'form': None,
            'role': request.session.get('role'),
            'product': product
        })

    def post(self, request, id):
        if request.session.get('role') is None or request.session.get('role') == '':
            return redirect('sign-in')
        else:
            if request.session.get('role') != 'admin':
                return redirect('products')
            if request.POST.get('action') == 'update':
                product = self.get_product_by_id(id)
                smallDescription = product.description.split('\n')[0]
                mainDescription = product.description.split('\n')[1]
                form = NewProductForm(initial={
                    'name': product.name,
                    'price': product.price,
                    'amount': product.amount,
                    'smallDescription': smallDescription,
                    'mainDescription': mainDescription,
                    'type': product.type.type
                })
                return render(request, 'main/products.html', {
                'form': form,
                'role': request.session.get('role'),
                'products': None
                })
            form = NewProductForm(request.POST)
            if form.is_valid():
                try:
                    description = form.data['smallDescription'] + '\n' + form.data['mainDescription']
                    product = ProductService.update_product(int(id),form.data['name'], float(form.data['price']), description, int(form.data['amount']), form.data['type'])
                    if product is not None:
                        return redirect('products')
                    else:
                        form.add_error(None, 'Ошибка создания')
                except:
                    form.add_error(None, 'Ошибка создания')
            return render(request, 'main/products.html', {
                'form': form,
                'role': request.session.get('role'),
                'products': None
                })


class TypesView(View):
    def get_types_data(self, request):
        try:
            types = ProductTypeService.get_all_types()
            if response_validator(types, request):
                return None
            types_data = list()
            for type in types:
                products = ProductService.get_all_products_by_type(type.type)
                if response_validator(products, request):
                    return None
                types_data.append({
                    'type': type.type,
                    'type_products': products[:2]
                })
            return types_data
        except:
            return None

    def get(self, request):
        if request.session.get('role') is None or request.session.get('role') == '':
            return redirect('sign-in')
        else:
            types_data = self.get_types_data(request)
            if response_validator(types_data, request):
                return redirect('main')
            return render(request, 'main/types.html', {
                'form': None,
                'role': request.session.get('role'),
                'types_data': types_data
            })

    def post(self, request):
        pass

class CodesView(View):
    def get(self, request):
        codes = DiscountService.get_all_discounts_by_param('amount')
        if codes is None:
            return redirect('main')
        else:
            return render(request, 'main/discounts.html', {
                'form': None,
                'codes': codes,
                'role': request.session.get('role')
            })

    def post(self, request):
        if request.session.get('role') is None or request.session.get('role') == '':
            return redirect('sign-in')
        else:
            if request.session.get('role') != 'admin':
                return redirect('codes')
            if request.POST.get('action') == 'create':
                form = AddDiscountForm()
                return render(request, 'main/discounts.html', {
                'form': form,
                'codes': None,
                'role': request.session.get('role')
                })
            form = AddDiscountForm(request.POST)
            if form.is_valid():
                try:
                    discount = DiscountService.add_discount(form.data['code'], int(form.data['amount']))
                    if discount is not None:
                        return redirect('codes')
                    else:
                        form.add_error(None, 'Ошибка создания')
                except:
                    form.add_error(None, 'Ошибка создания')
            return render(request, 'main/discounts.html', {
                'form': form,
                'codes': None,
                'role': request.session.get('role')
                })

            

class ChangeCodeStatusView(View):
    def get(self, request, id):
        if request.session.get('role') != 'admin':
            return redirect('codes')
        discount = DiscountService.change_discount_status(id)
        if response_validator(discount, request):
            return redirect('main')
        else:
            return redirect('codes')

    def post(self, request, id):
        pass

class CreateOrderView(View):
    def get(self, request):
        if request.session.get('role') is None or request.session.get('role') == '':
            return redirect('sign-in')
        else:
            form = OrderForm()
            return render(request, 'main/create-order.html', {
                'form': form,
                'role': request.session.get('role')
            })

    def post(self, request):
        email = request.session.get('user')
        role = request.session.get('role')
        if response_validator(email, request) or role != 'user':
            return redirect('main')
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                order = OrderService.create_order(email, form.cleaned_data['products'], form.cleaned_data['date'], form.cleaned_data['address'], form.cleaned_data['sale_code'])
                if order is not None:
                    return redirect('products')
                else:
                    form.add_error(None, 'Ошибка создания заказа')
            except:
                form.add_error(None, 'Ошибка создания заказа')
        return render(request, 'main/create-order.html', {
                'form': form,
                'role': request.session.get('role')
            })

class CancelOrderView(View):
    def get(self, request, id):
        if request.session.get('role') is None or request.session.get('role') == '':
            return redirect('sign-in')
        else:
            order = OrderService.cancel_order(id)
            print(order)
            if response_validator(order, request):
                return redirect('main')
            else:
                return redirect('account')

    def post(self, request, id):
        pass

class AdminView(View):
    def get(self, request):
        if request.session.get('role') != 'admin':
            return redirect('sign-in')
        else:
            products = AdminService.get_price_list()
            orders = AdminService.get_order_for_stat()
            most_popular_products = AdminService.get_popular_products()
            month_stats = AdminService.get_month_volume()
            income = AdminService.get_year_income()
            return render(request, 'main/admin.html',{
                'role': request.session.get('role'),
                'products': products,
                'orders': orders,
                'most_popular_products': most_popular_products,
                'month_stats': month_stats,
                'income': income
            })
        
    def post(self, request):
        pass