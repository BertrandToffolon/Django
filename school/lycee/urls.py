from django.conf.urls import url
from . import views
from .views import StudentCreateView, StudentEditView, Call

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),
  url(r'^student/create/$', StudentCreateView.as_view(), name="create_student"),
  url(r'^call/(?P<cursus_id>[0-9]+)/$', Call.as_view(), name='call'),
  url(r'^call/particular/$', views.particular_call, name='particular_call'),
  url(r'^student/(?P<student_id>[0-9]+)$', views.student_detail, name='student_detail'),
  url(r'^student/edit/(?P<pk>\d+)/$', StudentEditView.as_view(), name='edit_student'),
  url(r'^student/edit/(?P<student_id>\d+)/$', StudentEditView.as_view(), name='edit_student'),
]