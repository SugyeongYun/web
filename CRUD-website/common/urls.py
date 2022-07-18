from django.urls import path
from django.contrib.auth import views as auth_views
from blog.models import Category

app_name = 'common'

category_list = Category.objects.order_by('id')

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html', extra_context = {'category_list': category_list}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]