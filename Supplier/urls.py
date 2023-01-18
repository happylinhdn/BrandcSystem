from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('export/', views.export_supplier_to_excel, name='export'),
   path('import/', views.import_supplier, name='import'),
   #path('register/', views.register, name='register'),
]