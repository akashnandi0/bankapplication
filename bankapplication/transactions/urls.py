from django.urls import path
from transactions.views import transferamount, depositamount, withdrawamount, balance
urlpatterns = [
    path('transferamount/',transferamount,name='transferamount'),
    path('depositamount/',depositamount,name='depositamount'),
    path('withdrawamount/',withdrawamount,name='withdrawamount'),
    path('balance/',balance,name='balanceenquiry')
]