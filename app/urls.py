from django.urls import path, include
from app import views

app_name = 'app'

urlpatterns = [
    path('',views.CreateVisitorEntry.as_view(), name = 'visitor_entry'),
    path('host/', views.CreateHost.as_view(), name = 'create_host'),
    path('about/',views.AboutView.as_view(),name = 'about_view'),
    path('accounts/', include('Accounts.urls', namespace='Accounts'))
]