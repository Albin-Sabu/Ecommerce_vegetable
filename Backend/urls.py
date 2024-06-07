from django.urls import path
from Backend import views

urlpatterns = [
    path('index_page/', views.index_page, name="index_page"),
    path('add_category/', views.add_category, name="add_category"),
    path('category/', views.category, name="category"),
    path('disp/', views.disp, name="disp"),
    path('edit_cat/<int:cid>/', views.edit_cat, name="edit_cat"),
    path('update_cat/<int:cid>/', views.update_cat, name="update_cat"),
    path('delete_cat/<int:cid>/', views.delete_cat, name="delete_cat"),
    path('login_page/', views.login_page, name="login_page"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('sign_out/', views.sign_out, name="sign_out"),
    path('add_products/', views.product_page, name="add_products"),
    path('product_reg/', views.product_reg, name="product_reg"),
    path('disp_p/', views.disp_p, name="disp_p"),
    path('edit_p/<int:pid>/', views.edit_p, name="edit_p"),
    path('update_pd/<int:pid>/', views.update_pd, name="update_pd"),
    path('delete_pd/<int:pid>/', views.delete_pd, name="delete_pd"),
    path('contact_details/', views.contact_details, name="contact_details"),
    path('delete_contact/<int:cid>/', views.delete_contact, name="delete_contact"),

]