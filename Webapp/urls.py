from django.urls import path
from Webapp import views

urlpatterns = [
    path('home/', views.home_page, name="home"),
    path('about_page/', views.about_page, name="about_page"),
    path('contact_page/', views.contact_page, name="contact_page"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('product_page/', views.product_page, name="product_page"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('filtered_page/<cat_name>/', views.filtered_page, name="filtered_page"),
    path('single_page/<int:pid>/', views.single_page, name="single_page"),
    path('register_page/', views.register_page, name="register_page"),
    path('register_p/', views.register_p, name="register_p"),
    path('user/', views.user, name="user"),
    path('user_out/', views.user_out, name="user_out"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('disp_cart/', views.disp_cart, name="disp_cart"),
    path('logins/', views.logins, name="logins"),

]