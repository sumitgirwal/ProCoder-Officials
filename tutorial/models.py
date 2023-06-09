from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Feedback(models.Model):
	email   = models.CharField(max_length=200, null=True)
	feedback = models.TextField(null=True,blank=False)
	notify  = models.BooleanField(default=False)
	created_date = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		data = str(self.id)+"-"+str(self.email)
		return data


class Skill(models.Model):
	skill = models.CharField(max_length=200, null=True)
	skill_icon = models.CharField(max_length=100, null=True)
	def __str__(self):
		data = str(self.id)+"-"+str(self.skill)
		return data

class UserProfile(models.Model):
	RATING  = (
			("0","0"),("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),
		)

	STATUS  = (
			("ADMIN","ADMIN"),("USER","USER"),("BLOCK","BLOCK"),("DEACTIVE","DEACTIVE"),
		)
	
	user 	  	 = models.OneToOneField(User, on_delete=models.CASCADE)
	status 		 = models.CharField(max_length=100,default="USER", choices=STATUS)
	first_name	 = models.CharField(max_length=200, null=True, blank=True)
	last_name	 = models.CharField(max_length=200, null=True, blank=True)
	email 	   	 = models.EmailField(null=True, unique=True, blank=True)
	about 		 = models.CharField(max_length=500, null=True, blank=True)
	# workflow     = models.ManyToManyField(Workflow, blank=True, null=True)	
	# interest	 = models.ManyToManyField(Interest, blank=True, null=True)
	# award 		 = models.ManyToManyField(Awards, blank=True, null=True)
	linkedin     = models.URLField(blank=True, null=True)
	github 		 = models.URLField(blank=True, null=True)
	twitter		 = models.URLField(blank=True, null=True)
	facebook 	 = models.URLField(blank=True, null=True) 
	skill        = models.ManyToManyField(Skill, blank=True, null=True)	
	#rating		 = models.CharField(max_length=3,default=0, choices=RATING)
	age			 = models.PositiveIntegerField(default=0)
	pic 	   	 = models.ImageField(default='default_image.jpg', null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True, null=True)
	modify_date  = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		data = str(self.id)+"-"+str(self.user.username)
		return data


class Rating(models.Model):
	user 		= models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	star1 		= models.PositiveIntegerField(default=0)
	star2 		= models.PositiveIntegerField(default=0)
	star3 		= models.PositiveIntegerField(default=0)
	star4 		= models.PositiveIntegerField(default=0)
	star5 		= models.PositiveIntegerField(default=0)
	def __str__(self):
		data = str(self.id)+"-STARBY--"+str(self.user.user.username)
		return data
 

class ByRating(models.Model):
	user      = models.ForeignKey(Rating, on_delete=models.CASCADE)
	rating_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	is_rating = models.BooleanField(default=False)
	def __str__(self):
		data = str(self.id)+"----"+str(self.user.user.user.username)+"----"+str(self.rating_by.user.username)
		return data
 



class Key(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	key = models.CharField(max_length=200, null=True)
	def __str__(self):
		data = str(self.id)+"-"+str(self.key)+"--"+str(self.user.user.username)
		return data
 

class Workflow(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	workflow = models.CharField(max_length=200, null=True)
	def __str__(self):
		data = str(self.id)+"-"+str(self.workflow)+str(self.user.user.username)
		return data

class Interest(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	interest = models.CharField(max_length=200, null=True)
	def __str__(self):
		data = str(self.id)+"-"+str(self.interest)+str(self.user.user.username)
		return data



class Award(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	award = models.CharField(max_length=200, null=True)
	def __str__(self):
		data = str(self.id)+"-"+str(self.award)+str(self.user.user.username)
		return data
 
class Course(models.Model):
	user 				= models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	#cid 				= models.CharField(max_length=20, null=True)
	slug				= models.CharField(max_length=300, null=True, blank=True)
	course_name 		= models.CharField(max_length=200, null=True)
	course_description  = models.TextField(null=True,blank=True)
	skill 				= models.ManyToManyField(Skill, blank=True)
	pic 				= models.ImageField(default='default_image.jpg', null=True, blank=True)	
	created_date 		= models.DateTimeField(auto_now_add=True, null=True)
	modify_date 		= models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		data = str(self.id)+"-"+str(self.course_name)
		return data


 
class CourseEnroll(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	user_enrollment = models.BooleanField(default=False, null=True)
	created_date = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		data = str(self.id)+"-"+str(self.user.user.username)
		return data
 



class Topic(models.Model):
	topic_name = models.CharField(max_length=200, null=True) 

	def __str__(self):
		data = str(self.id)+"-"+str(self.topic_name)
		return data


class Content(models.Model):
	course       = models.ForeignKey(Course, on_delete=models.CASCADE)
	topic 		 = models.ForeignKey(Topic, on_delete=models.CASCADE)
	content_data = models.TextField(null=True, blank=True)
	view		 = models.IntegerField(null=True, default=0)
	created_date = models.DateTimeField(auto_now_add=True, null=True)
	modify_date  = models.DateTimeField(auto_now=True, null=True)
	
	def __str__(self):
		data = str(self.id)+"-"+str(self.topic)+"-"+str(self.course)
		return data
 

class Quiz(models.Model):
	user 			 = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	course 		   	 = models.ForeignKey(Course, on_delete=models.CASCADE)
	quiz_name		 = models.CharField(max_length=200, null=True)
	quiz_description = models.TextField(null=True,blank=True)
	#start_date 		 = models.DateTimeField(auto_now=True,null=True, blank=True)
	created_date	 = models.DateTimeField(auto_now_add=True, null=True)
	modify_date 	 = models.DateTimeField(auto_now=True, null=True)
	def __str__(self):
		data = str(self.id)+"-"+str(self.quiz_name)
		return data
	

class Qna(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	question =  models.TextField(null=True)
	answer	 = 	models.CharField(max_length=500, null=True)
	option_1 =	models.CharField(max_length=500, null=True)
	option_2 =	models.CharField(max_length=500, null=True)
	option_3 =	models.CharField(max_length=500, null=True)
	option_4 =	models.CharField(max_length=500, null=True)
	def __str__(self):
		data = str(self.id)+"-"+str(self.quiz.quiz_name)
		return data



class QuizTaken(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	user_enrollment = models.BooleanField(default=False)
	quiz_taken = models.BooleanField(default=False)

	def __str__(self):
		data = str(self.id)+"-"+str(self.user.user.username)
		return data





class UserPerformance(models.Model):
	user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
	#quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
	correct_answer = models.IntegerField(null=True, default=0)
	wrong_answer = models.IntegerField(null=True, default=0)
	none_answer = models.IntegerField(null=True, default=0)
	total_qna = models.IntegerField(null=True,default=0)
	created_date = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		data = str(self.id)+"-"+str(self.user.user.username)
		return data
