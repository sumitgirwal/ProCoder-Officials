from django.http import HttpResponse
from django.shortcuts import redirect
from tutorial.models import *

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('tutorial:index')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func



 

def userlock(view_func):
	def wrapper_func(request, *args, **kwargs):
		try:
			if request.session['lock']:
				return redirect('tutorial:lockscreen')
			else:
				return view_func(request, *args, **kwargs)
		except:
			return view_func(request, *args, **kwargs)	
	return wrapper_func


 
 
# def allowed_users(allowed_roles=[]):
# 	def decorator(view_func):
# 		def wrapper_func(request, *args, **kwargs):
# 			group = None
# 			if request.user.groups.exists():
# 				group = request.user.groups.all()[0].name
# 			if group in allowed_roles:
# 				return view_func(request, *args, **kwargs)
# 			else:
# 				return HttpResponse('You are not access brother!!!!!')
# 		return wrapper_func
# 	return decorator

def check_status(view_func):
	def wrapper_function(request, *args, **kwargs):
		user = UserProfile.objects.get(user=request.user)
		status = user.status
		if status == 'USER':
			return redirect('tutorial:userdashboard')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_function