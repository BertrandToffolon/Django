from django.conf.urls import url
from . import views
from .views import StudentCreateView

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),
  url(r'^student/create/$', StudentCreateView.as_view(), name="create_student"),
]