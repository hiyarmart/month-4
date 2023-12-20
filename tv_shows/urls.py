from django.urls import path
from . import views


urlpatterns = [
    path('show_list/', views.show_list, name='show_list'),
    path('show_list/<int:id>/', views.show_detail, name='show_detail'),
    path('show_list_id/<int:id>/', views.show_id_key, name='show_id_key'),
]
