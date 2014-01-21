from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

from projects.views import ProyectoDetailView

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('main.views',
    (r'^$', 'home'),
)

urlpatterns += patterns('users.views',
    (r'^login/$', 'login_user'),
    (r'^logout/$', 'logout_user'),
    (r'^profile/$', 'profile_user'),
    (r'^profile/edit/$', 'edit_user_profile'),
)

urlpatterns += patterns('',
    #(r'^proyectos/(?P<proyecto_id>\d+)/$', 'project_details'),
    url(r'^proyectos/(?P<pk>\d+)/$', ProyectoDetailView.as_view(), name='proyecto-detail'),
)


