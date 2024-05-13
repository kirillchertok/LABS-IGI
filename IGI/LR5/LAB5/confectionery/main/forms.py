from typing import Any
from django.contrib.auth.forms import UserCreationForm
from .infrastracture.data_validators import *
from .infrastracture.password_functions import *
from django import forms
from .models import *
from datetime import datetime, timedelta
from .services.modelsServices.productService import *
from .services.modelsServices.discountService import *

class NewProductForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"productNameNew",
        "placeholder":"Введите название продукта...",
        "name":"productname"
        }))
    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        "class":"login-input",
        "id":"productPriceNew",
        "placeholder":"Введите цену продукта...",
        "name":"productprice"
        }))
    smallDescription = forms.CharField(required=True,widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"productSmallDescriptionNew",
        "placeholder":"Введите общее описание продукта...",
        "name":"productsmalldescription"
        }))
    mainDescription = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"productMainDescriptionNew",
        "placeholder":"Введите основне описание продукта...",
        "name":"productmaindescription"
        }))
    amount = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        "class":"login-input",
        "id":"productAmountNew",
        "placeholder":"Введите количество продукта на складе...",
        "name":"productamount"
        }))
    type = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"productTypeNew",
        "placeholder":"Введите тип продукта...",
        "name":"productname"
        }))
    
    def clean(self) -> dict[str, Any]:
        number_validator(self.cleaned_data['price'], float, self)
        number_validator(self.cleaned_data['amount'], int, self)
        return self.cleaned_data
    
    class Meta:
        model = Product
        """ exclude = ['id', 'created_at', 'updated_at'] """

class AddDiscountForm(forms.Form):
    code = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"discountCode",
        "placeholder":"Введите код акции...",
        "name":"discountcode"
        }))
    amount = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        "class":"login-input",
        "id":"discountAmount",
        "placeholder":"Введите размер скидки...",
        "name":"discountamount"
        }))
    
    def clean(self) -> dict[str, Any]:
        number_validator(self.cleaned_data['amount'], int, self)
        return self.cleaned_data

    class Meta:
        model = Discount
        fields = ['code' , 'amount']

class SignUpForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"userNameReg",
        "placeholder":"Введите имя пользователя...",
        "name":"useremail"
        }))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"userPhoneReg",
        "placeholder":"Введите номер телефона...",
        "name":"password"
        }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"userEmailReg",
        "placeholder":"Введите почту...",
        "name":"useremail"
        }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class":"login-input",
        "id":"userPasswordReg",
        "placeholder":"Введите пароль...",
        "name":"password"
        }))
    confirm = forms.BooleanField(help_text='Я подтверждаю, что мне есть 18', required=True)

    def clean(self) -> dict[str, Any]:
        phone_validator(self.cleaned_data['phone'], self)
        password_validator(self.cleaned_data['password'], self)
        return self.cleaned_data
    
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'password']


class SignInForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"userEmailLogin",
        "placeholder":"Введите почту...",
        "name":"useremail"
        }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class":"login-input",
        "id":"userPasswordLogin",
        "placeholder":"Введите пароль...",
        "name":"password"
        }))

    def clean(self) -> dict[str, Any]:
        return self.cleaned_data
    
    class Meta:
        model = Customer
        fields = ['email', 'password']

class UpdateInfForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"userNameUpdate",
        "name":"password"
        }))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"userPhoneUpdate",
        "name":"password"
        }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"userEmailUpdate",
        "name":"useremail"
        }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class":"login-input",
        "id":"userPasswordUpdate",
        "placeholder":"Введите пароль...",
        "name":"password"
        }))
    
    def clean(self) -> dict[str, Any]:
        phone_validator(self.cleaned_data['phone'], self)
        password_validator(self.cleaned_data['password'], self)
        return self.cleaned_data
    
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'password']

class CustomCheckbox(forms.CheckboxSelectMultiple):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option_dict = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        option_dict['attrs']['data-price'] = label.split(' ')[-2]
        return option_dict

class OrderForm(forms.Form):
    products = forms.MultipleChoiceField(
        choices=list(map(lambda b: (b.id, f'{b.name}, {b.type.type}, {b.price} BYN {'(1шт.)' if b.type.type == 'Торт' else '(1кг.)'}'), filter(lambda b: b.amount > 0, ProductService.get_all_py_param('amount')))), 
        required=True, 
        error_messages={'required': 'Выберите хотя бы 1 продукт'}, 
        widget=forms.CheckboxSelectMultiple(attrs={
            "class":"select-product",
            "id":"seleteProductOrder",
            "name":"selectProduct"
        }))
    date = forms.DateField(required=True, error_messages={'required': 'Введите дату'}, initial=datetime.today().date() + timedelta(days=1) , widget=forms.SelectDateWidget(attrs={
        "class":"login-input",
        "id":"selectDateOrder",
        "name":"selectDate"
    }))
    address = forms.CharField(required=True, error_messages={'required': 'Введите адресс'}, widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"userAdressOrder",
        "name":"userAdress",
        "placeholder":"Введите адрес формата: `Город`, `Улица` `Номер дома`"
        }))
    sale_code = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={
        "class":"login-input",
        "id":"userCodeOrder",
        "name":"userAdress",
        "placeholder":"Введите код скидки..."
        }))
    
    def clean_products(self):
        data = self.cleaned_data['products']
        if len(data) == 0:
            self.add_error(None, 'Выберите хотя бы 1 продукт')
            return 'error'
        return data
    
    def clean_date(self):
        data = self.cleaned_data['date']
        if data <= datetime.today().date():
            self.add_error(None, 'Не может быть дата доставки в прошедшем времени')
            return 'err'
        return data

    def clean_address(self):
        data = self.cleaned_data['address']
        if len(data) <= 1 or data.split(',')[0] is None:
            self.add_error(None, 'Укажите корректный адрес')
            return 'err'
        return data
    
    def clean_sale_code(self):
        data = self.cleaned_data['sale_code']
        if len(data) and not DiscountService.check_discount_code(data):
            self.add_error(None, 'Кода не существует или он не активен')
            return 'err'
        return data

    class Meta:
        model = Order