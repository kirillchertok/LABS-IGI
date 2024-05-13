from django.db import models
from django.utils import timezone
from django.urls import reverse


class BaseModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, help_text="Unique ID")
    created_at = models.DateTimeField(default=timezone.now, help_text='Дата добавления')
    updated_at = models.DateTimeField(default=timezone.now, help_text='Дата последнего обновления')

    class Meta:
        abstract = True

class Discount(BaseModel):
    code = models.CharField(max_length=50, help_text='Код скидки')
    amount = models.SmallIntegerField(help_text='Размер скидки')
    is_active = models.BooleanField(help_text='Активен', default=False)

    class Meta:
        db_table = 'sale_codes_table'
        ordering = ['is_active', 'code']

    def get_absolute_url(self):
        return reverse('code-status-change', args=[str(self.id)])

    def __str__(self) -> str:
        return f'{self.id} {self.code} {self.is_active} {self.created_at} {self.updated_at}'  

class ProductType(BaseModel):
    type = models.TextField(unique=True, help_text='Вид изделия')

    class Meta:
        db_table = 'type_table'
        ordering = ['type']

    def __str__(self) -> str:
        return f'{self.id} {self.type} {self.created_at} {self.updated_at}'

class Product(BaseModel):
    name = models.TextField(help_text='Имя изделия')
    price = models.FloatField(help_text='Цена изделия')
    description = models.TextField(help_text='Описание изделия')
    amount = models.PositiveIntegerField(help_text='Количество на складе')
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    buyed = models.PositiveIntegerField(help_text='Всего заказано')

    class Meta:
        db_table='products_table'
        ordering=['-price']

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.price} {self.description} {self.amount} {self.buyed} {self.type} {self.created_at} {self.updated_at}'

class Customer(BaseModel):
    name = models.CharField(max_length=50, help_text='Name')
    phone = models.CharField(max_length=13, unique=True,help_text='Phone number')
    email = models.EmailField(unique=True, help_text='Email')
    password = models.CharField(max_length=300, help_text='Password')

    class Meta:
        db_table = 'customers_table'
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.phone} {self.email} {self.password} {self.created_at} {self.updated_at}'

class Employee(BaseModel):
    name = models.CharField(max_length=50, help_text='Name')
    phone = models.CharField(max_length=13, unique=True,help_text='Phone number')
    email = models.EmailField(unique=True, help_text='Email')
    password = models.CharField(max_length=300, help_text='Password')
    is_admin = models.BooleanField(help_text='Админ/Сотрудник')

    class Meta:
        db_table = 'employees_table'
        ordering = ['-is_admin', 'name']

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.phone} {self.email} {self.password} {self.is_admin} {self.created_at} {self.updated_at}'

class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, help_text='Список заказанных изделий')

    class Meta:
        db_table= 'orders_table'
        ordering=['customer']

    def get_absolute_url(self):
        return reverse('order-delete', args=[str(self.id)])       

    def __str__(self) -> str:
        return f'{self.id} {self.customer} {self.created_at} {self.updated_at}'

class OrderInfo(BaseModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.BooleanField(default=False, help_text='Статус заказа')
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(help_text='Дата доставки')
    delivery_address = models.TextField(default='Minsk, ', help_text='Адрес доставки')
    amount_of_money = models.FloatField(help_text='Сумма заказа')

    class Meta:
        db_table = 'orders_info_table'
        ordering = ['delivery_date']

    def __str__(self) -> str:
        return f'{self.id} {self.order} {self.delivery_date} {self.delivery_address} {self.amount_of_money} {self.status} {self.discount} {self.created_at} {self.updated_at}'







class AboutCompany(BaseModel):
    text = models.TextField(help_text='О компании')   

    class Meta:
        db_table = 'about_company_table'

    def __str__(self) -> str:
        return f'{self.id} {self.text} {self.created_at} {self.updated_at}'
    
class Policy(BaseModel):
    text = models.TextField(help_text='Политика конфиденфиальности')   

    class Meta:
        db_table = 'company_policy_table'

    def __str__(self) -> str:
        return f'{self.id} {self.text} {self.created_at} {self.updated_at}'

class News(BaseModel):
    title = models.CharField(max_length=50, help_text='Заголовок')
    text = models.TextField(help_text='Текст статьи')
    img = models.ImageField(help_text='Фотография', blank=True, upload_to='app/static/main/img', null=True)

    class Meta:
        db_table = 'news_table'
        ordering = ['title']

    def __str__(self) -> str:
        return f'{self.id} {self.title} {self.text} {self.img.url if self.img else "no image"} {self.created_at} {self.updated_at}'

class QA(BaseModel):
    question = models.TextField(help_text='Question')
    answer = models.TextField(help_text='Answer')

    class Meta:
        db_table = 'qa_table'
        ordering = ['id']

    def __str__(self) -> str:
        return f'{self.id} {self.question} {self.answer} {self.created_at} {self.updated_at}'

class EmployeesInf(BaseModel):
    img = models.ImageField(help_text='Фотография сотрудника', blank=True, upload_to='app/static/main/img', null=True)
    work = models.TextField(help_text='Его задачи') 
    other_inf = models.OneToOneField(Employee, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employeesyInf_table'

    def __str__(self) -> str:
        return f'{self.id} {self.work} {self.other_inf} {self.created_at} {self.updated_at}'

class Vacancy(BaseModel):
    name = models.CharField(max_length=50, help_text='Вакансия')
    description = models.TextField(help_text='Описание вакансии')

    class Meta:
        db_table = 'vacancies_table'
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.description} {self.created_at} {self.updated_at}'

class Review(BaseModel):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, help_text='Отправитель')
    rate = models.PositiveSmallIntegerField(help_text='Оценка')
    text = models.TextField(help_text='Текст отзыва')

    class Meta:
        db_table = 'customer_reviews_table'
        ordering = ['rate']

    def __str__(self) -> str:
        return f'{self.id} {self.user.name} {self.rate} {self.text} {self.created_at} {self.updated_at}'     