from urllib import request
from django.contrib.auth.models import User
from django import forms 
from tutorial.models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from tinymce.widgets import TinyMCE

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from procoder.settings import DEFAULT_FROM_EMAIL
from django.views.generic import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.query_utils import Q


class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(
    		label=("Email Or Username"), max_length=254,
    		widget=forms.TextInput(attrs={'class': 'form-control',
			'required': 'true',
			'placeholder': 'Email or Username'	
	})

    )


class ResetPasswordRequestView(FormView):
    template_name = "tutorial/commons/password_reset.html"   
    # success_url='/tutorial/reset_password_sent',
    form_class = PasswordResetRequestForm
    @staticmethod
    def validate_email_address(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data= form.cleaned_data["email_or_username"]
        if self.validate_email_address(data) is True:                 
            associated_users= User.objects.filter(Q(email=data)|Q(username=data))
            if associated_users.exists():
                for user in associated_users:
                        c = {
                            'email': user.email,
                            'domain': request.META['HTTP_HOST'],
                            'site_name': '127.0.0.1:8000',
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'user': user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                            }
                        subject_template_name='tutorial/commons/password_reset_subject.txt'                      
                        email_template_name='tutorial/commons/password_reset_email.html'                       
                        subject = loader.render_to_string(subject_template_name, c)
                        subject = ''.join(subject.splitlines())
                        email = loader.render_to_string(email_template_name, c)
                        send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                result = self.form_valid(form)
                messages.success(request, 'An email has been sent to ' + data +". Please check its inbox to continue reseting password.")
                return result
            result = self.form_invalid(form)
            messages.error(request, 'No user is associated with this email address')
            return result
        else:
            associated_users= User.objects.filter(username=data)
            if associated_users.exists():
                for user in associated_users:
                    c = {
                        'email': user.email,
                        'domain': '127.0.0.1:8000',  
                        'site_name': 'Procoder',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                        }
                    subject_template_name='tutorial/commons/password_reset_subject.txt'
                    email_template_name='tutorial/commons/password_reset_email.html'
                    subject = loader.render_to_string(subject_template_name, c)
                    # Email subject *must not* contain newlines
                    subject = ''.join(subject.splitlines())
                    email = loader.render_to_string(email_template_name, c)
                    send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                result = self.form_valid(form)
                messages.success(request, 'Email has been sent to ' + data +"'s email address. Please check its inbox to continue reseting password.")
                return result
            result = self.form_invalid(form)
            messages.error(request, 'This username does not exist in the system.')
            return result
        messages.error(request, 'Invalid Input')
        return self.form_invalid(form)




class NewUserForm(UserCreationForm):
	username = forms.RegexField(
	label=("Login"), max_length=30, regex=r"^[\w.@+-]+$",
	help_text=("Required. 30 characters or fewer. Letters, digits and "
	"@/./+/-/_ only."),
	error_messages={
	'invalid': ("This value may contain only letters, numbers and "
	"@/./+/-/_ characters.")},
	widget=forms.TextInput(attrs={'class': 'form-control',
	'required': 'true',
	  "placeholder":"User Name",
	  	
	})
	)

	password1 = forms.CharField(
	label=("Password"),
	widget=forms.PasswordInput(attrs={'class': 'form-control',
	'required': 'true',
	'placeholder': 'Password'


	})
	)
	password2 = forms.CharField(
	label=("Password confirmation"),
	widget=forms.PasswordInput(attrs={'class': 'form-control',
	'type': 'password',
	'required': 'true',
	'placeholder': 'Confirm password'
	}),
	help_text=("Enter the same password as above, for verification.")
	)

	class Meta:
		model = User
		fields = ["username", "password1", "password2"]

# def __init__(self, *args, **kwargs):
#     super(User, self).__init__(*args, **kwargs)

#     self.fields['username'].widget.attrs['class'] = 'form-control'
#     self.fields['password1'].widget.attrs['class'] = 'form-control'
#     self.fields['password2'].widget.attrs['class'] = 'form-control'

class UserProfileEditForm(forms.ModelForm):
	first_name = forms.CharField(
			required=False,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter your first name",
				"class":"form-control",
				"type":"text", 
				"id":"inputText1", 
				}
			),
			 
		)

	last_name = forms.CharField(
			required=False,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter your last name",
				"class":"form-control",
				"type":"text", 
				"id":"inputText2", 
				}
			),
			 
		)

	email =  forms.EmailField(
			required=False,
			widget = forms.EmailInput(
				attrs={
				"placeholder":"Enter your email id",
				"class":"form-control",
				"type":"text", 
				"id":"inputEmail1", 
				}
			),
			 
		)

	about = forms.CharField(
			required=False,
			widget = forms.Textarea(
				attrs={
				"class":"textarea",
				"style" : "width: 100%; height: 100px; font-size: 14px; line-height: 28px; border: 1px solid #dddddd; padding: 10px;",
				"rows":220,
				"cols":10,
				"placeholder":"About you.",
				 
				}
			)
		) 
	linkedin = forms.URLField(
			required=False,
			widget = forms.URLInput(
				attrs={
				"placeholder":"Enter your linkedin profile link",
				"class":"form-control",
				"type":"url", 
				 
				}
			),
			 
		)
	github = forms.URLField(
			required=False,
			widget = forms.URLInput(
				attrs={
				 "placeholder":"Enter your github profile link",
				"class":"form-control",
				"type":"url", 
				  
				}
			),
			 
		)
	twitter = forms.URLField(
			required=False,
			widget = forms.URLInput(
				attrs={
				 "placeholder":"Enter your twitter profile link",
				"class":"form-control",
				"type":"url", 
				 
				}
			),
			 
		)
	facebook = forms.URLField(
			required=False,
			widget = forms.URLInput(
				attrs={
				 "placeholder":"Enter your facebook profile link",
				"class":"form-control",
				"type":"url", 
				"id":"inputText1", 
				}
			),
			 
		)
	skill = forms.ModelMultipleChoiceField (
		queryset = Skill.objects.all(),
		widget = forms.SelectMultiple(
			attrs = {

			"id":"inputState",
			"class":"custom-select",
			} 
			)
		)
	
	age = forms.IntegerField(
		widget = forms.NumberInput(
			attrs = {
			"class":"form-control",
			"value":"0",
			},
			)
		)
	pic = forms.ImageField(
		required=False,
		widget = forms.FileInput(
			attrs = {
			"class":"custom-file-input",
			"id":"customFile",
			"type": "file"
			},

			)
		)
	
	class Meta:
		model = UserProfile
		fields = ['first_name','last_name','skill', 'age', 'pic', 'facebook', 'twitter', 'github', 'linkedin', 'about','email']




class UserProfileForm(forms.ModelForm):
	RATING  = [
			("0","0"),("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),
		]
	STATUS  = (
			("ADMIN","ADMIN"),("USER","USER"),("BLOCK","BLOCK"),("DEACTIVE","DEACTIVE"),
		)	
	user = forms.ModelChoiceField(
		queryset=User.objects.all(),
		required=True,
		widget = forms.Select(
			
			attrs = {
			"id":"inputState",
			"class":"custom-select",
			}
			)
		)

	rating = forms.CharField(
		 
		required=False,
		widget = forms.Select(
			attrs = {
			 
			"class":"custom-select",
			},
			choices=RATING,
			)
		)
	status = forms.CharField(
		required=False,
		widget = forms.Select(
			attrs = {
			 
			"class":"custom-select",
			},
			choices=STATUS,
			)
		)
	
	first_name = forms.CharField(
			required=False,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter your first name",
				"class":"form-control",
				"type":"text", 
				"id":"inputText1", 
				}
			),
			 
		)

	last_name = forms.CharField(
			required=False,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter your last name",
				"class":"form-control",
				"type":"text", 
				"id":"inputText2", 
				}
			),
			 
		)

	email =  forms.EmailField(
			required=False,
			widget = forms.EmailInput(
				attrs={
				"placeholder":"Enter your email id",
				"class":"form-control",
				"type":"text", 
				"id":"inputEmail1", 
				}
			),
			 
		)

	about = forms.CharField(
			required=False,
			widget = forms.Textarea(
				attrs={
				"class":"textarea",
				"style" : "width: 100%; height: 100px; font-size: 14px; line-height: 28px; border: 1px solid #dddddd; padding: 10px;",
				"rows":220,
				"cols":10,
				 
				}
			)
		) 
	linkedin = forms.URLField(
			required=False,
			widget = forms.URLInput(
				attrs={
				 
				"class":"form-control",
				"type":"url", 
				 
				}
			),
			 
		)
	github = forms.URLField(
			required=False,
			widget = forms.URLInput(
				attrs={
				 
				"class":"form-control",
				"type":"url", 
				  
				}
			),
			 
		)
	twitter = forms.URLField(
			required=False,
			widget = forms.URLInput(
				attrs={
				 
				"class":"form-control",
				"type":"url", 
				 
				}
			),
			 
		)
	facebook = forms.URLField(
			required=False,
			widget = forms.URLInput(
				attrs={
				 
				"class":"form-control",
				"type":"url", 
				"id":"inputText1", 
				}
			),
			 
		)
	skill = forms.ModelMultipleChoiceField (
		queryset = Skill.objects.all(),
		widget = forms.SelectMultiple(
			attrs = {

			"id":"inputState",
			"class":"custom-select",
			} 
			)
		)
	
	age = forms.IntegerField(
		widget = forms.NumberInput(
			attrs = {
			"class":"form-control",
			"value":"0",
			},
			)
		)
	pic = forms.ImageField(
		required=False,
		widget = forms.FileInput(
			attrs = {
			"class":"custom-file-input",
			"id":"customFile",
			"type": "file"
			},

			)
		)
	
	class Meta:
		model = UserProfile
		fields = ['user','first_name','last_name','skill','rating', 
				'age', 'pic', 'facebook', 'twitter', 'github',
				 'linkedin', 'about','email', 'status']







class CourseForm(forms.ModelForm):
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
	
	course_name = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter the course name",
				"class":"form-control",
				"type":"text", 
				"id":"inputText1", 
				}
			),
			 
		)
	slug = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter the slug or url.",
				"class":"form-control",
				"type":"text", 
				"id":"inputText1", 
				}
			),
			 
		)

	course_description = forms.CharField(
			required=False,
			widget = forms.Textarea(
				attrs={
				"class":"textarea",
				"style" : "width: 100%; height: 100px; font-size: 14px; line-height: 28px; border: 1px solid #dddddd; padding: 10px;",
				"rows":220,
				"cols":10,
				"placeholder":"This is the best course to improve your skill.",
				}
			)
		) 
	#SKILL = [(i.id,i.skill)  for i in Skill.objects.all().order_by('-id')]
	# skill = forms.MultipleChoiceField(
	# 	choices= SKILL,
	skill = forms.ModelMultipleChoiceField (
		queryset = Skill.objects.all(),
		required=False,
		widget = forms.SelectMultiple(
			attrs = {
			"id":"inputState",
			"class":"custom-select",
			} 
			)
		)
	

	pic = forms.ImageField(
		required=False,
		widget = forms.FileInput(
			attrs = {
			"class":"custom-file-input",
			"id":"customFile",
			},

			)
		)
		 
	class Meta:
		model = Course
		fields = '__all__'


class TopicForm(forms.ModelForm):
	topic_name = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter the course-topic name",
				"class":"form-control",
				"type":"text", 
				"id":"inputText1", 
				}
			),
			 
		)

	class Meta:
		model = Topic
		fields = '__all__'

class CourseEnrollForm(forms.ModelForm):
	class Meta:
		model = CourseEnroll
		fields = '__all__'



class ContentForm(forms.ModelForm):
	course = forms.ModelChoiceField(
		queryset=Course.objects.all(),
		required=True,
		widget = forms.Select(
			
			attrs = {
			"id":"inputState",
			"class":"form-control",
			}
			)
		)
	topic = forms.ModelChoiceField(
		queryset=Topic.objects.all(),
		required=True,
		widget = forms.Select(
			
			attrs = {
			"id":"inputState",
			"class":"form-control",
			}
			)
		)

	# slug = forms.CharField(
	# 		required=True,
	# 		widget = forms.TextInput(
	# 			attrs={
	# 			"placeholder":"Enter the slug or url.",
	# 			"class":"form-control",
	# 			"type":"text", 
	# 			"id":"inputText1", 
	# 			}
	# 		),
			 
	# 	)
	# view = forms.CharField(
	# 		required=False,
	# 		widget = forms.TextInput(
	# 			attrs={
	# 			"class":"form-control",
	# 			"type":"text", 
	# 			"id":"inputText1", 
	# 			}
	# 		),
			 
	# 	)
	content_data =forms.CharField(
			required=False,
			widget = forms.Textarea(
				attrs= {
				 "id":"compose-textarea",
				 "class":"form-control",
				 "style":"height: 300px",
				}

			)
		) 
	class Meta:
		model = Content
		fields = ['course','topic','content_data']

 
class QuizForm(forms.ModelForm):
	user = forms.ModelChoiceField(
		queryset = UserProfile.objects.all(),
		required = True,
		widget = forms.Select(
			attrs = {
			"id":"inputState",
			"class":"custom-select",
			}
		)
	)
	
	course = forms.ModelChoiceField(
		queryset = Course.objects.all(),
		required = True,
		widget = forms.Select(
			attrs = {
			"id":"inputState",
			"class":"custom-select",
			}
		)
	)
	
	quiz_name = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter the quiz name",
				"class":"form-control",
				"type":"text", 
				"id":"inputText1", 
				}
			),
			 
		)

	quiz_description = forms.CharField(
			required=False,
			widget = forms.Textarea(
				attrs={
				"placeholder":"This is the best course to improve your skill.",
				"class":"textarea",
				"style" : "width: 100%; height: 100px; font-size: 14px; line-height: 28px; border: 1px solid #dddddd; padding: 10px;",
				"rows":220,
				"cols":10,
				}
			)
		) 
	#start_date =  forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M:%S'],widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M:%S',attrs = {}))
	class Meta:
		model = Quiz
		fields = '__all__'



class QnaForm(forms.ModelForm):
	quiz = forms.ModelChoiceField(
		queryset = Quiz.objects.all(),
		required = True,
		widget = forms.Select(
			attrs = {
			"id":"inputState",
			"class":"custom-select",
			}
		)
	) 
	question = forms.CharField(
			label='Question Create',
			required=False,
			widget = forms.Textarea(
				attrs={
				"placeholder":"Enter Your Question Here !",
				"class":"textarea",
				"style" : "width: 100%; height: 100px; font-size: 14px; line-height: 28px; border: 1px solid #dddddd; padding: 10px;",
				"rows":220,
				"cols":10,
				}
			)
		)
	answer = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter answer of question",
				"class":"form-control",
				"type":"text", 
				"id":"inputText1", 
				}
			),
			 
		)
	option_1 = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Option 1",
				"class":"form-control",
				"type":"text", 
				"id":"inputText1", 
				}
			),
			 
		)
	option_2 = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Option 2",
				"class":"form-control",
				"type":"text", 
				"id":"inputText1", 
				}
			),
			 
		)
	option_3 = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Option 3",
				"class":"form-control",
				"type":"text", 
				"id":"inputText1", 
				}
			),
			 
		)
	option_4 = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Option 4",
				"class":"form-control",
				"type":"text", 
				"id":"inputText1", 
				}
			),
			 
		)

	class Meta:
		model = Qna
		fields = '__all__'



class QuizTakenForm(forms.ModelForm):
	user = forms.ModelChoiceField(
		queryset = UserProfile.objects.all(),
		required = True,
		widget = forms.Select(
			
			attrs = {
			"id":"inputState",
			"class":"form-control",
			}
			)
		)
	quiz = forms.ModelChoiceField(
		queryset = Quiz.objects.all(),
		required = True,
		widget = forms.Select(
			
			attrs = {
			"id":"inputState",
			"class":"form-control",
			}
			)
		)


 #  <div class="custom-control custom-switch custom-switch-off-danger custom-switch-on-success">
  #                     <input type="checkbox" class="custom-control-input" id="customSwitch3">
  #                     <label class="custom-control-label" for="customSwitch3">Toggle this custom switch element with custom colors danger/success</label>
  #                   </div>
	user_enrollment = forms.BooleanField(
			required=False,
			widget = forms.CheckboxInput(
				attrs={
			  
			   # "class":"custom-control-input",
			   #  "id":"customCheck1",
			  
				}
			),
			 
		)
	quiz_taken = forms.BooleanField(
			required=False, 
			widget = forms.CheckboxInput(
				attrs={
				  
				  # "class":"custom-control-input",
				  #  "id":"customCheck1",
				 
				 
				}
			),
			 
		)
	
	class Meta:
		model = QuizTaken
		fields = '__all__'



class UserPerformanceForm(forms.ModelForm):
	user = forms.ModelChoiceField(
		queryset = UserProfile.objects.all(),
		required = True,
		widget = forms.Select(
			
			attrs = {
			"id":"inputState",
			"class":"form-control",
			}
			)
		)
	# quiz = forms.ModelChoiceField(
	# 	queryset = Quiz.objects.all(),
	# 	required = True,
	# 	widget = forms.Select(
			
	# 		attrs = {
	# 		"id":"inputState",
	# 		"class":"form-control",
	# 		}
	# 		)
	# 	)
	total_qna = forms.IntegerField(
		widget = forms.NumberInput(
			attrs = {
			"class":"form-control",
			"value":"0",
			},
			)
		)

	correct_answer = forms.IntegerField(
			label='Correct Answer',
			required=False,
			widget = forms.TextInput(
				attrs={
				"class":"knob",
				'data-skin':"tron" ,
				"data-thickness": "0.2",
				"data-width":"150",
				"data-height":"150" ,
				"data-fgColor":"green",
				}
			)
		) 
	wrong_answer = forms.IntegerField(
			label='Wrong Answer',
			required=False,
			widget = forms.TextInput(
				attrs={
				"class":"knob",
				'data-skin':"tron" ,
				"data-thickness": "0.2",
				"data-width":"150",
				"data-height":"150" ,
				"data-fgColor":"red",
				}
			)
		) 
	none_answer = forms.IntegerField(
			label='No Selected Answer',
			required=False,
			widget = forms.TextInput(
				attrs={
				"class":"knob",
				'data-skin':"tron" ,
				"data-thickness": "0.2",
				"data-width":"150",
				"data-height":"150" ,
				"data-fgColor":"#36648b",
				}
			)
		) 

	class Meta:
		model = UserPerformance
		fields = '__all__'





class FeedbackForm(forms.ModelForm):
	email = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter your email",
				"class":"form-control",
				"type":"text", 
				"id":"inputText1", 
				}
			),
			 
		)
	feedback = forms.CharField(
			required=True,
			widget = forms.Textarea(
				attrs={
				"placeholder":"This is awesome website....",				
				"class":"form-control",
				"type":"text", 
				"id":"exampleFormControlTextarea1", 
				 "rows" : "3"
				}
			),
			 
		) 
	 
	notify = forms.BooleanField(
			required=False, 
			widget = forms.CheckboxInput(
				attrs={
				  
				 "type": "checkbox",
				  "id":"exampleCheck1",
				   "class":"form-check-input", 

				 
				}
			),
			 
		)
	class Meta:
		model = Feedback
		fields = '__all__'







class KeyForm(forms.ModelForm):
 	
	user = forms.CharField(
		required=False,
		widget = forms.TextInput(
		attrs={

		"class":"form-control",
		"type":"text", 
		"id":"exampleFormControlTextarea1", 
		"readonly":"",
		}
		),

	) 

	key = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter Your Key Point.",				
				"class":"form-control",
				"type":"text", 
				"id":"exampleFormControlTextarea1", 
				 
				}
			),
			 
		) 
	 
	
	class Meta:
		model = Key
		fields = '__all__'

class WorkflowForm(forms.ModelForm):
	workflow = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter Your Workflow Point.",				
				"class":"form-control",
				"type":"text", 
				"id":"exampleFormControlTextarea1", 
				 
				}
			),
			 
		) 
	 
	
	class Meta:
		model = Workflow
		fields = ['workflow']


class InterestForm(forms.ModelForm):
	interest = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter Your Interest Point.",				
				"class":"form-control",
				"type":"text", 
				"id":"exampleFormControlTextarea1", 
				 
				}
			),
			 
		) 
	 
	
	class Meta:
		model = Interest
		fields = ['interest']


class AwardForm(forms.ModelForm):
	award = forms.CharField(
			required=True,
			widget = forms.TextInput(
				attrs={
				"placeholder":"Enter Your Award.",				
				"class":"form-control",
				"type":"text", 
				"id":"exampleFormControlTextarea1", 
				 
				}
			),
			 
		) 
	 
	
	class Meta:
		model = Award
		fields = ['award']







class SkillForm(forms.ModelForm):

	skill = forms.CharField(
		required=True,
		widget = forms.TextInput(
		attrs={

		"class":"form-control",
		"type":"text", 
		"id":"exampleFormControlTextarea1", 
		"placeholder":"Enter Skill",
		}
		),

	) 

	skill_icon = forms.CharField(
		required=True,
		widget = forms.TextInput(
		attrs={
		"placeholder":"Enter Skill Icon.",				
		"class":"form-control",
		"type":"text", 
		"id":"exampleFormControlTextarea1", 

		}
		),

	) 


	class Meta:
		model = Skill
		fields = '__all__'


