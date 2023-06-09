from django.shortcuts import render, redirect
from tutorial.models import *
from friendindeed.models import *
from blog.models import *
from friendindeed.filters import *

#For Course Enrolled
from django.db.models import Q
from django.db.models import Max, Min, Avg

# -*- coding: utf-8 -*-
#for all course printing.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#messages
from django.contrib import messages



#decorators
from django.contrib.auth.decorators import login_required
from tutorial.decorators import *

@login_required(login_url='/tutorial/login_page/')
@userlock
def checkmessages(request):
	if request.method=='POST':
		value = request.POST.get('value')
		if value != '':
			info  = Information.objects.get(id=value)
			info.delete()
			print('Del;eted!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

def load_data(request):		
	user_messages = []
	user_messages_profile = []
	user  = UserProfile.objects.get(user=request.user)
	info =  Information.objects.filter(to_info=user.id)
	for i in info:
		user_messages.append(i)
		user_messages_profile.append(UserProfile.objects.get(id=i.from_info))
		
	user_messages = zip(user_messages_profile, user_messages)	 
	context = {
	'user_messages':user_messages,
	'total_messages':info.count(),

	}
	return context


@login_required(login_url='/tutorial/login_page/')
@userlock
def allusers(request):
	users = UserProfile.objects.all().order_by('-id')
	users = users.filter(~Q(user=request.user)) 

	current_user = UserProfile.objects.get(user=request.user)
	userfilter = UserFilter(request.GET, queryset=users) 
	users = userfilter.qs

 
	if request.method=='POST':
		user_id = request.POST.get('user')
		from_user = UserProfile.objects.get(user=request.user)
		to_user = UserProfile.objects.get(id=user_id)
		friend = Friend()
		friend.from_user = from_user.id
		friend.to_user = to_user.id
		friend.save()
		msg = 'Request Sent to '+str(to_user.user.username)
		messages.success(request, msg)
	
	check = [] 
	for i in  users:		
		 
		try:
			from_user = UserProfile.objects.get(user=request.user)
			to_user = i.id
			friend = Friend.objects.get(from_user=from_user.id, to_user=to_user)
			check.append(True)
		except Exception as e:
			 
			check.append(False)

			
	context = {'users':zip(users,check),'total_user_count':UserProfile.objects.all().count()-1, 'userfilter':userfilter}
	context = dict(context,**load_data(request)) 
	return render(request, 'friendindeed/allusers.html', context)

@login_required(login_url='/tutorial/login_page/')
@userlock
def userfriend(request):
	user = UserProfile.objects.get(user=request.user)
	friend = Friend.objects.filter(_to=user)	
	print(friend,'!!!!!!!!!!!!!!!!!') 

	context = {
		 

	}
	context = dict(context,**load_data(request))
	return render(request, 'friendindeed/userfriend.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def userdashboard(request, slug):

	check = True
	if slug == 'CRNONE':
		check = False 
	else:
		try:
			check_the_chat_room = Member.objects.get(CRID=slug)
		except:
			return redirect('tutorial:error4o4')
	user = UserProfile.objects.get(user=request.user)
	messages = ChatRoom.objects.filter(CRID=slug).order_by('created_date')
	chat_user = None
	try:
		member_users = Member.objects.get(CRID=slug)
		from_ = UserProfile.objects.get(id=member_users.from_member)
		to_   = UserProfile.objects.get(id=member_users.to_member)
		c_user = UserProfile.objects.get(user=request.user)
		
		chat_user = from_
		if from_==c_user:
			chat_user = to_

		# if UserProfile.objects.get(user=request.user) ==  UserProfile.objects.get(id=Member.objects.get(CRID=slug).from_member):
		# 	chat_user = UserProfile.objects.get(id=Member.objects.get(CRID=slug).from_member)	
		# else:	
		# 	chat_user = UserProfile.objects.get(id=Member.objects.get(CRID=slug).to_member)
	except:
		pass
	if request.method=='POST':
		deny = request.POST.get('deny')
		allow = request.POST.get('allow')
		cancel = request.POST.get('cancel')
		message = request.POST.get('message')
		if allow :
			friend = Friend.objects.get(id=allow)
			info = Information(from_info=user.id, to_info=friend.from_user, message="Your request is Accepted :)")
			info.save()
			friend.delete()
			friend = friend.from_user
			member = None
			try:
				member = Member.objects.all().order_by('-id')[0]
			except:
				value = 1
			print(member,'!!!!!!!!!!!!!!!!!!!!')
			if member:
				value = member.id+1 
			CRID = 'CR'+str(value)
			member = Member(CRID=CRID, from_member=user.id, to_member=friend)
			member.save()
			print(allow, friend,'accept!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		elif deny:
			friend = Friend.objects.get(id=deny)
			print(deny, friend,'deline~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``~~~~~~~~~~~~~~~~')
			info = Information(from_info=user.id, to_info=friend.from_user, message="Your request is rejected :(.")
			info.save()
			friend.delete()
		elif cancel:
			friend = Friend.objects.get(id=cancel)
			print(cancel, friend,'Cancel~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``~~~~~~~~~~~~~~~~')
			info = Information(from_info=user.id, to_info=friend.from_user, message="Your request is cancel.")
			info.save()
			friend.delete()
		elif message:	
			chat = ChatRoom(CRID=slug, user=user, message=message)
			chat.save()
		 	
	
	if request.method=='POST':
		value = request.POST.get('value')
		cancel = request.POST.get('cancel')
		if value :
			info  = Information.objects.get(id=value)
			info.delete()
			 
		remove = request.POST.get('remove')
		print(remove)	
		if remove:
			 
			member = Member.objects.get(CRID=remove)
			from_member = member.from_member
			to_member = member.to_member
			member.delete()
			chatroom = ChatRoom.objects.filter(CRID=remove)
			chatroom.delete()
			current_user = UserProfile.objects.get(user=request.user)
			if from_member==current_user.id:	
				info =  Information(from_info=current_user.id, to_info=to_member ,message=str('Your Remove by')+str(from_member))
			else:
				info =  Information(from_info=to_member, to_info=current_user.id,message=str('Your Remove by')+str(to_member))
			check = False
			info.save()

	friend_request  = []
	friend_value = []
	for i in  Friend.objects.filter(Q(to_user=user.id)):
		friend_request.append(UserProfile.objects.get(id=i.from_user))
		friend_value.append(i.id)

	user_request  = []
	user_value  = []
	for i in  Friend.objects.filter(Q(from_user=user.id)):
		user_request.append(UserProfile.objects.get(id=i.to_user))
		user_value.append(i.id)		
	

	friend_request = zip(friend_request, friend_value)
	user_request = zip(user_request, user_value)
		
	 

	member_CRID = []
	member_profile  = []
	from_data = Member.objects.filter(from_member=user.id).order_by('-id')
	to_data = Member.objects.filter(to_member=user.id).order_by('-id')
	for i in  from_data:
		member_CRID.append(i.CRID)		
		member_profile.append(UserProfile.objects.get(id=i.to_member))
	for i in to_data :
		member_CRID.append(i.CRID)		
		member_profile.append(UserProfile.objects.get(id=i.from_member))	

	# member_profile.remove(UserProfile.objects.get(user=request.user))
	# member_CRID.remove(UserProfile.objects.get(user=request.user))
	member = zip(member_profile, member_CRID)
	

	context = {

	'check':check,
	'messages':messages,
	'chat_user':chat_user,
	'user':user,
	'friend_request':friend_request,
	'user_request':user_request,
	'member':member,
	 

		 

	}
	context = dict(context,**load_data(request))
	return render(request, 'friendindeed/userdashboard.html', context)

def index(request):
	posts = Post.objects.all().order_by('-id')[:6]
	users = UserProfile.objects.all().order_by('-id')[:6]
	context = {
		'posts':posts,
		'users':users,
	
	}
	 
	return render(request, 'friendindeed/index.html', context)

