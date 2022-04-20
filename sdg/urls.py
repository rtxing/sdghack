"""mapsproblem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from goals import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(r'', views.home),
    path(r'tni/<goal_no>', views.tni),
    path(r'tracking', views.tracking),
    path(r'matrix', views.matrix),
    path(r'knowledgegraph/<goal_no>', views.kg),
    path(r'goalsinter/<goal_no>', views.goalsinter),
    path(r'value/<goal_no>', views.value),
    path(r'partnerships/<goal_no>', views.partnerships),
    path(r'success', views.success),
    #path(r'home', views.home),
    #path(r'tree1/', views.tree1),
    #path(r'accounts/profile/', views.profile),
    #path(r'postproblem/', views.postproblem),
    #path(r'postproblem2/', views.postproblem2),
    #path('admin/', admin.site.urls),
    #path(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),

    #path('__debug__/', include('debug_toolbar.urls')), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
