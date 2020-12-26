from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
	posts = Post.objects
	return render(request, 'postslist.html', {'posts': posts})

def post_create(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	else:
		form = PostForm()
	return render(request, 'postcreate.html', {'form': form})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)

	return render(request, 'postdetail.html', {'post': post})

def post_update(request, pk):
	post = get_object_or_404(Post, pk=pk)

	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect('home')

	else:
		form = PostForm(instance=post)
	return render(request, 'postupdate.html', {'form': form})

def post_delete(request, pk):
	post = Post.objects.get(pk=pk)
	post.delete()
	return redirect('home')