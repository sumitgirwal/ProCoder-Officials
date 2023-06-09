from django.shortcuts import render, redirect
from blog.models import *

def index(request):
	post = Post.objects.all().order_by('-id')[:6]
	context = {
		'post':post,
	}
	return render(request, 'index.html', context)



 