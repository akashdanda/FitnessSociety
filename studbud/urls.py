"""studbud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from log.views import login_request,register,pagelogout,ResetPassView,setPass
from progress.views import calorieTrackerView, progresshome, workoutprogress,journals,alljournals
from base.views import information,test,home, nav
from graphs.views import workoutview, graphNavPage
from social_media.views import Profileviewupt,Profileview,profile, profile_search_bar, profile_search_results, accept_requests
from django.contrib.auth import views as auth_views
from weight.views import weight, line_graph
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_request,name='login'),
    path('register/',register,name='register'),
    path('logout/',pagelogout, name='logout'),
    path('calorieTracker/',calorieTrackerView,name='cal_tracker'),
    path('progresshome/',progresshome,name='progress_home'),
    path('workoutdaily/',workoutprogress,name='workout'),
    path('DailyJournals/',journals,name='journal'),
    path('alljournals/',alljournals,name='all_journals'),
    path('info/',information,name='info'),
    path('',test,name="home"),
    path('workoutdaily/graphs/',workoutview,name='workOut_graph'),
    path('profileupdate/',Profileviewupt,name='prof_update'),
    path('resetpass/',ResetPassView,name='reset'),
    path('profile_view/',Profileview,name='profile'),
    path('graph_nav/',graphNavPage,name="graph_home"),
    path('userweight/',weight,name="weight"),
    path('userweight/weight_progress/',line_graph,name='weight_graph'),
    path('setpass/',auth_views.PasswordChangeView.as_view(template_name='setpass.html')),
    path('profile/<int:pk>',profile,name='profiles'),
    #path('profiles_list/',Profile_Search_Class.as_view(),name="profile_list"),
    path('profile_search/',profile_search_bar,name='search_profiles'),
    path('profile_results/',profile_search_results,name='results'),
    path('nav/',nav,name='nav'),
    path('friend_requests',accept_requests,name='requests'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

