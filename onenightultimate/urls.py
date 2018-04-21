from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views
import werewolf.views

# Examples:
# url(r'^$', 'onenightultimate.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', werewolf.views.index, name='index'),
    url(r'^waitingforplayers$', werewolf.views.waitingforplayers, name='waitingforplayers'),
    path('admin/', admin.site.urls),
]
