from django.db import models
from tutorial.models import *



class Category(models.Model):
	category     = models.CharField(max_length=500, null=True)
	created_date = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return str(self.category)


class Post(models.Model):
	user     		 = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	post_title		 = models.CharField(max_length=500, null=True)
	post_pic 		 = models.ImageField(default='default_image.jpg',null=True, blank=True)
	post_content	 = models.TextField(null=True, blank=True)
	category         = models.ManyToManyField(Category, blank=True, null=True)
	post_view        = models.IntegerField(null=True, default=0)
	created_date 	 = models.DateTimeField(auto_now_add=True, null=True)
	modify_date      = models.DateTimeField(auto_now=True, null=True)
	def __str__(self):
		return str(self.post_title)+"-----"+str(self.user.user.username)

class Comment(models.Model):
	post        = models.ForeignKey(Post, on_delete=models.CASCADE)
	user         = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	comment      = models.TextField(null=True)
	created_date = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return str(self.comment)+"---"+str(self.user.user.username)

 
class Like(models.Model):
	post         = models.ForeignKey(Post, on_delete=models.CASCADE)
	user         = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	created_date = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return str(self.post)+"---"+str(self.user.user.username)

 







