from django.shortcuts import render, redirect	
from django.urls import reverse

#User Default
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#For printing the exception
import traceback

#User Define
from tutorial.models import *
from blog.models import *
from friendindeed.models import *

from tutorial.forms import *
from tutorial.decorators import *


import unicodedata

#For Course Enrolled
from django.db.models import Q
from django.db.models import Max, Min, Avg

# -*- coding: utf-8 -*-
#for all course printing.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime

#Object 
from django.shortcuts import get_list_or_404, get_object_or_404 
 
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

#decorators
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse











# from django.contrib.auth.tokens import default_token_generator
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template import loader
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError
# from django.core.mail import send_mail
# from settings import DEFAULT_FROM_EMAIL
# from django.views.generic import *
# from utils.forms.reset_password_form import PasswordResetRequestForm
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.db.models.query_utils import Q





#################################################################################################33
import csv
import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User

def export_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="ProcoderDataBase.csv"'
	writer = csv.writer(response)

	#Users
	writer.writerow([])
	writer.writerow(['User ID', 'User Name', 'Last Login'])
	rows = User.objects.all().values_list('id', 'username','last_login')
	for row in rows:
		writer.writerow(row) 

	#Users Profile
	writer.writerow([])
	writer.writerow([
			'User', 'Status','First name', 
			'Last name', 'Email address','About',
			'Linkedin', 'Github', 'Twitter',
			'Facebook', 'Skill', 'Age','Joined Date', 'Updated Date'
			 ])
	rows = UserProfile.objects.all().values_list(
			'user',
			'status', 
			'first_name',
			'last_name', 
			'email',
			'about', 
			'linkedin',
			'github', 
			'twitter',
			'facebook', 
			'skill',
			'age', 
			'created_date',
			'modify_date',
		 )
	for row in rows:
		writer.writerow(row)  

	#Skill Objects
	writer.writerow([])
	writer.writerow([
				'Skill Name',
			'Skill Icon',
			'Message',
 		   
			 ])
	rows = Skill.objects.all().values_list(
				'skill', 'skill_icon'
		 )
	for row in rows:
		writer.writerow(row)  
		

	#Feedback Objects
	writer.writerow([])
	writer.writerow([
				'Email',
			'Feedback',
			'Notify',

			'Date Time',
			 
 		   
			 ])
	rows = Feedback.objects.all().values_list(
				'email', 'feedback','notify',

			'created_date',
			 
		 )
	for row in rows:
		writer.writerow(row)  
			
	#Rating
	writer.writerow([])
	writer.writerow([
			'User', 'Star1','Star2', 
			'Star3', 'Star4','Star5',
		   
			 ])
	rows = Rating.objects.all().values_list(
			'user',
			'star1', 
			'star2',
			'star3', 
			'star4',
			'star5', 
		 )
	for row in rows:
		writer.writerow(row)  
	
	#ByRating Objects	
	writer.writerow([])
	writer.writerow([
			'User', 'Rating By','Rating Yes/No',
		   
			 ])
	rows = ByRating.objects.all().values_list(
			'user',
			'rating_by', 
			'is_rating',
		 
		 )
	for row in rows:
		writer.writerow(row)  
	

	#Key Objects	
	writer.writerow([])
	writer.writerow([
			'User', 'Key',
			 ])
	rows = Key.objects.all().values_list(
			'user',
			'key',
		 
		 )
	for row in rows:
		writer.writerow(row)

	#Workflow Objects	
	writer.writerow([])
	writer.writerow([
			'User', 'Workflow',
			 ])
	rows = Workflow.objects.all().values_list(
			'user',
			'workflow',
		 
		 )
	for row in rows:
		writer.writerow(row)

	#Interest Objects	
	writer.writerow([])
	writer.writerow([
			'User', 'Interest',
			 ])
	rows = Interest.objects.all().values_list(
			'user',
			'interest',
		 
		 )
	for row in rows:
		writer.writerow(row)  
	

	#Award Objects	
	writer.writerow([])
	writer.writerow([
			'User', 'Award',
			 ])
	rows = Award.objects.all().values_list(
			'user',
			'award',
		 
		 )
	for row in rows:
		writer.writerow(row)  
	
	#Course Objects	
	writer.writerow([])
	writer.writerow([
				'User', 

			'Slug','Course', 'Course Description',
			'Skill','Created Date',
			'Modify Date',
 		   
			 ])
	rows = Course.objects.all().values_list(
			'user',
			'slug', 'course_name', 'course_description', 
			'skill', 

			'created_date',
			'modify_date', 
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
	
	#CourseEnroll Objects		
	writer.writerow([])
	writer.writerow([
				'User', 'Course', 
			'Enrollment', 
 		   'Created Date'
			 ])
	rows = CourseEnroll.objects.all().values_list(
			'user',
			'course', 'user_enrollment',
			'created_date',
			 
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
		
	#Topic Objects		
	writer.writerow([])
	writer.writerow([
				'Topic Name',  
 		   
			 ])
	rows = Topic.objects.all().values_list(
			'topic_name',
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
			
	#Quiz Objects	
	writer.writerow([])
	writer.writerow([
					'User', 'Course','Quiz Name','Quiz Description',
					'Created Date', 'Updated Date', 
 		
 		   
			 ])
	rows = Quiz.objects.all().values_list(
				'user','course','quiz_name',
			'quiz_description',
			 'created_date',
			'modify_date', 
		 
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
			
			
	#Qna Objects	
	writer.writerow([])
	writer.writerow([
						'Quiz ID', 'Question','Answer',
			'Option_1','Option_2','Option_3','Option_4', 
 		   
			
 		   
			 ])
	rows = Qna.objects.all().values_list(
			'quiz','question','answer',
			'option_1',	'option_2',
			'option_3',	'option_4',
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
	

	#QuizTaken Objects	
	writer.writerow([])
	writer.writerow([
				'User ID', 'Quiz','User Enrolled',
			'Quiz Enrolled', 
			
 		   
			 ])
	rows = QuizTaken.objects.all().values_list(
			'user','quiz','user_enrollment',
			'quiz_taken',	
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
	
	#UserPerformance Objects	
	writer.writerow([])
	writer.writerow([
			'User ID', 'Correct Answer','Wrong Answer',
			'Not Answer','No. of Questions'  
 		  
			
 		   
			 ])
	rows = UserPerformance.objects.all().values_list(
			'user','correct_answer','wrong_answer',
			'none_answer',	'total_qna' 	
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
	
	#Content Objects	
	writer.writerow([])
	writer.writerow([
			'Course', 'Topic','No. of View' ,
 		   'Created Date',
			'Updated Date', 
		 
 		  
			
 		   
			 ])
	rows = Content.objects.all().values_list(
			'course','topic',
			'view',	
		 'created_date',
			'modify_date', 
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
	
	#Category Objects	
	writer.writerow([])
	writer.writerow([
			'Category',    
 		   
 		  
			
 		   
			 ])
	rows = Category.objects.all().values_list(
			'category', 
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
	
	#post Objects	
	writer.writerow([])
	writer.writerow([
		'User ID',
			'Post Title',
			'Category',
			'Post View',    
 		   'Published Date',
			'Updated Date', 
		 
 		  
			
 		   
			 ])
	rows = Post.objects.all().values_list(
			'user', 'post_title','category','post_view','created_date',
			'modify_date', 
		 
			 
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  

	#Comment Objects	
	writer.writerow([])
	writer.writerow([
		'Post ID',
			'User ID ',
			'Comment',    
 		   
 		  'Created Date'
			
 		   
			 ])
	rows = Comment.objects.all().values_list(
			'post', 'user','comment', 
			 'created_date',
	 
			 
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
	
	#Like Objects	
	writer.writerow([])
	writer.writerow([
			'Post ID',
			'User ID ',
			'Created Date', 
 		   
 		  
			
 		   
			 ])
	rows = Like.objects.all().values_list(
				'post', 'user',
			 
			 'created_date',
			  
		 
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
	
	#Friend Objects	
	writer.writerow([])
	writer.writerow([
			'From User',
			'To User',
			'Friend',
 		   'Created Date'
 		  
			
 		   
			 ])
	rows = Friend.objects.all().values_list(
			'from_user', 'to_user','friend',
			'created_date',
			 
		 
			 
			 	
			 
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
	
	#Member Objects	
	writer.writerow([])
	writer.writerow([
			'CRID',
			'From Member',
			'To Member',
			   
 		   
 		  
			
 		   
			 ])
	rows = Member.objects.all().values_list(
				'CRID', 'from_member','to_member'
			
		 	
		 
		 )
	for row in rows:
		writer.writerow(row)  
	

	#ChatRoom Objects	
	writer.writerow([])
	writer.writerow([
				'CRID',
			'User',
			'Message',
			   'Created Date'
 		   
 		  
			
 		   
			 ])
	rows = ChatRoom.objects.all().values_list(
			'CRID', 'user','message',
			 
			
			'created_date',
			 
		 
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
	
	#Information Objects
	writer.writerow([])
	writer.writerow([
				'From Info',
			'To Info',
			'Message',
 		   
 		  'Created Date',
			 
		 
			
 		   
			 ])
	rows = Information.objects.all().values_list(
				'from_info', 'to_info','message','created_date'
			 
			 	
			 
			
			
		 
		 
		 )
	for row in rows:
		writer.writerow(row)  
	


	return response

def export_xls(request):
	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="ProcoderDataBase.xls"'
	wb = xlwt.Workbook(encoding='utf-8')

	#Rating Objects		
	ws = wb.add_sheet('User')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'User ID', 'User Name',
			 
		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = User.objects.all().values_list(
			'id',
			'username',
			 
			
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)

	#UserProfile		
	ws = wb.add_sheet('User Profile')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'User', 'Status','First name', 
			'Last name', 'Email address','About',
			'Linkedin', 'Github', 'Twitter',
			'Facebook', 'Skill', 'Age',
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = UserProfile.objects.all().values_list(
			'user',
			'status', 
			'first_name',
			'last_name', 
			'email',
			'about', 
			'linkedin',
			'github', 
			'twitter',
			'facebook', 
			'skill',
			'age', 
		 

			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)

	#Skill Objects		
	ws = wb.add_sheet('Skill')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'Skill', 'Skill Icon', 
		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Skill.objects.all().values_list(
			'skill',
			'skill_icon', 
			  	
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)
	
	#Feedback Objects		
	ws = wb.add_sheet('Feedback')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'email', 'feedback','notify' 
		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Feedback.objects.all().values_list(
			'email',
			'feedback',
			'notify', 
			  	
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)
							
	#Rating Objects		
	ws = wb.add_sheet('Rating')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'User', 'Star1','Star2', 
			'Star3', 'Star4','Star5',
		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Rating.objects.all().values_list(
			'user',
			'star1', 
			'star2',
			'star3', 
			'star4',
			'star5', 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)

	#ByRating Objects		
	ws = wb.add_sheet('ByRating')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'User', 'Rating By','Rating Yes/No', 
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = ByRating.objects.all().values_list(
			'user',
			'rating_by', 
			'is_rating',
		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)

	#Key Objects		
	ws = wb.add_sheet('Key')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'User', 'Key', 
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Key.objects.all().values_list(
			'user',
			'key', 
		 
		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
	
	#Workflow Objects		
	ws = wb.add_sheet('Workflow')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'User', 'Workflow', 
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Workflow.objects.all().values_list(
			'user',
			'workflow', 
		 
		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
	
	#Interest Objects		
	ws = wb.add_sheet('Interest')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'User', 'Interest', 
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Interest.objects.all().values_list(
			'user',
			'interest', 
		 
		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
			
	#Award Objects		
	ws = wb.add_sheet('Award')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'User', 'Award', 
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Award.objects.all().values_list(
			'user',
			'award', 
		 
		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
			
	#Course Objects		
	ws = wb.add_sheet('Course')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'User', 'Course', 
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Course.objects.all().values_list(
			'user',
			'slug', 'course_name', 'course_description', 
			'skill',  
		 
		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
			
	#CourseEnroll Objects		
	ws = wb.add_sheet('CourseEnroll')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'User', 'Course', 
			'Enrollment',  
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = CourseEnroll.objects.all().values_list(
			'user',
			'course', 'user_enrollment',
		 
		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
			
	#Topic Objects		
	ws = wb.add_sheet('Topic')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'Topic Name',  
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Topic.objects.all().values_list(
			'topic_name',
			 
		 
		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
			
		
	
	
	#Quiz Objects		
	ws = wb.add_sheet('Quiz')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'User', 'Course','Quiz Name','Quiz Description' 
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Quiz.objects.all().values_list(
			'user','course','quiz_name',
			'quiz_description',
			 
		 
		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
			
		
	#Qna Objects		
	ws = wb.add_sheet('Question and Answer')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'Quiz ID', 'Question','Answer',
			'Option_1','Option_2','Option_3','Option_4', 
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Qna.objects.all().values_list(
			'quiz','question','answer',
			'option_1',	'option_2',
			'option_3',	'option_4',
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
			
	#QuizTaken Objects		
	ws = wb.add_sheet('Quiz Enrolled')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'User ID', 'Quiz','User Enrolled',
			'Quiz Enrolled', 
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = QuizTaken.objects.all().values_list(
			'user','quiz','user_enrollment',
			'quiz_taken',	 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
			
	#UserPerformance Objects		
	ws = wb.add_sheet('User Performance')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'User ID', 'Correct Answer','Wrong Answer',
			'Not Answer','No. of Questions'  
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = UserPerformance.objects.all().values_list(
			'user','correct_answer','wrong_answer',
			'none_answer',	'total_qna' 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
			
		
	#Content Objects		
	ws = wb.add_sheet('Content')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'Course', 'Topic','No. of View' 
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Content.objects.all().values_list(
			'course','topic',
			'view',
			 		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)


	#Category Objects		
	ws = wb.add_sheet('Category')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [

			'Category',   
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Category.objects.all().values_list(
			'category', 
			 
			 		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
	
	#Post Objects		
	ws = wb.add_sheet('Post')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [

			'User ID',
			'Post Title',
			'Category',
			'Post View',   
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Post.objects.all().values_list(
			'user', 'post_title','category','post_view'
			 
			 		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
	
	#Comment Objects		
	ws = wb.add_sheet('Comment')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'Post ID',
			'User ID ',
			'Comment',
			   
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Comment.objects.all().values_list(
			'post', 'user','comment', 
			 
			 		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
	
	#Like Objects		
	ws = wb.add_sheet('Like')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'Post ID',
			'User ID ',
			'Comment',
			   
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Like.objects.all().values_list(
			'post', 'user',
			 
			 		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
						

	#Friend Objects		
	ws = wb.add_sheet('Friend')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'From User',
			'To User',
			'Friend',
			   
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Friend.objects.all().values_list(
			'from_user', 'to_user','friend'
			 
			 		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
						

	#Member Objects		
	ws = wb.add_sheet('Member')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'CRID',
			'From Member',
			'To Member',
			   
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Member.objects.all().values_list(
			'CRID', 'from_member','to_member'
			 
			 		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
						

	#ChatRoom Objects		
	ws = wb.add_sheet('ChatRoom')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'CRID',
			'User',
			'Message',
			   
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = ChatRoom.objects.all().values_list(
			'CRID', 'user','message'
			 
			 		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
						
	#Information Objects		
	ws = wb.add_sheet('Information')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = [
			'From Info',
			'To Info',
			'Message',
			   
 		   
			 ]
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	font_style = xlwt.XFStyle()
	rows = Information.objects.all().values_list(
			'from_info', 'to_info','message'
			 
			 		 
			)
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)		
						

				
								
	wb.save(response)
	return response

def example(request):
	return render(request, 'tutorial/example.html')


































@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def skill(request):
	skills = Skill.objects.all().order_by('-id')
	form = SkillForm() 
	forms = []
	for skill in skills:
		forms.append(SkillForm(instance=skill))
	ziped_data = zip(skills, forms)
	context = {'skills':skills, 'form':form, 'forms':forms, 'ziped_data':ziped_data, } 
	context = dict(context,**load_data(request))
	return render(request, 'tutorial/skill.html',context)



def lockscreen(request):
	lock = False
	request.session['lock'] = True
	if request.method=='POST':
		username = request.user.username
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		request.session['lock'] = False
		if user :
			userstatus = UserProfile.objects.get(user=user)
			if userstatus.status == 'ADMIN':
				return redirect('tutorial:admin_panel')
			elif userstatus.status == 'USER':
				return redirect('tutorial:userdashboard')
		else:
			messages.error(request,'Password are invalid.')

	user =  UserProfile.objects.get(user=request.user)
	context = {'user':user}
	return render(request, 'tutorial/commons/lockscreen.html', context)



#-------------Login, Register, logout------------------------- 


def userutility(request):
	user 	 = UserProfile.objects.get(user=request.user)
	key 	 = user.key_set.all().order_by('-id')
	workflow = user.workflow_set.all().order_by('-id')
	interest = user.interest_set.all().order_by('-id')
	award 	 = user.award_set.all().order_by('-id')
	 
	context = {
	"user":user, 
	"key":key, 
	"workflow":workflow, 	 
	"interest":interest, 
	"award":award,
 
	}
	return render(request, 'tutorial/userutility.html', context)

def feedback_page(request):
	form = FeedbackForm()
	if request.method=='POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			form.save()
			msg = 'Thank you ! "'+str(form.cleaned_data['email'])+'" for feedback. '
			messages.success(request, msg)	
			print('Thank Your')
			return redirect('index')
		else:
			messages.debug(request, str(form.errors))
			print(str(form.errors))

	context = {'form':form}
	return render(request, 'tutorial/commons/feedbackpage.html', context)

def login_page(request):
	username  = request.POST.get('username')
	password = request.POST.get('password')
	if request.method=='POST':
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			user = UserProfile.objects.get(user=user)
			request.session['status'] = user.status 
			status = user.status
			next_data = request.POST.get('next') 
			if status == 'USER':
				#if 
				return redirect('tutorial:userdashboard')
			elif status == 'BLOCK':
				messages.warning(request, 'Sorry, Your block now due to some resoune  go to feedback. ')
				return redirect('tutorial:login_page')
			elif status == 'ADMIN':
				return redirect('tutorial:admin_panel')	
			elif status == 'DEACTIVE':
				messages.warning(request, 'Your username or password are wrong !!!!!!')
				return redirect('tutorial:login_page')
			else:
				return HttpResponse('not')	
		else:
			messages.warning(request, 'Your username or password are wrong !!!!!!')
			
	return render(request, "tutorial/commons/login_page.html")

 
def register_page(request):
	form = NewUserForm()
	print("Hello")
	if request.method=='POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			user = User.objects.get(username=username)
			user = UserProfile(user=user)
			userprofile = user
			user.save()
			user = Rating(user=user)
			user.save()
			user = UserPerformance(user=userprofile)
			user.save()
			msg = 'Welcome to '+form.cleaned_data['username']
			messages.success(request,msg)
			return redirect('tutorial:login_page')
		else:

			messages.info(request,form.errors)
			print(str(form.errors))

	context = {'form':form}
	return render(request, 'tutorial/commons/register_page.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def logout_page(request):
	logout(request)
	messages.success(request, 'Your Logout Successfully !!!')
	return redirect('tutorial:login_page')


#-------------Admin Dashboard------------------------

 
def load_data(request):
		
	users = UserProfile.objects.all().order_by('-id')[:6] #[::-1] FOR Assending Order
	total_users = UserProfile.objects.all().count()
	total_active_users = UserProfile.objects.all().filter(Q(status='USER')).count()
	total_active_users += UserProfile.objects.all().filter(Q(status='ADMIN')).count()
	total_deactive_users = UserProfile.objects.all().filter(status='DEACTIVE').count()
	
	courseenroll =  CourseEnroll.objects.all().order_by('-id')[:5]


	courses = Course.objects.all().order_by('-id')[:5]
	total_courses = Course.objects.all().count()


	total_course_enrolled = CourseEnroll.objects.all().count()
	total_topic = Topic.objects.all().count()
	
	topics = Topic.objects.all().order_by('-id')[:5]
	contents = Content.objects.all().order_by('-id')[:5]

	total_content = Content.objects.all().count()

	quiztaken = QuizTaken.objects.all().order_by('-id')[:5]
	total_quizs = Quiz.objects.all().count()
	total_quiz_taken = QuizTaken.objects.all().count()
	total_qnas = Qna.objects.all().count()

	total_quizattempted = QuizTaken.objects.filter(quiz_taken=True).count()	

	total_feedback = Feedback.objects.all().count()

	userprofile = UserProfile.objects.get(user=request.user)

	total_skill = Skill.objects.all().count()
	context = {

		'userprofile':			userprofile,
		'topics':				topics,
		'contents':				contents,
		'users':				users,
		'total_users':			total_users,
		'total_active_users':	total_active_users,
		'total_deactive_users':	total_deactive_users,

		'courseenroll':			courseenroll,
		'courses':				courses,
		'total_courses':		total_courses,
		'total_course_enrolled':total_course_enrolled,
		'total_topic':			total_topic,
		'total_content':		total_content,

		'quiztaken':			quiztaken,
		'total_quizs':			total_quizs,
		'total_quiz_taken':		total_quiz_taken,
		'total_qnas':			total_qnas,
		'total_quizattempted':	total_quizattempted,

		'total_feedback':		total_feedback,
		'total_skill':			total_skill,
	}
	return context


@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def email(request):
	users = UserProfile.objects.all()
	user_emails = users.filter(~Q(status="DEACTIVE")) 
	print(user_emails)
	have_email = []
	have_not_email = []

	have_email_time = []
	have_not_email_time = []

	feedback = Feedback.objects.all()
	have_email_feedback = []
	have_not_email_feedback = []
	
	have_email_feedback_time = []
	have_not_email_feedback_time = []

	have_email_zip_data = None
	have_not_email_zip_data = None

	have_email_feedback_zip_data = None
	have_not_email_feedback_zip_data = None

	if request.method == 'POST':
		subject = request.POST.get('subject_data')
		message = request.POST.get('email_data')
		for i in user_emails:
			if i.email == None or i.email == '' :
				print("NOT Email", i.email)
				have_not_email.append(i)
				have_not_email_time.append(datetime.now().strftime("%H:%M:%S, %a, %d-%b-%Y"))
			else:
				have_email.append(i)
				print("HAVE ", i.email)
				try:
					text_content = 'This is an important message.'
					html_content = message
					msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [i.email])
					msg.attach_alternative(html_content, "text/html")
					msg.send()
					have_email_time.append(datetime.now().strftime("%H:%M:%S, %a, %d-%b-%Y"))
					print('SENDED successfully',i.user.username, i.email)
				except Exception as e:
					print(e)
					have_not_email.append(i)
					have_not_email_time.append(datetime.now().strftime("%H:%M:%S, %a, %d-%b-%Y"))
					print('NOT ',i.user.username, i.email)

		have_email_zip_data = zip(have_email,have_email_time )		
		have_not_email_zip_data = zip(have_not_email,have_not_email_time )

		feedbackuser = request.POST.get('feedbackuser')	
		print("_____________________________________________________________",feedbackuser )
		if feedbackuser == "True":
			user_emails = Feedback.objects.all()
			for i in user_emails:
				if i.email == None or i.email == '' :
					print("NOT Email", i.email)
					have_not_email_feedback.append(i)
					have_not_email_feedback_time.append(datetime.now().strftime("%H:%M:%S, %a, %d-%b-%Y"))
				else:
					have_email_feedback.append(i)
					print("HAVE ", i.email)
					try:
						text_content = 'This is an important message.'
						html_content = message
						msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [i.email])
						msg.attach_alternative(html_content, "text/html")
						msg.send()
						have_email_feedback_time.append(datetime.now().strftime("%H:%M:%S, %a, %d-%b-%Y"))
						print('SENDED successfully', i.email)
					except Exception as e:
						print(e)
						have_not_email_feedback.append(i)
						have_not_email_feedback_time.append(datetime.now().strftime("%H:%M:%S, %a, %d-%b-%Y"))
						print('NOT ', i.email)

			have_email_feedback_zip_data = zip(have_email_feedback,have_email_feedback_time )		
			have_not_email_feedback_zip_data = zip(have_not_email_feedback,have_not_email_feedback_time )

	context = {
		'users_all':users,
		'have_email':have_email,
		'have_not_email':have_not_email,
		'total_have_email':len(have_email),
		'total_have_not_email':len(have_not_email),
		'have_email_zip_data':have_email_zip_data,
		'have_not_email_zip_data':have_not_email_zip_data,

		'feedback':feedback,
		'have_email_feedback':have_email_feedback,
		'have_not_email_feedback':have_not_email_feedback,
		'total_have_feedback_email':len(have_email_feedback),
		'total_have_not_feedback_email':len(have_not_email_feedback),
		'have_email_feedback_zip_data':have_email_feedback_zip_data,
		'have_not_email_feedback_zip_data':have_not_email_feedback_zip_data,

	}
	context = dict(context,**load_data(request))
	return render(request, 'tutorial/email.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def analysis(request):
	courses = Course.objects.all().order_by('-id')
	courses_data = []
	courses_label = []
	for i in courses :
		courses_data.append(i.courseenroll_set.all().count())
		courses_label.append(i.course_name)

	quizzes = Quiz.objects.all().order_by('-id')
	quizzes_data = []
	quizzes_label = []
	for i in quizzes :
		quizzes_data.append(i.quiztaken_set.all().count())
		quizzes_label.append(i.quiz_name)	
	

	
	users = UserProfile.objects.all() 
	useradmin_data = [
			users.filter(status="USER").count(), 
			users.filter(status="ADMIN").count(),
			users.filter(status="BLOCK").count(),
			users.filter(status="DEACTIVE").count(),
			 ]
	useractive_data = [users.filter(~Q(status="DEACTIVE")).count(), users.filter(Q(status="DEACTIVE")).count(), ]
		 
	contents_data = []
	contents_label = []	 
	contents = Content.objects.all().order_by('-view')[:10]
	for i in contents:
		contents_data.append(i.view)
		contents_label.append(i)	




	context = {

	'courses_data':courses_data,
	"courses_label":courses_label,
	"courses":courses,
	
	'quizzes_data':quizzes_data,
	'quizzes_label':quizzes_label,
	'quizzes':quizzes,

	'useradmin_data': useradmin_data,
	'useradmin_label':['User', 'Admin', 'Block', 'Deactive'],
	'users':users,

	'useractive_data':useractive_data,

	'contents_data':contents_data,
	'contents_label':contents_label,
	'contents':contents,

	}
	context = dict(context,**load_data(request))
	return render(request, 'tutorial/analysis.html', context)

 

@login_required(login_url='/tutorial/login_page/')
@userlock 
@check_status 
def admin_panel(request):
	context = load_data(request)
	return render(request, 'tutorial/admin_panel.html', context)


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
	return render(request, 'tutorial/user.html',context)


@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def feedback(request):
	users = Feedback.objects.all().order_by('-id')
	form = FeedbackForm() 
	forms = []
	for user in users:
		forms.append(FeedbackForm(instance=user))
	ziped_data = zip(users, forms)
	context = {'users':users, 'form':form, 'forms':forms, 'ziped_data':ziped_data, } 
	context = dict(context,**load_data(request))
	return render(request, 'tutorial/feedback.html',context)







@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def admin_tutorial(request):
	return render(request, 'tutorial/admin_tutorial.html')



@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def quiztaken(request):
	quizs = QuizTaken.objects.all().order_by('-id')
	form = QuizTakenForm() 
	forms = []
	for quiz in quizs:
		forms.append(QuizTakenForm(instance=quiz))
	ziped_data = zip(quizs, forms)
	context = {'quizs':quizs, 'form':form, 'forms':forms, 'ziped_data':ziped_data} 
	context = dict(context,**load_data(request))
	return render(request, 'tutorial/quiztaken.html',context)




@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def quiz(request):
	quizs = Quiz.objects.all().order_by('-id')
	form = QuizForm() 
	forms = []
	for quiz in quizs:
		forms.append(QuizForm(instance=quiz))
	ziped_data = zip(quizs, forms)
	context = {'quizs':quizs, 'form':form, 'forms':forms, 'ziped_data':ziped_data} 
	context = dict(context,**load_data(request))
	return render(request, 'tutorial/quiz.html',context)



@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def qna(request):
	qnas = Qna.objects.all().order_by('-id')
	form = QnaForm() 
	forms = []
	for qna in qnas:
		forms.append(QnaForm(instance=qna))
	ziped_data = zip(qnas, forms)
	context = {'qnas':qnas, 'form':form, 'forms':forms, 'ziped_data':ziped_data} 
	context = dict(context,**load_data(request))
	return render(request, 'tutorial/qna.html',context)


@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def performance(request):
	users = UserPerformance.objects.all().order_by('-id')
	form = UserPerformanceForm() 
	forms = []
	for user in users:
		forms.append(UserPerformanceForm(instance=user))
	ziped_data = zip(users, forms)
	context = {'users':users, 'form':form, 'forms':forms, 'ziped_data':ziped_data}
	context = dict(context,**load_data(request)) 
	return render(request, 'tutorial/performance.html',context)



@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def content(request):
	contents = Content.objects.all().order_by('-id')
	form = ContentForm() 
	forms = []
	for content in contents:
		forms.append(ContentForm(instance=content))
	ziped_data = zip(contents, forms)
	context = {'contents':contents, 'form':form, 'forms':forms, 'ziped_data':ziped_data}
	context = dict(context,**load_data(request)) 
	return render(request, 'tutorial/content.html',context)



@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def topic(request):
	topics = Topic.objects.all().order_by('-id')
	form = TopicForm() 
	forms = []
	for topic in topics:
		forms.append(TopicForm(instance=topic))
	ziped_data = zip(topics, forms)
	context = {'topics':topics, 'form':form, 'forms':forms, 'ziped_data':ziped_data} 
	context = dict(context,**load_data(request))
	return render(request, 'tutorial/topic.html',context)



@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def course(request):
	courses = Course.objects.all().order_by('-id')
	form = CourseForm() 
	forms = []
	for course in courses:
		forms.append(CourseForm(instance=course))
	ziped_data = zip(courses, forms)
	context = {'courses':courses, 'form':form, 'forms':forms, 'ziped_data':ziped_data} 
	context = dict(context,**load_data(request))
	return render(request, 'tutorial/course.html',context)



#-------------User Dashboard------------------------

@login_required(login_url='/tutorial/login_page/')
@userlock
def userprofiledelete(request):
	user = request.user
	userprofile = UserProfile.objects.get(user=user)
	if request.method=='POST':
		try:
			userdeactive = User.objects.get(id=user.id)
			userdeactive.is_active = False
			userdeactive.save()
			print("Your Successfully DELETED!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			messages.success(request, 'Your Account Successfully Deleted :(')
			return redirect('tutorial:register_page')
		except Exception as e:
			print(e)
	context = {'user':userprofile}
	return render(request, 'tutorial/userprofiledelete', context)



@login_required(login_url='/tutorial/login_page/')
@userlock
def userprofileedit(request):
	user = request.user
	user = UserProfile.objects.get(user=user)
	form = UserProfileEditForm(instance=user)
	if request.method=='POST':
		form = UserProfileEditForm(request.POST,request.FILES,  instance=user)
		 
		if form.is_valid():
			form.save()
			msg =  'User '+str(user.user.username)+' updated profile successfully.'
			messages.info(request, msg)
			return redirect('tutorial:userdashboard')
		else:
			for i in form.errors:
				messages.error(request, str(i)+' Form Errors ')
			print(form.errors)
			return redirect('tutorial:userdashboard')

	context = {'form':form} 
	return render(request, 'tutorial/userprofileedit', context)



@login_required(login_url='/tutorial/login_page/')
@userlock
def userprofile(request, id):
	user = UserProfile.objects.get(id=id)
	check = False
	star_print = []
	try:
		rate = Rating.objects.get(user=user)
		byrating = ByRating.objects.get(user=rate,rating_by=UserProfile.objects.get(user=request.user))
		check = True
	except Exception as e:
		check = False
		print(e)

	if check == False:	
		if request.method=='POST':
			print("POST@@@@@@@@@@@@@@@@@@@@@@@@@@")
			star = request.POST.get('star')
			rate = Rating.objects.get(user=user)
			if star=='1':
				rate.star1 += 1  
			elif star=='2':
				rate.star2 += 1  
			elif star=='3':
				rate.star3 += 1  
			elif star=='4':
				rate.star4 += 1
			elif star=='5':
				rate.star5 += 1
			rate.save() 	
			print(rate,"Updated_________________________")
			try:

				byrating = ByRating(user=rate, rating_by=UserProfile.objects.get(user=request.user),is_rating=True)
				byrating.save()
				print(byrating,'Created===============================')
				check = True
			except Exception as e:
				print(e)
				


	if check == True :			
		rate = Rating.objects.get(user=user)
		total_star = (5*rate.star5+4*rate.star4+3*rate.star3+2*rate.star2+1*rate.star1)
		total_count =(rate.star5+rate.star4+rate.star2+rate.star2+rate.star1)
		try:
			star_rating = total_star/total_count
		except:
			star_rating = 0.0
		star_print = []
		for i in range(int(star_rating)):
			star_print.append('STAR')

		if star_rating-int(star_rating)!=0.0:
			star_print.append('HALF_STAR')			

		for i in range(5-int(star_rating)-1):
			star_print.append('NOTSTAR')	

		print(star_rating,'_____________________________________________')		
	print(star_print,'############################################')		
	print(check,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')		
	context = {'user':user, 'check':check, 'star_print':star_print}
	return render(request, 'tutorial/userprofile.html', context)



# @login_required(login_url='/tutorial/login_page/')
# @userlock
# def userprofile(request, id):
# 	user = None
# 	ratedata = None
# 	user = UserProfile.objects.get(id=id)
# 	current_user = UserProfile.objects.get(user=request.user)
# 	star_print = []
# 	check = False
	
# 	if request.method=='POST':
# 		star = request.POST.get('star')
# 		try:
# 			byrating = ByRating.objects.filter(Q(user=user) and Q(rating_by=current_user))
# 			if byrating:
# 				check  = byrating.is_rating
# 		except:
# 			byrating = ByRating()
# 			byrating.user = user
# 			byrating.rating_by = current_user
# 			byrating.is_rating = True
# 			try:
# 				rate = Rating.objects.get(user=user)
# 				if star=='1':
# 					rate.star1 += 1  
# 				elif star=='2':
# 					rate.star2 += 1  
# 				elif star=='3':
# 					rate.star3 += 1  
# 				elif star=='4':
# 					rate.star4 += 1
# 				elif star=='5':
# 					rate.star5 += 1
# 				rate.save() 
# 				print(rate,"Updated_________________________")
# 			except:
# 				rate = Rating()
# 				rate.user=user
# 				if star=='1':
# 					rate.star1 += 1  
# 				elif star=='2':
# 					rate.star2 += 1  
# 				elif star=='3':
# 					rate.star3 += 1  
# 				elif star=='4':
# 					rate.star4 += 1
# 				elif star=='5':
# 					rate.star5 += 1
# 				rate.save() 
# 				print(rate,"Created_________________________")
			 
					
			

# 	try:
# 		rate = Rating.objects.get(user=user)
# 		total_star = (5*rate.star5+4*rate.star4+3*rate.star3+2*rate.star2+1*rate.star1)
# 		total_count =(rate.star5+rate.star4+rate.star2+rate.star2+rate.star1)
# 		star_rating = total_star/total_count
# 		ratedata = rate
# 		star_print = []
# 		for i in range(int(star_rating)):
# 			star_print.append('STAR')

# 		if star_rating-int(star_rating)!=0.0:
# 			star_print.append('HALF_STAR')
		
# 		print(star_print)	

# 	except Exception as e:
# 		print(e)

# 	context = {'user':user, 'ratedata':ratedata,'star_print':star_print,}
# 	return render(request, 'tutorial/userprofile.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def userdashboard(request):
	user = request.user
	user = UserProfile.objects.get(user=user)
	total_user_course = user.courseenroll_set.all().count()
	total_user_quiz   = user.quiztaken_set.count()
	 
	total_user_rank	  = None
	value = 0
	 
	up = UserPerformance.objects.all().order_by('-correct_answer')
	print("hello")
	for i in up:
		value+=1	
		if i.user == user :
			break;
		
		print(value,'!!!!!!!!!!!!!!')

	total_user_rank = str(value)+"/"+str(UserPerformance.objects.all().count())		
	form = UserProfileEditForm(instance=user)
	context = {
	"user":user,
	"total_user_course" : total_user_course,
	"total_user_quiz" : total_user_quiz,
	"total_user_rank" : total_user_rank,
  
	 
	"form":form,
	}
	return render(request, 'tutorial/userdashboard.html', context)



@login_required(login_url='/tutorial/login_page/')
@userlock
def usercourse(request):
	courses = Course.objects.all() 
	user = UserProfile.objects.get(user=request.user)
	courses_list = CourseEnroll.objects.filter(user=user).order_by('-id')

	paginator =  Paginator(courses_list, 6)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		courses = paginator.page(page)
	except(EmptyPage, InvalidPage):
		courses = paginator.page(paginator.num_pages)
	context = {'courses':courses, 'total_course':courses_list.count()}
	return render(request, 'tutorial/usercourse.html', context)



#-------------User Dashboard------------------------

@login_required(login_url='/tutorial/login_page/')
@userlock
def account_settings(request):
	user = UserProfile.objects.get(user=request.user)
	context = {'user':user}
	return render(request, 'tutorial/account_settings.html', context)





@login_required(login_url='/tutorial/login_page/') 
@userlock
def allquiztaken(request):
	quiztakens = QuizTaken.objects.all()
	context = {'quiztakens':quiztakens}
	return render(request, 'tutorial/allquiztaken.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def allperformance(request):
	users = UserPerformance.objects.all()
	context = {'users':users}
	return render(request, 'tutorial/allperformance.html',context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def performanceview(request):	
	user = UserProfile.objects.get(user=request.user)
	user = UserPerformance.objects.get(user=user)
	total_qna  = user.total_qna
	try:
		correct_answer = (user.correct_answer*100)//total_qna 
	except:
		correct_answer = 0
	try:
		wrong_answer =	(user.wrong_answer*100)//total_qna 
	except:
		wrong_answer = 0
	try:
		none_answer =	 (user.none_answer*100)//total_qna 
	except:
		none_answer = 0		

	
	

	context={
		'total_qna':total_qna,
		'user':user,
		"correct_answer"	 : correct_answer,
		"wrong_answer"	 : wrong_answer,
		"none_answer" 	 : none_answer,
	}
	return render(request, 'tutorial/performanceview.html', context)
 

@login_required(login_url='/tutorial/login_page/')
@userlock 
def viewreport(request,id):
	quiz = Quiz.objects.get(id=id)
	qnas = quiz.qna_set.all()
	score_data = request.session['score_data']
	choice_data = request.session['choice_data']
	ziped_data = zip(qnas,score_data, choice_data)
	
	total_qnas =qnas.count()
	total_correct =0
	total_wrong =0
	total_none =0

	for choice in score_data:
		if choice == True:
			total_correct+=1
		elif choice == False:
			total_wrong+=1
		elif choice == None:
			total_none+=1

	if request.method=='POST':	

		user = UserProfile.objects.get(user=request.user)
		if not UserPerformance.objects.filter(Q(user=user)).exists() :
			try:
				userperformance = UserPerformance(
					user = user,
					correct_answer = total_correct,
					wrong_answer = total_wrong ,
					none_answer = total_none,
					total_qna = total_qnas ,
					)
				userperformance.save()
			except:
				pass
		else:
			user_performance = UserPerformance.objects.get(user=user)
			print(UserPerformance.objects.get(user=user),"#######################3")
			user_performance.correct_answer += total_correct
			user_performance.wrong_answer += total_wrong 
			user_performance.none_answer += total_none
			user_performance.total_qna += total_qnas 
			user_performance.save()
			print(UserPerformance.objects.get(user=user),"#######################3")
		return redirect('tutorial:quizaccess',quiz.id)	
		 				
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")	 
	context = {'quiz':quiz, 'qnas':qnas, 'ziped_data':ziped_data, }
	return render(request, "tutorial/quizresult.html", context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def quizattemp(request,id):
	quiz = Quiz.objects.get(id=id)
	qnas = quiz.qna_set.all()
	user = UserProfile.objects.get(user=request.user)
	quizenroll = QuizTaken.objects.get(Q(user=UserProfile.objects.get(id=user.id)) & Q(quiz=quiz))
 
	if not quizenroll: 
		return redirect('allquiz')

	if quizenroll.quiz_taken == False:	
			quizenroll.quiz_taken = True
			quizenroll.save() 
			messages.info(request,'Best of luck :)')
	if request.method=='POST':
		c=1
		score_data= []
		choice_data = []
		for qna in qnas:
			s = "group_"+str(c)
			data = request.POST.get(s,"")
			if qna.answer == data:
				score_data.append(True)
				choice_data.append(data)

			elif data =="":
				score_data.append(None)
				choice_data.append(None)

			else:
				score_data.append(False)
				choice_data.append(data)

			c=c+1


		request.session['score_data']=score_data
		request.session['choice_data']=choice_data
		user = UserProfile.objects.get(user=request.user)	
		return redirect('tutorial:viewreport',id=id)

	
	context = {'quiz':quiz, 'qnas':qnas}
	return render(request, 'tutorial/quizattemp.html', context)



@login_required(login_url='/tutorial/login_page/')
@userlock
def quizaccess(request,id):
	quiz = Quiz.objects.get(id=id) 
	user = UserProfile.objects.get(user=request.user)
	quiz_enrolled	= QuizTaken.objects.all()
	quizenroll = None
	quiztaken =None
	quizenroll = quiz_enrolled.filter(Q(user=UserProfile.objects.get(id=user.id)) & Q(quiz=quiz))
	if request.method=='POST':
		if not quizenroll and request.POST.get('QUIZ')=="enrollme":
			enrolled = QuizTaken(user=user, quiz=quiz, user_enrollment=True, quiz_taken=False)
			enrolled.save()
			quizenroll = True
			msg = 'Welcome "'+str(user.user.username)+'" to "'+str(quiz.quiz_name)+'" quiz.'
			messages.success(request,msg)
			print("Not enrolled !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		else:
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ALready enrolled")
	try:
		data = quiz_enrolled.get(Q(user=UserProfile.objects.get(id=user.id)) & Q(quiz=quiz))
		quiztaken = data.quiz_taken
		quizenroll  = data.quizenroll
	except Exception as e:
		pass
		track = traceback.format_exc()
		print(track)
			
	context = {'quiz':quiz,'quizenroll':quizenroll, 'quiztaken':quiztaken}
	return render(request, 'tutorial/quizaccess.html', context)



def index(request):
	courses = Course.objects.all().order_by('-id')[:6]
	total_course = Course.objects.all().count()
	total_user = UserProfile.objects.all().count()
	total_quiz = Quiz.objects.all().count()
	total_content = Content.objects.all().count()
	
	context = {'courses':courses,
	"total_course" :total_course ,
	"total_user"  :total_user,
	"total_quiz" :total_quiz,
	"total_content" :total_content,
		}
	return render(request, 'tutorial/index.html',context)


def error4o4(request):
	return render(request, 'tutorial/base/error4o4.html')

@login_required(login_url='/tutorial/login_page/')
@userlock
def contenthome(request, single_slug):
	try:
		course = Course.objects.get(slug=single_slug)
		user = UserProfile.objects.get(user=request.user)
		user = user.courseenroll_set.all()
	except:
		return redirect('tutorial:error4o4')
	
	
	if user: 
		print(user,"111111111111111111")
		for i in user:
			if i.user_enrollment != True and i.course==course:
				return redirect('tutorial:courseview',single_slug)

	else:
		return redirect('tutorial:allcourse')

	contents_list = course.content_set.all()
	topic_list = contents_list
	paginator =  Paginator(contents_list, 1)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		contents_list = paginator.page(page)
	except(EmptyPage, InvalidPage):
		contents_list = paginator.page(paginator.num_pages)	

	for i in contents_list.object_list:
		i.view +=1
		i.save()
	# 	print(i.view,"--")	
	# print("hello",contents_list.object_list,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	context = {'contents':contents_list, 'course':course, "topic_list" :topic_list, 'page_number':contents_list.number}
	return render(request, 'tutorial/contenthome.html',context)


	# courses_list = Course.objects.all().order_by('-id')
	# paginator =  Paginator(courses_list, 6)

	# try:
	# 	page = int(request.GET.get('page', '1'))
	# except:
	# 	page = 1

	# try:
	# 	courses = paginator.page(page)
	# except(EmptyPage, InvalidPage):
	# 	courses = paginator.page(paginator.num_pages)


	# context = {'courses':courses,'total_course':courses_list.count()} 


	# content =[c.content_slug for c in Course.objects.all()]
	# if single_slug in content:
	# 	matching_series = Content.objects.filter(course_topic__content_slug=single_slug)
	# 	series_urls = {}
	# 	for m in matching_series.all():
	# 		part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
	# 		series_urls[m] = part_one.tutorial_slug

	# 	return render(request=request,
	# 		template_name='main/category.html',
	# 		context={"tutorial_series": matching_series, "part_ones": series_urls})


	# print(contents)
	# context = {'contents':contents,'course':course}
	# return render(request, 'tutorial/contenthome.html',context)


# def single_slug(request, single_slug):
#     # first check to see if the url is in categories.

#     categories = [c.category_slug for c in TutorialCategory.objects.all()]
#     if single_slug in categories:
#         matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
#         series_urls = {}

#         for m in matching_series.all():
#             part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
#             series_urls[m] = part_one.tutorial_slug

#         return render(request=request,
#                       template_name='main/category.html',
#                       context={"tutorial_series": matching_series, "part_ones": series_urls})



def pageview(request):
	if request.method=='GET':
		cid  = request.GET.get('cid')
		contents = course.content_set.get(id=cid) 
		print(cid,content,'!!!!!!!!!!!!!!!!!!!')
	else:
		print('NOt fount###########################')

	return HttpResponse()

#<---------------All-------------------------------------

@login_required(login_url='/tutorial/login_page/')
@userlock
def alluser(request):
	users = UserProfile.objects.all()
	context = {'users':users} 
	return render(request, 'tutorial/alluser.html',context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def alltopic(request):
	topics = Topic.objects.all()
	context = {'topics':topics} 
	return render(request, 'tutorial/alltopic.html',context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def allcourse(request):
	courses_list = Course.objects.all().order_by('-id')
	paginator =  Paginator(courses_list, 6)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		courses = paginator.page(page)
	except(EmptyPage, InvalidPage):
		courses = paginator.page(paginator.num_pages)


	context = {'courses':courses,'total_course':courses_list.count()} 
	return render(request, 'tutorial/allcourse.html',context)


	# paginator = Paginator(courses_list, 3) # Show 3 articles per page
	# page = request.GET.get('page')
	# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1", page)
	# try:
	# 	courses = paginator.page(page)
	# except PageNotAnInteger:
	# 	# If page is not an integer, deliver first page.
	# 	courses = paginator.page(1)
	# except EmptyPage:
	# 	# If page is out of range (e.g. 9999), deliver last page of results.
	# 	courses = paginator.page(paginator.num_pages)



@login_required(login_url='/tutorial/login_page/')
@userlock
def allcontent(request):
	contents = Content.objects.all()
	context = {'contents':contents} 
	return render(request, 'tutorial/allcontent.html',context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def allquiz(request):
	courses_list = Quiz.objects.all().order_by('-id')
	paginator =  Paginator(courses_list, 6)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1
	try:
		courses = paginator.page(page)
	except(EmptyPage, InvalidPage):
		courses = paginator.page(paginator.num_pages)

	context = {'courses':courses,'total_quiz':courses_list.count()} 
	return render(request, 'tutorial/allquiz.html',context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def allqna(request):
	qnas = Qna.objects.all()
	context = {'qnas':qnas}
	return render(request, 'tutorial/allqna.html',context)	


#<---------------Create -----------------------------


@login_required(login_url='/tutorial/login_page/')
@userlock
def keycreate(request):
	 
	if request.method=='POST':
		key = request.POST.get('key')
		user = UserProfile.objects.get(user=request.user)
		key = Key(user=user, key=key)
		key.save()
		messages.success(request, "New key "+str(key)+"  created successfully.")		 
		return redirect('tutorial:userutility')
	context = {}
	return render(request, 'tutorial/userutility.html',context)

@login_required(login_url='/tutorial/login_page/')
@userlock
def keyedit(request, id):
	if request.method=='POST':
		keyname = request.POST.get('key')
		keydata = Key.objects.get(id=id)
		keydata.key = keyname
		keydata.save()
		messages.success(request, "New key "+str(keyname)+"  updated successfully.")		 
		return redirect('tutorial:userutility')
 
	return render(request, 'tutorial/userutility.html')


@login_required(login_url='/tutorial/login_page/')
@userlock
def keydelete(request, id):
	if request.method=='POST':
		keydata = Key.objects.get(id=id)
		keydata.delete()
		messages.error(request, "Key point "+str(keydata.key)+"  deleted successfully.")		 
		return redirect('tutorial:userutility')
 
	return render(request, 'tutorial/userutility.html')



@login_required(login_url='/tutorial/login_page/')
@userlock
def workflowcreate(request):
	 
	if request.method=='POST':
		workflow = request.POST.get('workflow')
		user = UserProfile.objects.get(user=request.user)
		workflow = Workflow(user=user, workflow=workflow)
		workflow.save()
		messages.success(request, "New workflow "+str(workflow)+"  created successfully.")		 
		return redirect('tutorial:userutility')

	return render(request, 'tutorial/userutility.html')

@login_required(login_url='/tutorial/login_page/')
@userlock
def workflowedit(request, id):
	if request.method=='POST':
		workflowname = request.POST.get('workflow')
		workflowdata = Workflow.objects.get(id=id)
		workflowdata.workflow = workflowname
		workflowdata.save()
		messages.success(request, "New workflow "+str(workflowname)+"  updated successfully.")		 
		return redirect('tutorial:userutility')
 
	return render(request, 'tutorial/userutility.html')


@login_required(login_url='/tutorial/login_page/')
@userlock
def workflowdelete(request, id):
	if request.method=='POST':
		workflowdata = Workflow.objects.get(id=id)
		workflowdata.delete()
		messages.error(request, "Workflow "+str(workflowdata.workflow)+"  deleted successfully.")		 
		return redirect('tutorial:userutility')
 
	return render(request, 'tutorial/userutility.html')

@login_required(login_url='/tutorial/login_page/')
@userlock
def interestcreate(request):
	if request.method=='POST':
		interest = request.POST.get('interest')
		user = UserProfile.objects.get(user=request.user)
		interest = Interest(user=user, interest=interest)
		interest.save()
		messages.success(request, "New interest "+str(interest)+"  created successfully.")		 
		return redirect('tutorial:userutility')

	return render(request, 'tutorial/userutility.html')

@login_required(login_url='/tutorial/login_page/')
@userlock
def interestedit(request, id):
	if request.method=='POST':
		interestname = request.POST.get('interest')
		interestdata = Interest.objects.get(id=id)
		interestdata.interest = interestname
		interestdata.save()
		messages.success(request, "New interest "+str(interestname)+"  updated successfully.")		 
		return redirect('tutorial:userutility')
 
	return render(request, 'tutorial/userutility.html')


@login_required(login_url='/tutorial/login_page/')
@userlock
def interestdelete(request, id):
	if request.method=='POST':
		interestdata = Interest.objects.get(id=id)
		interestdata.delete()
		messages.error(request, "Interest "+str(interestdata.interest)+"  deleted successfully.")		 
		return redirect('tutorial:userutility')
	return render(request, 'tutorial/userutility.html')

@login_required(login_url='/tutorial/login_page/')
@userlock
def awardcreate(request):
	if request.method=='POST':
		award = request.POST.get('award')
		user = UserProfile.objects.get(user=request.user)
		award = Award(user=user, award=award)
		award.save()
		messages.success(request, "New award "+str(award)+"  created successfully.")		 
		return redirect('tutorial:userutility')

	return render(request, 'tutorial/userutility.html')

@login_required(login_url='/tutorial/login_page/')
@userlock
def awardedit(request, id):
	if request.method=='POST':
		awardname = request.POST.get('award')
		awarddata = Award.objects.get(id=id)
		awarddata.award = awardname
		awarddata.save()
		messages.success(request, "New award "+str(awardname)+"  updated successfully.")		 
		return redirect('tutorial:userutility')
 
	return render(request, 'tutorial/userutility.html')


@login_required(login_url='/tutorial/login_page/')
@userlock
def awarddelete(request, id):
	if request.method=='POST':
		awarddata = Award.objects.get(id=id)
		awarddata.delete()
		messages.error(request, "Award "+str(awarddata.award)+"  deleted successfully.")		 
		return redirect('tutorial:userutility')
	return render(request, 'tutorial/userutility.html')







































@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def usercreate(request):
	form = UserProfileForm()
	if request.method=='POST':
		form = UserProfileForm(request.POST,request.FILES )
		if form.is_valid():
			form.save()
			msg = 'New User "'+str(form.cleaned_data['user'])+'" Created Successfully.'
			messages.success(request, msg)
			return redirect('tutorial:user')
		else:
			messages.debug(request, str(form.errors))
			print(str(form.errors))
			return redirect('tutorial:user')

	context = {'form':form}
	return render(request, 'tutorial/user.html',context)


@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def skillcreate(request):
	form = SkillForm()
	if request.method=='POST':
		form = SkillForm(request.POST)
		if form.is_valid():
			form.save()
			msg = 'New Skill "'+str(form.cleaned_data['skill'])+'"  Created Successfully.'
			messages.success(request, msg)
			return redirect('tutorial:skill')
		else:
			messages.debug(request, str(form.errors))
			print(str(form.errors))
			return redirect('tutorial:skill')

	context = {'form':form}
	return render(request, 'tutorial/skill.html',context)






@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def feedbackcreate(request):
	form = FeedbackForm()
	if request.method=='POST':
		form = FeedbackForm(request.POST,request.FILES )
		if form.is_valid():
			form.save()
			msg = 'New feedback "'+str(form.cleaned_data['email'])+'" Created Successfully.'
			messages.success(request, msg)
			return redirect('tutorial:feedback')
		else:
			messages.debug(request, str(form.errors))
			print(str(form.errors))
			return redirect('tutorial:feedback')

	context = {'form':form}
	return render(request, 'tutorial/feedback.html',context)






# @login_required(login_url='/tutorial/login_page/')
# @userlock
# @check_status 
# def feedbackcreate(request):
# 	form = FeedbackForm()
# 	if request.method=='POST':
# 		form = FeedbackForm(request.POST,request.FILES )
# 		if form.is_valid():
# 			form.save()
# 			msg = 'Thank you ! "'+str(form.cleaned_data['email'])+'" for feedback. '
# 			messages.success(request, msg)
			 
# 		else:
# 			messages.debug(request, str(form.errors))
# 			print(str(form.errors))
			 

# 	context = {'form':form}
# 	return render(request, 'tutorial/commons/feedback.html',context)


@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def coursecreate(request):
	form = CourseForm()
	if request.method=='POST':
		form = CourseForm(request.POST ,request.FILES)
		if form.is_valid():
			form.save()
			msg = '"'+str(form.cleaned_data['course_name'])+'" New course created successfully.'
			messages.success(request, msg)
			return redirect('tutorial:course')
		else:
			messages.errors(request, 'Data invalid.')
			return redirect('tutorial:course')

	context = {'form':form}
	return render(request, 'tutorial/course.html',context)



@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def topiccreate(request):
	form = TopicForm()
	if request.method=='POST':
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			msg = '"'+str(form.cleaned_data['topic_name'])+'" Topic created successfully.'
			messages.success(request, msg)
			return redirect('tutorial:topic')
		else:
			messages.error(request, 'Data invalid.')
			return redirect('tutorial:topic')
	context = {'form':form}
	return render(request, 'tutorial/topic.html',context)


@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def contentcreate(request):
	form = ContentForm()
	if request.method=='POST':
		form = ContentForm(request.POST)
		if form.is_valid():
			form.save()
			course_name = form.cleaned_data.get('course')
			msg = '"'+str(course_name)+'" New tutorial created successfully '
			messages.success(request,msg)
			return redirect('tutorial:content') 
		else:
			messages.error(request, "Data invalid.")
			print(form.errors,'!!!!!!!!!!!!!!!!!!!!!!')
			return redirect('tutorial:tutorial:tutorial:content')
	context = {'form':form}
	return render(request, 'tutorial/content.html',context)



@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def quizcreate(request):
	form = QuizForm()
	if request.method=='POST':
		form = QuizForm(request.POST)
		if form.is_valid():
			form.save()
			msg = '"'+str(form.cleaned_data['quiz_name'])+'" Quiz created successfully.'			 
			messages.success(request, msg)			
			return redirect('tutorial:quiz')
		else:
			print(form.errors)
			messages.error(request, 'Data is invalid.')
			return redirect('tutorial:quiz')

	context = {'form':form}
	return render(request, 'tutorial/quiz.html',context)


@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def qnacreate(request):
	form = QnaForm()
	if request.method=='POST':
		form = QnaForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Qna Created success.")
			return redirect('tutorial:qna')
		else:
			messages.error(request, 'Data invalid.')
			return redirect('tutorial:qna')

	context = {'form':form}
	return render(request, 'tutorial/qna.html',context)


@login_required(login_url='/tutorial/login_page/')
@userlock
@check_status 
def quiztakencreate(request):
	form = QuizTakenForm()
	if request.method=='POST':
		form = QuizTakenForm(request.POST)
		if form.is_valid():
			form.save()
			msg = 'New user "'+str(form.cleaned_data['user'])+'" created Successfully.'
			messages.success(request, msg)			
			return redirect('tutorial:quiztaken')
		else:
			messages.info(request, 'Data is invalid.')
			return redirect('tutorial:quiztaken')

	context = {'form':form}
	return render(request, 'tutorial/quiztaken.html',context)


@login_required(login_url='/tutorial/login_page/') 
@userlock
@check_status 
def performancecreate(request):
	form = UserPerformanceForm()
	if request.method=='POST':
		form = UserPerformanceForm(request.POST)
		if form.is_valid():
			form.save()
			msg = 'User "'+str(form.cleaned_data['user'])+'" updated successfully.'
			messages.success(request, msg)
			return redirect('tutorial:performance')
		else:
			messages.error(request, "Data invalid.")
			return redirect('tutorial:performance')

	context = {'form':form}
	return render(request, 'tutorial/performancecreate.html',context)





#<----------View-----------------------------------------------------------

@login_required(login_url='/tutorial/login_page/')
@userlock
def userquiz(request):
	quiz = Quiz.objects.all() 
	user = UserProfile.objects.get(user=request.user)
	quiz_list = QuizTaken.objects.filter(user=user).order_by('-id')

	paginator =  Paginator(quiz_list, 6)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		quizzes = paginator.page(page)
	except(EmptyPage, InvalidPage):
		quizzes = paginator.page(paginator.num_pages)
	context = {'courses':quizzes, 'total_quiz':quiz_list.count()}
	return render(request, 'tutorial/userquiz.html', context)



@login_required(login_url='/tutorial/login_page/')
@userlock
def userview(request,id):
	user = UserProfile.objects.get(id=id)
	context = {'user':user}
	return render(request, 'tutorial/userview.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def courseview(request,id):
	course = Course.objects.get(id=id) 
	user = UserProfile.objects.get(user=request.user)
	course_enrolled	= CourseEnroll.objects.all()
	courseenroll = None
	courseenroll = course_enrolled.filter(Q(user=UserProfile.objects.get(id=user.id)) & Q(course=course))
	if request.method=='POST':
		if not courseenroll:
			enrolled = CourseEnroll(user=user, course=course, user_enrollment=True)
			enrolled.save()
			msg = 'Welcome "'+str(user.user.username)+'" to "'+str(course.course_name)+'" course.'
			messages.success(request,msg)
			print("Not enrolled!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		else:
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ALready enrolled")

	courseenroll = course_enrolled.filter(Q(user=UserProfile.objects.get(id=user.id)) & Q(course=course))	
	context = {'course':course,'courseenroll':courseenroll}
	return render(request, 'tutorial/courseview.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def topicview(request,id):
	topic = Topic.objects.get(id=id)
	context = {'topic':topic}
	return render(request, 'tutorial/topicview.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def contentview(request,id):
	content = Content.objects.get(id=id)
	context = {'content':content}
	return render(request, 'tutorial/contentview.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def quizview(request,id):
	quiz = Quiz.objects.get(id=id)
	context = {'quiz':quiz}
	return render(request, 'tutorial/quizview.html', context)



@login_required(login_url='/tutorial/login_page/')
@userlock
def qnaview(request,id):
	qna = Qna.objects.get(id=id)
	context = {'qna':qna}
	return render(request, 'tutorial/qnaview.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def quiztakenview(request, id):
	quiztaken = QuizTaken.objects.get(id=id)
	context = {'quiztaken':quiztaken}
	return render(request, 'tutorial/quiztakenview.html', context)

# <---------------Delete-------------------

@login_required(login_url='/tutorial/login_page/')
@userlock
def userdelete(request,id):
	user = User.objects.get(id=id)
	if request.method=='POST':
		username = user.username
		user.delete()
		messages.error(request,username+' User deleted successfully.')
		return redirect('tutorial:user')
	else:
		messages.error(request,' Error')
		return redirect('tutorial:user')
	context = {'user':user}
	return render(request, 'tutorial/user.html', context)

@login_required(login_url='/tutorial/login_page/')
@userlock
def skilldelete(request,id):
	skill = Skill.objects.get(id=id)
	if request.method=='POST':
		skillname = skill.skill
		skill.delete()
		messages.error(request,skillname+' Skill deleted successfully.')
		return redirect('tutorial:skill')
	else:
		messages.error(request,' Error')
		return redirect('tutorial:skill')
	context = {'skill':skill}
	return render(request, 'tutorial/skill.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def feedbackdelete(request,id):
	user = Feedback.objects.get(id=id)
	if request.method=='POST':
		username = user.email
		user.delete()
		messages.error(request,username+' feedback deleted successfully.')
		return redirect('tutorial:feedback')
	else:
		messages.error(request,' Error')
		return redirect('tutorial:feedback')
	context = {'user':user}
	return render(request, 'tutorial/feedback.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def coursedelete(request,id):
	course = Course.objects.get(id=id)
	if request.method=='POST':
		course_name = course.course_name
		course.delete()
		msg = '"'+str(course_name)+str('" Course deleted successfully.')
		messages.error(request, msg)
		return redirect('tutorial:course')
	else:
		messages.error(request, "Data invalid.")
		return redirect('tutorial:course')
	context = {'course':course}
	return render(request, 'tutorial/course.html', context)



@login_required(login_url='/tutorial/login_page/')
@userlock
def topicdelete(request,id):
	topic = Topic.objects.get(id=id)
	if request.method=='POST':
		topic_name = topic.topic_name
		topic.delete()
		msg = '"'+str(topic_name)+'" topic deleted successfully.'
		messages.error(request, msg)
		return redirect('tutorial:topic')
	else:
		messages.error(request, 'Data invalid.')
		return redirect('tutorial:topic')

	context = {'topic':topic}
	return render(request, 'tutorial/topic.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def contentdelete(request,id):
	content = Content.objects.get(id=id)
	if request.method=='POST':
		course_name = content.course.course_name	
		content.delete()
		msg = '"'+str(course_name)+'" Tutorial Deleted Successfully.' 
		messages.error(request, msg)
		return redirect('tutorial:content')
	else:
		messages.error(request,  'Data invalid.')
		return redirect('tutorial:content')
	context = {'content':content}
	return render(request, 'tutorial/content.html', context)

 
@login_required(login_url='/tutorial/login_page/')
@userlock
def quizdelete(request,id):
	quiz = Quiz.objects.get(id=id)
	if request.method=='POST':
		quiz_name = quiz.quiz_name
		quiz.delete()
		msg = '"'+str(quiz_name)+'" Quiz deleted success.'
		messages.error(request, msg)
		return redirect('tutorial:quiz')
	else:
		messages.error(request, "Data invalid.")
		return redirect('tutorial:quiz')
	context = {'quiz':quiz}
	return render(request, 'tutorial/quiz.html', context)

 
@login_required(login_url='/tutorial/login_page/')
@userlock
def qnadelete(request,id):
	qna = Qna.objects.get(id=id)
	if request.method=='POST':
		qna.delete()
		messages.error(request,  'Qna deleted success.')
		return redirect('tutorial:qna')
	context = {'qna':qna}
	return render(request, 'tutorial/qna.html', context)

 
@login_required(login_url='/tutorial/login_page/')
@userlock
def quiztakendelete(request,id):
	quiztaken = QuizTaken.objects.get(id=id)
	if request.method=='POST':
		username = quiztaken.user.user.username
		quiztaken.delete()
		msg = 'User "'+username+'" deleted successfully.'
		messages.error(request, msg)
		return redirect('tutorial:quiztaken')
	else:
		messages.error(request, "Data invalid.")
		return redirect('tutorial:quiztaken')
	context = {'quiztaken':quiztaken}
	return render(request, 'tutorial/quiztaken.html', context)

 
@login_required(login_url='/tutorial/login_page/')
@userlock
def performancedelete(request,id):
	userperformance = UserPerformance.objects.get(id=id)
	# print(userperformance)
	# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	if request.method=='POST':
		userperformance.delete()
		messages.error(request,  'User performance deleted success.')
		return redirect('tutorial:performance')
	else:
		messages.error(request,  'Data error.')
		return redirect('tutorial:performance')
	context = {'performance':performance}
	return render(request, 'tutorial/performance.html', context)






#<-------------EDIT--------------------------

@login_required(login_url='/tutorial/login_page/')
@userlock
def useredit(request,id):
	user = UserProfile.objects.get(id=id)
	form = UserProfileForm(instance=user)
	if request.method=='POST':
		form = UserProfileForm(request.POST,request.FILES,  instance=user)
		if form.is_valid():
			email = form.cleaned_data['email']
			form.save()
			user = User.objects.get(username=user.user.username)
			user.email = email
			user.save()
			msg =  'User '+str(form.cleaned_data['user'])+' updated successfully.'
			messages.info(request, msg)
			return redirect('tutorial:user')
		else:
			messages.error(request, form.error+' Form Errors ')
			print(str(form.error))
			return redirect('tutorial:user')

	context = {'form':form}
	return render(request, 'tutorial/user.html', context)


 

@login_required(login_url='/tutorial/login_page/')
@userlock
def skilledit(request,id):
	skill = Skill.objects.get(id=id)
	form = SkillForm(instance=skill)
	if request.method=='POST':
		form = SkillForm(request.POST,instance=skill)
		if form.is_valid():
			form.save()
			msg =  'Skill '+str(form.cleaned_data['skill'])+' updated successfully.'
			messages.info(request, msg)
			return redirect('tutorial:skill')
		else:
			messages.error(request, form.error+' Form Errors ')
			print(str(form.error))
			return redirect('tutorial:skill')

	context = {'form':form}
	return render(request, 'tutorial/skill.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def feedbackedit(request,id):
	user = Feedback.objects.get(id=id)
	form = FeedbackForm(instance=user)
	if request.method=='POST':
		form = FeedbackForm(request.POST,request.FILES,  instance=user)
		if form.is_valid():
			form.save()
			msg =  'Feedback '+str(form.cleaned_data['email'])+' updated successfully.'
			messages.info(request, msg)
			return redirect('tutorial:feedback')
		else:
			messages.error(request, form.error+' Form Errors ')
			print(str(form.error))
			return redirect('tutorial:feedback')

	context = {'form':form}
	return render(request, 'tutorial/feedback.html', context)




# @login_required(login_url='/tutorial/login_page/')
# @userlock
# def feedbackedit(request,id):
# 	user = UserProfile.objects.get(id=id)
# 	form = UserProfileForm(instance=user)
# 	if request.method=='POST':
# 		form = UserProfileForm(request.POST,request.FILES,  instance=user)
# 		if form.is_valid():
# 			form.save()
# 			msg =  'User '+str(form.cleaned_data['user'])+' updated successfully.'
# 			messages.info(request, msg)
# 			return redirect('user')
# 		else:
# 			messages.error(request, form.error+' Form Errors ')
# 			print(str(form.error))
# 			return redirect('user')

# 	context = {'form':form}
# 	return render(request, 'tutorial/user.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def courseedit(request,id):
	course = Course.objects.get(id=id)
	form = CourseForm(instance=course)
	if request.method=='POST':
		form = CourseForm(request.POST, request.FILES, instance=course)
		if form.is_valid():
			form.save()
			msg = '"'+str(form.cleaned_data['course_name'])+'" Course updated successfully.'
			messages.success(request, msg)
			return redirect('tutorial:course')
		else:
			messages.error(request, 'Data is invalid')
			return redirect('tutorial:course')

	context = {'form':form, 'course':course}
	return render(request, 'tutorial/course.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def topicedit(request,id):
	topic = Topic.objects.get(id=id)
	form = TopicForm(instance=topic)
	if request.method=='POST':
		form = TopicForm(request.POST, instance=topic)
		if form.is_valid():
			form.save()
			msg = '"'+str(form.cleaned_data['topic_name'])+'" Topic updated successfully.'
			messages.info(request, msg)
			return redirect('tutorial:topic')
		else:
			messages.error(request, 'Data invalid.')
			return redirect('tutorial:topic')

	context = {'form':form, 'topic':topic,}
	return render(request, 'tutorial/topicedit.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def contentedit(request,id):
	content = Content.objects.get(id=id)
	form = ContentForm(instance=content)
	if request.method=='POST':
		form = ContentForm(request.POST, instance=content)
		if form.is_valid():
			form.save()
			course_name = form.cleaned_data.get('course')
			msg = '"'+str(course_name)+'" tutorial updated successfully '
			messages.success(request,msg)
			return redirect('tutorial:content')
		else:
			messages.info(request, 'Data invalid.')
			return redirect('tutorial:content')

	context = {'form':form,'content':content}
	return render(request, 'tutorial/content.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def quizedit(request,id):
	quiz = Quiz.objects.get(id=id)
	form = QuizForm(instance=quiz)
	if request.method=='POST':
		form = QuizForm(request.POST, instance=quiz)
		if form.is_valid():
			form.save()
			msg = '"'+str(form.cleaned_data['quiz_name'])+'" Quiz updated successfully.'			 
			messages.success(request, msg)	
			return redirect('tutorial:quiz')
		else:
			messages.error(request, 'Data invalid.')
			return redirect('tutorial:quiz')

	context = {'form':form,'quiz':quiz}
	return render(request, 'tutorial/quiz.html', context)



@login_required(login_url='/tutorial/login_page/')
@userlock
def qnaedit(request,id):
	qna = Qna.objects.get(id=id)
	form = QnaForm(instance=qna)
	if request.method=='POST':
		form = QnaForm(request.POST, instance=qna)
		if form.is_valid():
			form.save()			
			messages.success(request, "Qna updated success.")
			return redirect('tutorial:qna')
		else:
			messages.error(request, 'Data is invalid.')

	context = {'form':form,'qna':qna}
	return render(request, 'tutorial/qna.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def quiztakenedit(request,id):
	quiztaken = QuizTaken.objects.get(id=id)
	form = QuizTakenForm(instance=quiztaken)
	if request.method=='POST':
		form = QuizTakenForm(request.POST, instance=quiztaken)
		if form.is_valid():
			form.save()
			msg = 'User "'+str(form.cleaned_data['user'])+'" updated successfully.'
			messages.success(request, msg)
			return redirect('tutorial:quiztaken')
		else:
			messages.info(request, 'Data is invalid.')
			return redirect('tutorial:quiztaken')

	context = {'form':form,'quiztaken':quiztaken}
	return render(request, 'tutorial/quiztaken.html', context)


@login_required(login_url='/tutorial/login_page/')
@userlock
def performanceedit(request,id):
	userperformance = UserPerformance.objects.get(id=id)
	form = UserPerformanceForm(instance=userperformance)
	if request.method=='POST':
		form = UserPerformanceForm(request.POST, instance=userperformance)
		if form.is_valid():
			form.save()
			msg = 'UserPerformance updated success.'
			messages.warning(request, msg)
			return redirect('tutorial:performance')
		else:
			messages.error(request, 'Data are invalid.')
			return redirect('tutorial:performance')

	context = {'form':form,'performance':performance}
	return render(request, 'tutorial/performance.html', context)



 
# @login_required(login_url='/tutorial/login_page/')
# @userlock
# def example(request):
# 	return render(request, 'tutorial/base/example.html')


#---------------------------Edit View-----------------------------------