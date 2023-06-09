from django.db import models
from tutorial.models import *

 

class Friend(models.Model):
	from_user     	 = models.PositiveIntegerField(default=0)
	to_user    	     = models.PositiveIntegerField(default=0)
	friend			 = models.BooleanField(default=False)
	created_date 	 = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		from_user = UserProfile.objects.get(id=self.from_user)
		to_user = UserProfile.objects.get(id=self.to_user)
		return str(self.id)+"-----"+str(from_user)+"-----"+str(to_user)



class Member(models.Model):
	CRID  				 = models.CharField(max_length=200, null=True)
	from_member     	 = models.PositiveIntegerField(default=0)
	to_member    	     = models.PositiveIntegerField(default=0)
	def __str__(self):
		from_user = UserProfile.objects.get(id=self.from_member)
		to_user = UserProfile.objects.get(id=self.to_member)
		return str(self.id)+"-----"+str(self.CRID)+"-----"+str(from_user)+"-----"+str(to_user)

class ChatRoom(models.Model):
	CRID          = models.CharField(max_length=200, null=True)
	user          = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	message       = models.TextField(null=True,blank=False)
	created_date  = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return str(self.id)+"-----"+str(self.CRID)+'----'+str(self.message)




class Information(models.Model):
	from_info     	 = models.PositiveIntegerField(default=0)
	to_info     	 = models.PositiveIntegerField(default=0)
	message			 = models.CharField(max_length=200, null=True)
	created_date 	 = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		from_user = UserProfile.objects.get(id=self.from_info)
		to_user = UserProfile.objects.get(id=self.to_info)
		return str(self.id)+"-----"+str(from_user)+"-----"+str(to_user)





# class SendRequest(models.Model):
# 	user     		 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="sender")
# 	userprofile	     = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="reciever")
# 	friend			 = models.BooleanField(default=False)
# 	created_date 	 = models.DateTimeField(auto_now_add=True, null=True)
# 	def __str__(self):
# 		return str(self.id)+"-----"+str(self.user.user.username)

# class Chat(models.Model):
# 	sendrequest    	 = models.ForeignKey(SendRequest, on_delete=models.CASCADE, related_name="sender")
# 	chat             = models.TextField(null=True,blank=False)
# 	created_date 	 = models.DateTimeField(auto_now_add=True, null=True)
# 	def __str__(self):
# 		return str(self.id)+"-----"+str(self.sendrequest.user.user.username)+'----'+str(self.chat)


# class ChatRoom(models.Model):
# 	user_from = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_from')
# 	user_to   = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_to')
# 	message   = models.TextField(null=True,blank=False)
# 	created_date  = models.DateTimeField(auto_now_add=True, null=True)
# 	def __str__(self):
# 		return str(self.id)+"-----"+str(self.user_from.user.username)+'----'+str(self.user_to.user.username)
