from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [

    path('', views.index, name='index'),
    path('allpost/', views.allpost, name='allpost'),       
    path('postview/<int:id>', views.postview, name='postview'),
    path('userpost/', views.userpost, name='userpost'),
    
	path('admin_panel/', views.admin_panel, name='admin_panel'),
	path('user/', views.user, name='user'),
	path('usercreate/', views.usercreate, name='usercreate'),
	path('useredit/<int:id>', views.useredit, name='useredit'),
	path('userdelete/<int:id>', views.userdelete, name='userdelete'),


	path('post/', views.post, name='post'),
	path('postcreate/', views.postcreate, name='postcreate'),
	path('postedit/<int:id>', views.postedit, name='postedit'),
	path('postdelete/<int:id>', views.postdelete, name='postdelete'),

	path('category/', views.category, name='category'),
	path('categorycreate/', views.categorycreate, name='categorycreate'),
	path('categoryedit/<int:id>', views.categoryedit, name='categoryedit'),
	path('categorydelete/<int:id>', views.categorydelete, name='categorydelete'),

	path('comment/', views.comment, name='comment'),
	path('commentcreate/', views.commentcreate, name='commentcreate'),
	path('commentedit/<int:id>', views.commentedit, name='commentedit'),
	path('commentdelete/<int:id>', views.commentdelete, name='commentdelete'),
	
	path('analysis/', views.analysis, name='analysis'),
	path('postsearch/', views.postsearch, name='postsearch'),





]
