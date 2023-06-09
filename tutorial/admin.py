from django.contrib import admin
from tutorial.models import *
from tinymce.widgets import TinyMCE
from django.db import models

class ContentAdmin(admin.ModelAdmin):
	fieldsets = [
		("Course/Topic", {"fields":["course","topic"]}),
		("Content", {"fields":["content_data"]}),
		("View", {"fields":["view"]})
	]


	formfield_overrides = {
			models.TextField: {'widget': TinyMCE()},
	}
	# TinyMCE.init({selector:'.tinyMCE'});

# class TutorialAdmin(admin.ModelAdmin):

#     fieldsets = [
#         ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
#         ("Content", {"fields": ["tutorial_content"]})
#     ]

#     formfield_overrides = {
#         models.TextField: {'widget': TinyMCE()},
#         }


admin.site.register(UserProfile)
admin.site.register(Workflow)
admin.site.register(Interest)
admin.site.register(Award)
admin.site.register(Key)
admin.site.register(Skill)
admin.site.register(Course)
admin.site.register(CourseEnroll)
admin.site.register(Topic)
admin.site.register(Content,ContentAdmin)
admin.site.register(Quiz)
admin.site.register(Qna)
admin.site.register(QuizTaken)
admin.site.register(UserPerformance)
admin.site.register(Feedback)
admin.site.register(Rating)
admin.site.register(ByRating)
