from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('booklist', views.booklist, name='booklist'),
    path('bookview/<int:id>', views.bookview, name='bookview'),
    path('createbook', views.createbook, name='createbook'),
    path('editbook/<int:id>', views.editbook, name='editbook'),
    path('deletebook/<int:id>', views.deletebook, name='deletebook'),

    #path('customerlist', views.customerlist, name='customerlist'),
    #path('customerview/<int:id>', views.customerview, name='customerview'),
    #path('createcustomer', views.createcustomer, name='createcustomer'),
    #path('editcustomer/<int:id>', views.editcustomer, name='editcustomer'),
    #path('deletecustomer/<int:id>', views.deletecustomer, name='deletecustomer')
    
    #path('orderlist', views.orderlist, name='orderlist'),
]
