from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns=[
    path('',views.index, name='index'),
    path('register/',views.register, name='registration'),
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('project_details/(?P<id>\d+)', views.display_project, name='prjctdtls'),
    path('profile/',views.profile, name='profile'),
    path('project/',views.awwards_project,name='newstarproject'),
    path('review/(?P<project_id>\d+)', views.review_awward_project, name='review'), 
    path('search/', views.project_search,name='search'),
    path('api/profileb',views.ProfileList.as_view(),name='profileEndpoint'),
    path('api/projectsb',views.ProjectList.as_view(),name='projectsEndpoint')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)