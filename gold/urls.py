from django.urls import path

from . import views
app_name = "gold"
urlpatterns = [
    path('', views.index, name="index"),
    path('browse/', views.browse, name="browse"),
    path('detail/<int:id>', views.detail, name="detail"),
    
]