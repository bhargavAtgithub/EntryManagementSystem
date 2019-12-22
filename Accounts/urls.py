from django.urls import path, include
from Accounts import views


app_name = 'Accounts'

urlpatterns = [
    path('', views.CreateVisitor.as_view(), name = "create_visitor"),
    path('visitor_entry/<str:username>/',views.CreateVisitorEntry, name = "accounts_visitor_entry"),
    path('visitor_login/',views.visitor_login, name="visitor_login"),

]
