from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category, Post
from .forms import PostForm
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    category_list = Category.objects.order_by('id')
    context = {'category_list': category_list}
    return render(request, 'index.html', context)


def bio(request):
    category_list = Category.objects.order_by('id')
    context = {'category_list': category_list}
    return render(request, 'bio.html', context)


def contact(request):
    category_list = Category.objects.order_by('id')
    context = {'category_list': category_list}
    return render(request, 'contact.html', context)


def show_list(request, category_name):
    category = Category.objects.get(name=category_name)
    page = request.GET.get('page', '1')
    post_list = Post.objects.order_by('-create_date')
    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)
    category_list = Category.objects.order_by('id')
    context = {'category_list': category_list, 'category': category, 'post_list': page_obj}
    return render(request, 'post_list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    category_list = Category.objects.order_by('id')
    context = {'category_list': category_list, 'post': post}
    return render(request, 'post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            category = Category.objects.get(id=request.POST['category'])
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.category = category
            post.save()
            return redirect('../../'+category.name+'/')
    else:
        form = PostForm()
    category_list = Category.objects.order_by('id')
    context = {'form': form, 'category_list': category_list}
    return render(request, 'post_form.html', context)


@login_required(login_url='common:login')
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    category = post.category
    if request.user.is_superuser:
        post.delete()
        return redirect('blog:post_list', category_name=category.name)
    else:
        messages.error(request, 'Unauthorized user')
        return redirect('blog:post_detail', post_id=post.id)


@login_required(login_url='common:login')
def post_modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user.is_superuser:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.modify_date = timezone.now()
                post.save()
                return redirect('blog:post_detail', post_id=post.id)
        else:
            form = PostForm(instance=post)
        category_list = Category.objects.order_by('id')
        context = {'form': form, 'category_list': category_list}
        return render(request, 'post_form.html', context)
    else:
        messages.error(request, 'Unauthorized user')
        return redirect('blog:post_detail', post_id=post.id)







