
from urllib import request
from django.contrib.auth.models import User
from django import forms 
from blog.models import *
from tinymce.widgets import TinyMCE

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget



class PostForm(forms.ModelForm):
	post_title = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter post title...",
				"class":"form-control",
				"type":"text", 
				"id":"inputText2", 
				}
			),
			 
		) 
	 
	post_pic = forms.ImageField(
		required=False,
		widget = forms.FileInput(
		attrs = {
		"class":"custom-file-input",
		"id":"customFile",
		"type": "file"
		},

		)
	)
	# post_content =forms.CharField(
	# 	required=False,
	# 	widget = forms.Textarea(
	# 	attrs= {
	# 	"id":"compose-textarea",
	# 	"class":"form-control",
	# 	"style":"height: 300px",
	# 	"placeholder":"This is the awesome post.",
	# 	}

	# )
	# ) 
	# post_content = forms.CharField(
	# 		required=False,
	# 		widget = forms.Textarea(
	# 			attrs={
	# 			"class":"textarea",
	# 			"style" : "width: 100%; height: 100px; font-size: 14px; line-height: 28px; border: 1px solid #dddddd; padding: 10px;",
	# 			"rows":220,
	# 			"cols":10,
	# 			"placeholder":"This is the awesome post.a",
	# 			}
	# 		)
	# 	) 
	post_content =forms.CharField(
			required=False,
			widget = forms.Textarea(
				attrs= {
				 "id":"compose-textarea",
				 "class":"form-control",
				 "style":"height: 300px",
				 "placeholder":"This is the awesome post.",
				}

			)
		) 
	# post_content =forms.CharField(
	# 		required=False,
	# 		widget=SummernoteInplaceWidget()
	# 	) 
	category = forms.ModelMultipleChoiceField (
		queryset = Category.objects.all(),
		required=False,
		widget = forms.SelectMultiple(
			attrs = {
			"id":"inputState",
			"class":"custom-select",
			} 
			)
		)
	class Meta:
		model = Post
		fields = ['post_title', 'post_pic', 'post_content', 'category']




class CategoryForm(forms.ModelForm):

	category = forms.CharField(
		required=True,
		widget = forms.TextInput(
		attrs={
		"class":"form-control",
		"type":"text", 
		"id":"exampleFormControlTextarea1", 
		"placeholder":"Enter Category",
		}
		),

	) 

	class Meta:
		model = Category
		fields = '__all__'



class CommentForm(forms.ModelForm):
	post = forms.ModelChoiceField(
		queryset=Post.objects.all(),
		required=True,
		widget = forms.Select(
			
			attrs = {
			"id":"inputState",
			"class":"custom-select",
			}
			)
		)
	user = forms.ModelChoiceField(
		queryset=UserProfile.objects.all(),
		required=True,
		widget = forms.Select(
			
			attrs = {
			"id":"inputState",
			"class":"custom-select",
			}
			)
		)
	comment =forms.CharField(
		required=False,
		widget = forms.Textarea(
		attrs= {
		 
		"class":"form-control",
		 
		"placeholder":"This is the awesome post.",
		}

	)
	) 
	class Meta:
		model = Comment
		fields = '__all__'



class LikeForm(forms.ModelForm):
	post = forms.CharField(
		required=True,
		widget = forms.TextInput(
		attrs={
		"class":"form-control",
		"type":"text", 
		"id":"exampleFormControlTextarea1", 
		 
		}
		),

	) 	
	user = forms.CharField(
		required=True,
		widget = forms.TextInput(
		attrs={
		"class":"form-control",
		"type":"text", 
		"id":"exampleFormControlTextarea1", 
		 
		}
		),

	) 	
	class Meta:
		model = Like
		fields = '__all__'
