from django.urls import path, re_path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='main'),

    path('sign-in', SignInView.as_view(), name='sign-in'),
    path('sign-up', SignUpView.as_view(),name='sign-up'),
    path('log-out', LogOutView.as_view(), name='log-out'),

    path('account', AccountView.as_view(), name='account'),
    re_path(r'^account/(?P<id>\d+)$', CancelOrderView.as_view(), name='order-delete'),

    path('products', AllProductsView.as_view(), name='products'),
    re_path(r'^products/(?P<id>\d+)$', ProductDetailView.as_view(), name='product-detail'),

    path('types', TypesView.as_view(), name='types'),

    path('codes', CodesView.as_view(), name='codes'),
    re_path(r'^codes/(?P<id>\d+)$', ChangeCodeStatusView.as_view(), name='code-status-change'),

    path('create-order', CreateOrderView.as_view(), name='create-order'),

    path('admin-page', AdminView.as_view(), name='admin-page')
]
