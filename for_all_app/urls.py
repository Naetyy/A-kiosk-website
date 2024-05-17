from django.contrib.auth.views import LoginView
from . import views
from django.urls import path


urlpatterns = [
    path("home", views.Home, name='home'),
    # path("home/<str:searchQuiry>/", views.Home, name='home'),
    path("about", views.About, name='about'),
    path("buy/<int:id>/", views.Buy, name='buy'),
    path("cart/<int:id>/", views.cart, name='cart'),
    path("search/", views.Search, name='search'),
    path("signup", views.SignUp, name='signup'),
    path("delete", views.delete, name='delete'),


    path('', LoginView.as_view(template_name= 'login.html'), name='login'),
    path('logout/', views.logout, name="logout"),

]
