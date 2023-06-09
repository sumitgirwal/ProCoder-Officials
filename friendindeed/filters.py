import django_filters
from django_filters import DateFilter, CharFilter
from django.contrib.auth.models import User
from django import forms
from tutorial.models import * 
from django.db.models import Q

class UserFilter(django_filters.FilterSet):
	full_name = CharFilter(field_name='full_name', method='search_by_full_name',
		widget = forms.TextInput(attrs={
					'class':"form-control", 
					'type':'search',
					'placeholder':'Search',
					
					}))

	def search_by_full_name(self, qs, name, value):
		for term in value.split():
			qs = qs.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))
		return qs
	class Meta:
		model = UserProfile
		fields = ['full_name']
		




