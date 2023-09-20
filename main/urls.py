from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('create-product', views.create_product, name='create_product'),
    path('xml', views.show_xml, name='XML'),
    path('json', views.show_json, name='JSON'),
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'), 
    path('register', views.register, name='register'), 
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout')
]
