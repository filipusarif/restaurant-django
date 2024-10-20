from django.urls import path
from main.views import show_main,login_owner,login_customer, register_owner, register_customer, logout_user
app_name = 'main'

urlpatterns = [
    path("",show_main,name="show_main"),
    path("login/owner",login_owner,name="login_owner"),
    path("login/customer",login_customer,name="login_customer"),
    path("register/owner",register_owner,name="register_owner"),
    path("register/customer",register_customer,name="register_customer"),
    path("logout/",logout_user,name="logout_user")
]