from django.urls import path
from . import views
from app.views import LogoutAllView,LogoutView
  
urlpatterns = [
    path('login/', views.HelloView.as_view(), name ='hello'),
    path('logoutall/', LogoutAllView, name='auth_logout_all'),
    path('logout/', LogoutView, name='auth_logout'),

]



