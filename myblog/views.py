from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'myblog/index.html', {'posts': posts})


def add_post(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма'
    else:
        form = PostForm()

    return render(request, 'myblog/add.html', {'form': form, 'error': error})


