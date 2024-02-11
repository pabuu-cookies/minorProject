from django.urls import path
from .views import c_canteen_view, s_canteen_view, orders_view, add_item

urlpatterns = [
    path('c_canteen/', c_canteen_view, name='c_canteen'),
    path('s_canteen/', s_canteen_view, name='s_canteen'),
    path('order/', orders_view, name='orders'),
    path('s_canteen/addMenuItem', add_item, name='add_new_menuItem'),
]
