"""technicaltest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path, re_path
from apps.contacts.views import ContactDetail, ContactList
from apps.meetings.views import MeetingDetailView, MeetingCreateView, MeetingsList, MeetingUpdateView, MeetingDeleteView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('drf/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('contacts/<int:id>', ContactDetail.as_view(), name='contact-detail'),
    path('contacts/', ContactList.as_view()),
    path('meetings/<int:id>/', MeetingDetailView.as_view(), name='meeting-detail'),
    path('meetings/<int:pk>/update/', MeetingUpdateView.as_view(), name='meeting-update'),
    path('meetings/<int:pk>/delete/', MeetingDeleteView.as_view(), name='meeting-delete'),
    path('meetings/create/', MeetingCreateView.as_view(), name='meeting-create'),
    re_path('meetings/', MeetingsList.as_view(), name='meeting-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)