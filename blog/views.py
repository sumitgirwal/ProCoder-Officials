#Build in function
from django.shortcuts import render, redirect

#User define modules
from blog.models import *
from blog.forms import *
from tutorial.forms import *
from blog.filters import * 

#More function
from django.contrib import messages
from django.contrib.auth.models import User

#For Course Enrolled
from django.db.models import Q
from django.db.models import Max, Min, Avg

# -*- coding: utf-8 -*-
#for all course printing.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.db.models.aggregates import Max

import math
import random

#decorators
from django.contrib.auth.decorators import login_required
from tutorial.decorators import *


def index(request):
	posts = Post.objects.all().order_by('-id')[:6]
	context = {
	'posts':posts,

	}
	return render(request, 'blog/index.html', context)





# @login_required(login_url='/tutorial/login_page/')
# @userlock
# @check_status 
@login_required(login_url='/tutorial/login_page/')
@userlock
def allpost(request):
	posts_list = Post.objects.all().order_by('-modify_date')
	paginator =  Paginator(posts_list, 6)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)

	category = Category.objects.all()	
	
	 
	context = {'posts':posts,'total_post':posts_list.count(), "category" : Category.objects.all(),
		"hotposts" : Post.objects.all().order_by('-post_view')[:5],"total_post":Post.objects.all().count() } 
	return render(request, 'blog/allpost.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def postview(request, id):
	post = Post.objects.get(id=id)
	post.post_view+=1
	post.save()	
	post = Post.objects.get(id=id)
	check = False
	try:
		user = UserProfile.objects.get(user=request.user)
		like = post.like_set.filter(Q(user=user))
		 
		if like :
			check = True
		if request.method=='POST':
			data = request.POST.get('data')
			if data=='like':
				like = Like(post=post, user=user)
				like.save()	
				check = True
			elif data=='notlike':
				like = Like.objects.get(post=post, user=user)
				like.delete()	
				check = False
			else :
				comment = request.POST.get('data')
				print(request.POST.get('data'))
				comment = Comment(post=post, user=user, comment=comment)
				comment.save()	

	except Exception as e:
		print(e)

	# dictsortreversed==order_by('-id') and dictsort==order_by('id') %}
	
	context = {
		'current_user':UserProfile.objects.get(user=request.user),
		'post':post,
		'check':check,
		'category':Category.objects.all(),
		"hotposts" : Post.objects.all().order_by('-post_view')[:5],

	} 
	return render(request, 'blog/postview.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def userpost(request):
	user = UserProfile.objects.get(user=request.user)
	post = user.post_set.order_by('-id')
	form = PostForm() 
	forms = []
	for i in post:
		forms.append(PostForm(instance=i))
	ziped_data = zip(post, forms)

	
	context = {'post':post, 'form':form, 'forms':forms, 'ziped_data':ziped_data, } 
	return render(request, 'blog/userpost.html', context)

@login_required(login_url='/tutorial/login_page/')
@userlock
def postcreate(request):
	form = PostForm()
	user = UserProfile.objects.get(user=request.user)
	if request.method=='POST':
		form = PostForm(request.POST,request.FILES,instance=Post(user=user) )
		if form.is_valid():
			post = form.save()
			msg = 'New Post "'+str(form.cleaned_data['post_title'])+'" Created Successfully.'
			messages.success(request, msg)
			return redirect('blog:userpost')
		else:
			messages.debug(request, str(form.errors))
			print(str(form.errors))
			return redirect('blog:userpost')

	context = {'form':form}
	return render(request, 'blog/userpost.html',context)

@login_required(login_url='/tutorial/login_page/')
@userlock
def postedit(request,id):
	post = Post.objects.get(id=id)
	form = PostForm(instance=post)
	if request.method=='POST':
		form = PostForm(request.POST,request.FILES,  instance=post)
		if form.is_valid():
			form.save()
			msg =  'Post '+str(form.cleaned_data['post_title'])+' updated successfully.'
			messages.info(request, msg)
			return redirect('blog:userpost')
		else:
			messages.error(request, form.error+' Form Errors ')
			print(str(form.error))
			return redirect('blog:userpost')

	context = {'form':form}
	return render(request, 'blog/userpost.html', context)

@login_required(login_url='/tutorial/login_page/')
@userlock
def postdelete(request,id):
	post = Post.objects.get(id=id)
	if request.method=='POST':
		post_title = post.post_title
		post.delete()
		messages.error(request,post_title+' Post deleted successfully.')
		return redirect('blog:userpost')
	else:
		messages.error(request,' Error')
		return redirect('blog:userpost')
	context = {'post':post}
	return render(request, 'blog/userpost.html', context)


 
def load_data(request):
		
	users = UserProfile.objects.all().order_by('-id')[:6] #[::-1] FOR Assending Order
	total_users = UserProfile.objects.all().count()
	total_active_users = User.objects.all().filter(is_active=True).count()
	total_deactive_users = User.objects.all().filter(is_active=False).count()
	
	courseenroll =  CourseEnroll.objects.all().order_by('-id')[:5]


	 
	total_posts = Post.objects.all().count()


	total_course_enrolled = CourseEnroll.objects.all().count()
	total_categorys = Category.objects.all().count()
	
	category = Category.objects.all().order_by('-id')[:5]
	#total_categorys = Category.objects.all().order_by('-id')[:5]

	total_content = Content.objects.all().count()

	quiztaken = QuizTaken.objects.all().order_by('-id')[:5]
	total_comments = Comment.objects.all().count()
	total_quiz_taken = QuizTaken.objects.all().count()
	total_qnas = Qna.objects.all().count()

	total_quizattempted = UserPerformance.objects.all().count()	

	total_feedback = Feedback.objects.all().count()

	userprofile = UserProfile.objects.get(user=request.user)

	total_skill = Skill.objects.all().count()

	total_likes = Like.objects.all().count()
	context = {

		'userprofile':			userprofile,
		'category':				category,
 
		'users':				users,
		'total_users':			total_users,
		'total_active_users':	total_active_users,
		'total_deactive_users':	total_deactive_users,

		'courseenroll':			courseenroll,
	 
		'total_posts':		total_posts,
		'total_course_enrolled':total_course_enrolled,
		'total_categorys':			total_categorys,
		'total_content':		total_content,

		'quiztaken':			quiztaken,
		'total_comments':			total_comments,
		'total_quiz_taken':		total_quiz_taken,
		'total_qnas':			total_qnas,
		'total_quizattempted':	total_quizattempted,

		'total_feedback':		total_feedback,
		'total_skill':			total_skill,
		'total_likes':          total_likes,
	}
	return context


@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status
def admin_panel(request):
	posts = Post.objects.all().order_by('-id')[:10]
	comments = Comment.objects.all().order_by('-id')[:10]
	likes = Like.objects.all().order_by('-id')[:10]	
	categorys = Category.objects.all().order_by('-id')[:10]
	context = {
	'total_user':UserProfile.objects.all().count(),
	'total_post':Post.objects.all().count(),
	'total_comment': Comment.objects.all().count(),
	'total_like': Like.objects.all().count(),
	'comments':comments,
	'posts':posts,
	'likes':likes,
	'categorys':categorys,
	

	}
	context = dict(context,**load_data(request))
	return render(request, 'blog/admin_panel.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status
def user(request):
	users = UserProfile.objects.all().order_by('-id')
	form = UserProfileForm() 
	forms = []
	for user in users:
		forms.append(UserProfileForm(instance=user))
	ziped_data = zip(users, forms)
	context = {'users':users, 'form':form, 'forms':forms, 'ziped_data':ziped_data, } 
	context = dict(context,**load_data(request))
	return render(request, 'blog/user.html',context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def usercreate(request):
	form = UserProfileForm()
	if request.method=='POST':
		form = UserProfileForm(request.POST,request.FILES )
		if form.is_valid():
			form.save()
			msg = 'New User "'+str(form.cleaned_data['user'])+'" Created Successfully.'
			messages.success(request, msg)
			return redirect('blog:user')
		else:
			messages.debug(request, str(form.errors))
			print(str(form.errors))
			return redirect('blog:user')

	context = {'form':form}
	return render(request, 'tutorial/user.html',context)



@login_required(login_url='/tutorial/login_page/')
@userlock
def useredit(request,id):
	user = UserProfile.objects.get(id=id)
	form = UserProfileForm(instance=user)
	if request.method=='POST':
		form = UserProfileForm(request.POST,request.FILES,  instance=user)
		if form.is_valid():
			form.save()
			msg =  'User '+str(form.cleaned_data['user'])+' updated successfully.'
			messages.info(request, msg)
			return redirect('blog:user')
		else:
			messages.error(request, form.errors+' Form Errors ')
			print(str(form.errors))
			return redirect('blog:user')

	context = {'form':form}
	return render(request, 'tutorial/user.html', context)

@login_required(login_url='/tutorial/login_page/')
@userlock
def userdelete(request,id):
	user = User.objects.get(id=id)
	if request.method=='POST':
		username = user.username
		user.delete()
		messages.error(request,username+' User deleted successfully.')
		return redirect('blog:user')
	else:
		messages.error(request,' Error')
		return redirect('blog:user')
	context = {'user':user}
	return render(request, 'tutorial/user.html', context)

@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status
def post(request):
	user = UserProfile.objects.get(user=request.user)
	post = user.post_set.order_by('-id')
	form = PostForm() 
	forms = []
	for i in post:
		forms.append(PostForm(instance=i))
	ziped_data = zip(post, forms)	
	context = {'post':post, 'form':form, 'forms':forms, 'ziped_data':ziped_data, } 
	context = dict(context,**load_data(request))
	return render(request, 'blog/post.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status
def category(request):
	categorys = Category.objects.all().order_by('-id')
	form = CategoryForm() 
	forms = []
	for i in categorys:
		forms.append(CategoryForm(instance=i))
	ziped_data = zip(categorys, forms)	
	context = {'categorys':categorys, 'form':form, 'forms':forms, 'ziped_data':ziped_data, } 
	context = dict(context,**load_data(request))
	return render(request, 'blog/category.html', context)



@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status
def categorycreate(request):
	form = CategoryForm()
	if request.method=='POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			msg = 'New Category "'+str(form.cleaned_data['category'])+'"  Created Successfully.'
			messages.success(request, msg)
			return redirect('blog:category')
		else:
			messages.debug(request, str(form.errors))
			print(str(form.errors))
			return redirect('blog:category')

	context = {'form':form}
	return render(request, 'blog/category.html',context)

@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status
def categoryedit(request,id):
	category = Category.objects.get(id=id)
	form = CategoryForm(instance=category)
	if request.method=='POST':
		form = CategoryForm(request.POST,instance=category)
		if form.is_valid():
			form.save()
			msg =  'Category '+str(form.cleaned_data['category'])+' updated successfully.'
			messages.info(request, msg)
			return redirect('blog:category')
		else:
			messages.error(request, form.error+' Form Errors ')
			print(str(form.error))
			return redirect('blog:category')

	context = {'form':form}
	return render(request, 'blog/category.html', context)

@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status
def categorydelete(request,id):
	category = Category.objects.get(id=id)
	if request.method=='POST':
		categoryname = category.category
		category.delete()
		messages.error(request,categoryname+' Category deleted successfully.')
		return redirect('blog:category')
	else:
		messages.error(request,' Error')
		return redirect('blog:category')
	context = {'category':category}
	return render(request, 'blog/category.html', context)




@login_required(login_url='/tutorial/login_page/')
@userlock
def comment(request):
	comments = Comment.objects.all().order_by('-id')
	form = CommentForm() 
	forms = []
	for i in comments:
		forms.append(CommentForm(instance=i))
	ziped_data = zip(comments, forms)	
	context = {'comments':comments, 'form':form, 'forms':forms, 'ziped_data':ziped_data, } 
	context = dict(context,**load_data(request))
	return render(request, 'blog/comment.html', context)



@login_required(login_url='/tutorial/login_page/')
@userlock
def commentcreate(request):
	form = CommentForm()
	if request.method=='POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()
			msg = 'New Comment "'+str(form.cleaned_data['comment'])+'"  Created Successfully.'
			messages.success(request, msg)
			return redirect('blog:comment')
		else:
			messages.debug(request, str(form.errors))
			print(str(form.errors))
			return redirect('blog:comment')

	context = {'form':form}
	return render(request, 'blog/comment.html',context)

@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status
def commentedit(request,id):
	comment = Comment.objects.get(id=id)
	form = CommentForm(instance=comment)
	if request.method=='POST':
		form = CommentForm(request.POST,instance=comment)
		if form.is_valid():
			form.save()
			msg =  'Comment '+str(form.cleaned_data['comment'])+' updated successfully.'
			messages.info(request, msg)
			return redirect('blog:comment')
		else:
			messages.error(request, form.error+' Form Errors ')
			print(str(form.error))
			return redirect('blog:comment')

	context = {'form':form}
	return render(request, 'blog/comment.html', context)

@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status
def commentdelete(request,id):
	comment = Comment.objects.get(id=id)
	if request.method=='POST':
		commentname = comment.comment
		comment.delete()
		messages.error(request,commentname+' Category deleted successfully.')
		return redirect('blog:comment')
	else:
		messages.error(request,' Error')
		return redirect('blog:comment')
	context = {'comment':comment}
	return render(request, 'blog/comment.html', context)

 
@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status
def analysis(request): 
	posts_data = []
	posts = Post.objects.all().order_by('-post_view')[:10]
	for i in posts:
		posts_data.append(i.post_view)
	
	categorys = Category.objects.all()
	category_data = []
	category_bg = []
	for i in categorys:
		category_data.append(i.post_set.all().count())	
		 

	posts = Post.objects.all()
	like_data = []
	like_label = []
	for i in posts:
		like_label.append(i)
		like_data.append(i.like_set.all().count())
		
	for i in range(len(like_data)): 
		min_idx = i 
		for j in range(i+1, len(like_data)): 
			if like_data[min_idx] < like_data[j]: 
				min_idx = j 
		like_label[i], like_label[min_idx] = like_label[min_idx], like_label[i]
		like_data[i], like_data[min_idx] = like_data[min_idx], like_data[i]  
	


	comment_data = []
	comment_label = []
	for i in posts:
		comment_label.append(i)
		comment_data.append(i.comment_set.all().count())
		
	for i in range(len(comment_data)): 
		min_idx = i 
		for j in range(i+1, len(comment_data)): 
			if comment_data[min_idx] < comment_data[j]: 
				min_idx = j 
		comment_label[i], comment_label[min_idx] = comment_label[min_idx], comment_label[i]
		comment_data[i], comment_data[min_idx] = comment_data[min_idx], comment_data[i] 	


	user_data = []
	user_label = []
	users = UserProfile.objects.all()
	for i in users:
		user_label.append(i)
		user_data.append(i.post_set.all().count())
	for i in range(len(user_data)): 
		min_idx = i 
		for j in range(i+1, len(user_data)): 
			if user_data[min_idx] < user_data[j]: 
				min_idx = j 
		user_label[i], user_label[min_idx] = user_label[min_idx], user_label[i]
		user_data[i], user_data[min_idx] = user_data[min_idx], user_data[i] 	

	





	context = {

	"posts":posts,
	'posts_data':posts_data,	

	'like_label':like_label,
	'like_data':like_data,


	'comment_label':comment_label,
	'comment_data':comment_data,

	'categorys':categorys,
	'category_data':category_data,
	
	'user_data':user_data[:10],
	'user_label':user_label[:10],

	}
	context = dict(context,**load_data(request))
	return render(request, 'blog/analysis.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def postsearch(request):
	posts = Post.objects.all().order_by('-id')
	postfilter = PostFilter(request.GET, queryset=Post.objects.all()) 
	posts = postfilter.qs

	hotposts = Post.objects.all().order_by('-post_view')[:5]
	 
	context = {
	"category" : Category.objects.all(),
	'posts':posts,
	'postfilter':postfilter,
	'hotposts':hotposts,


	}
	 
	return render(request, 'blog/postsearch.html', context)


 