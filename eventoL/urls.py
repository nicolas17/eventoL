import autocomplete_light
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView
from eventoL import settings
from manager import views

autocomplete_light.autodiscover()
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name="home"),
    url(r'^api/', include('manager.api.urls')),
    url(r'^create-event/$', views.create_event, name="create_event"),
    url(r'^event/', include('manager.urls'), name='event'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^grappelli/', include('grappelli.urls'), name='grappelli'),
    url(r'^ckeditor/', include('ckeditor.urls'), name='ckeditor'),
    url(r'^accounts/profile/', TemplateView.as_view(template_name='account/profile.html'), name="user_profile"),
    url(r'^accounts/', include('allauth.urls'))

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
