from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [
    path('', views.index, name='index'),
    path('bio/', views.bio, name='bio'),
    path('contact/', views.contact, name='contact'),
    path('<category_name>/', views.show_list, name='post_list'),
    path('post/view/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/delete/<int:post_id>', views.post_delete, name='post_delete'),
    path('post/modify/<int:post_id>', views.post_modify, name='post_modify')
]