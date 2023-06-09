from django.contrib import admin
from blog.models import *

from tinymce.widgets import TinyMCE
from django.db import models

from django_summernote.admin import SummernoteModelAdmin
 
	
# class PostAdmin(admin.ModelAdmin):
# 	fieldsets = [
# 	("user", {'fields': ["user"]}),
# 	("Post/Pic", {'fields': ["post_title", "post_pic"]}),
# 	("category", {'fields': ["category"]}),
# 	("Content", {"fields": ["post_content"]})
# 	]
# 	formfield_overrides = {
# 	models.TextField: {'widget': TinyMCE()},
# 	}

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('post_content',)

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Like)