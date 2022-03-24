from django.urls import path, include, re_path
from product.views import *

app_name='Product'
urlpatterns = [


    # Function mehtod views

    # path('list/', inventory_list, name='inventory_list'),

    path('list/form_success/', FormSuccess, name='form_success'),

    # re_path(r'^item/(?P<pk>\d+)$', item_detail, name='item_review'),

    # path('add_product/', item_create, name='item_add'),

    # re_path(r'^item/update/(?P<pk>\d+)$', item_update, name='item_update'),

    # re_path(r'^item/delete/(?P<pk>\d+)$', item_delete, name='delete'),

    # Class method views

    path('list/', Inventory.as_view(), name='inventory_list'),

    re_path(r'^item/(?P<pk>\d+)$', ItemDetail.as_view(), name='item_review'),

    path('add_product/', ItemAdd.as_view(), name='item_add'),

    re_path(r'^item/update/(?P<pk>\d+)$', ItemUpdate.as_view(), name='item_update'),

    re_path(r'^item/delete/(?P<pk>\d+)$', ItemDelete.as_view(), name='delete'),


]