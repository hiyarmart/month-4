from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_list, name='show_list'),
    path('show_list/<int:id>/', views.show_detail, name='show_detail'),
    path('show_list_id/<int:id>/', views.show_id_key, name='show_id_key'),
    path('create_show/', views.show_create_view, name='create_show'),
    path('show_list_delete/', views.show_list_delete_view, name='show_list_delete'),
    path('show_drop/<int:id>/delete/', views.show_drop_view, name='show_drop'),
    path('show_list_update/', views.show_list_edit_view, name='show_list_update'),
    path('show_update/<int:id>/update/', views.show_update, name='show_update'),
]
