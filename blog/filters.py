import django_filters
from django_filters import DateFilter, CharFilter
from blog.models import *
from django import forms 


class PostFilter(django_filters.FilterSet):
	end_date = DateFilter(
				field_name="created_date", 
				lookup_expr='lte',
				widget = forms.TextInput(attrs={
					 
					'class':'form-control',

					})

				)
	start_date = DateFilter(
				field_name="created_date", 
				lookup_expr='gte',
				widget = forms.TextInput(attrs={
					 
					'class':'form-control',

					}))
	
	contain = CharFilter(
				field_name='post_title', 
				lookup_expr='icontains',
				widget = forms.TextInput(attrs={
					 
					'class':'form-control',

					}))
	user = django_filters.ModelChoiceFilter(
				field_name='user',
				queryset=UserProfile.objects.all(),
				widget = forms.Select(attrs={
					'class':'form-control',
					'id':'exampleFormControlSelect1',

					})
				)
	category = django_filters.ModelMultipleChoiceFilter(
				field_name='category',
				queryset=Category.objects.all(),	
				widget = forms.SelectMultiple(
					attrs={
					'class':'form-control',
					'id':'exampleFormControlSelect1',
					'multiple':'',

					})
				)
	post_title = django_filters.CharFilter(
				 
				widget = forms.TextInput(attrs={
					 
					'class':'form-control',

					}))

	class Meta:
		model = Post
		fields = ['user','post_title','category', 'created_date']
		exclude = ['user','post_title','category', 'created_date']





