import django_filters

from .models import *

class CourseFilter(django_filters.FilterSet):
	class Meta:
		model = Course
		fields = ['user','course_name','skill', 'created_date']
	# @property
 #    def qs(self):
 #        parent = super().qs
 #        author = getattr(self.request, 'user', None)

 #        return parent.filter(is_published=True) \
 #            | parent.filter(author=author)