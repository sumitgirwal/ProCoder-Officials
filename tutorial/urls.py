from django.urls import path
from tutorial import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from tutorial import forms

app_name = 'tutorial'

urlpatterns = [
    path('error4o4/', views.error4o4, name='error4o4'),
    path('xls/', views.export_xls, name='export_xls'),
    path('csv/', views.export_csv, name='export_csv'),
    path('userutility/', views.userutility, name='userutility'),
    path('keycreate/', views.keycreate, name='keycreate'),
    path('keyedit/<int:id>', views.keyedit, name='keyedit'),
    path('keydelete/<int:id>', views.keydelete, name='keydelete'),
    
    path('workflowcreate/', views.workflowcreate, name='workflowcreate'),
    path('workflowedit/<int:id>', views.workflowedit, name='workflowedit'),
    path('workflowdelete/<int:id>', views.workflowdelete, name='workflowdelete'),
    
    path('interestcreate/', views.interestcreate, name='interestcreate'),
    path('interestedit/<int:id>', views.interestedit, name='interestedit'),
    path('interestdelete/<int:id>', views.interestdelete, name='interestdelete'),
    
    path('awardcreate/', views.awardcreate, name='awardcreate'),
    path('awardedit/<int:id>', views.awardedit, name='awardedit'),
    path('awarddelete/<int:id>', views.awarddelete, name='awarddelete'),
    
    path('skill/', views.skill, name='skill'),
    path('skillcreate/', views.skillcreate, name='skillcreate'),
    path('skilledit/<int:id>', views.skilledit, name='skilledit'),
    path('skilldelete/<int:id>', views.skilldelete, name='skilldelete'),
    


    path('lockscreen/', views.lockscreen, name='lockscreen'),
    path('tutorial/pageview',views.pageview, name="pageview"),
    #Both Accessible
    path('login_page/', views.login_page, name='login_page'),
    path('logout_page/', views.logout_page, name='logout_page'),
    path('register_page/', views.register_page, name='register_page'),
    path('account_settings/', views.account_settings, name='account_settings'),

    #New Url
    path('admin_panel/', views.admin_panel, name="admin_panel"),
    path('user/', views.user, name='user'),
    path('performance/', views.performance, name='performance'),
    path('course/', views.course, name='course'),
    path('topic/', views.topic, name='topic'),
    path('content/', views.content, name='content'),
    path('quiz/', views.quiz, name='quiz'),
    path('qna/', views.qna, name='qna'),
    path('quiztaken/', views.quiztaken, name='quiztaken'),

    #User 
    path('quizaccess/<int:id>', views.quizaccess, name='quizaccess'),
    path('usercourse/', views.usercourse, name="usercourse"),
    path('userquiz/', views.userquiz, name="userquiz"),
    path('account_settings/', views.account_settings, name="account_settings"),
    
    
    
	#Main Urls 
    path('', views.index, name='index'),
    
    #Exitra Urls	 
    path('content/<single_slug>', views.contenthome, name='contenthome'),

    #All Operation Urls   
    path('alluser/', views.alluser, name='alluser'),
    path('alltopic/', views.alltopic, name='alltopic'),
    path('allcontent/', views.allcontent, name='allcontent'),
    path('allcourse/', views.allcourse, name='allcourse'),
    path('allquiz/', views.allquiz, name='allquiz'),
    path('allqna/', views.allqna, name='allqna'),
    path('allperformance/', views.allperformance, name='allperformance'),   
    path('allquiztaken/', views.allquiztaken, name='allquiztaken'),

    #Create Operation
    path('usercreate/', views.usercreate, name='usercreate'),
    path('coursecreate/', views.coursecreate, name='coursecreate'),
    path('topiccreate/', views.topiccreate, name='topiccreate'),
    path('contentcreate/', views.contentcreate, name='contentcreate'),
    path('quizcreate/', views.quizcreate, name='quizcreate'),
    path('qnacreate/', views.qnacreate, name='qnacreate'),
    path('quiztakencreate/', views.quiztakencreate, name='quiztakencreate'),
    path('performancecreate/', views.performancecreate, name='performancecreate'),
    path('feedbackcreate/', views.feedbackcreate, name='feedbackcreate'),
 


    #View Operation
    path('userview/<int:id>', views.userview, name='userview'),
    path('courseview/<int:id>', views.courseview, name='courseview'),
    # path('courseview/', views.courseview, name='courseview'),
    
    path('topicview/<int:id>', views.topicview, name='topicview'),
    path('contentview/<int:id>', views.contentview, name='contentview'),
    path('quizview/<int:id>', views.quizview, name='quizview'),
    path('qnaview/<int:id>', views.qnaview, name='qnaview'),
    path('quiztakenview/<int:id>', views.quiztakenview, name='quiztakenview'),   
    path('performanceview/', views.performanceview, name='performanceview'),

    #Edit Operation
    path('useredit/<int:id>', views.useredit, name='useredit'),
    path('courseedit/<int:id>', views.courseedit, name='courseedit'),
    path('topicedit/<int:id>', views.topicedit, name='topicedit'),
    path('contentedit/<int:id>', views.contentedit, name='contentedit'),
    path('quizedit/<int:id>', views.quizedit, name='quizedit'),
    path('qnaedit/<int:id>', views.qnaedit, name='qnaedit'),
    path('quiztakenedit/<int:id>', views.quiztakenedit, name='quiztakenedit'),
    path('performanceedit/<int:id>', views.performanceedit, name='performanceedit'),
    path('feedbackedit/<int:id>', views.feedbackedit, name='feedbackedit'),


    #Delete Operation
	path('userdelete/<int:id>', views.userdelete, name='userdelete'),
	path('coursedelete/<int:id>', views.coursedelete, name='coursedelete'),
	path('topicdelete/<int:id>', views.topicdelete, name='topicdelete'),
	path('contentdelete/<int:id>', views.contentdelete, name='contentdelete'),
    path('quizdelete/<int:id>', views.quizdelete, name='quizdelete'),
    path('qnadelete/<int:id>', views.qnadelete, name='qnadelete'),
    path('quiztakendelete/<int:id>', views.quiztakendelete, name='quiztakendelete'),
    path('performancedelete/<int:id>', views.performancedelete, name='performancedelete'),
    path('feedbackdelete/<int:id>', views.feedbackdelete, name='feedbackdelete'),
        

    #User Quiz Url
    path('quiz/', views.quiz, name='quiz'),
    path('quizattemp/<int:id>', views.quizattemp, name='quizattemp'),
    path('viewreport/<int:id>', views.viewreport, name='viewreport'),
    path('example/', views.example, name='example'),
    path('userdashboard/', views.userdashboard, name="userdashboard"),
    path('userprofile/<int:id>', views.userprofile, name='userprofile'),
    path('userprofiledelete/', views.userprofiledelete,name='userprofiledelete'),
    path('userprofileedit/', views.userprofileedit,name='userprofileedit'),
    
    path('analysis/', views.analysis, name="analysis"),
    path('email/', views.email, name="email"),



    path('reset_password/', forms.ResetPasswordRequestView.as_view(
                # template_name='tutorial/commons/password_reset.html',
                # subject_template_name='tutorial/commons/password_reset_subject.txt',
                #  email_template_name='tutorial/commons/password_reset_email.html',
                 success_url='/tutorial/reset_password_sent',
                    ), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view( template_name='tutorial/commons/password_reset_done.html'), name="password_reset_done"),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='tutorial/commons/password_reset_confirm.html', success_url='/tutorial/password_reset_complete'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='tutorial/commons/password_reset_complete.html'), name="password_reset_complete"),
    
    path('feedback/', views.feedback, name='feedback'),
    path('feedback_page/', views.feedback_page, name='feedback_page'),






 




 



]
