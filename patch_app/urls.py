from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.patch_notes, name='patch_notes'),
]