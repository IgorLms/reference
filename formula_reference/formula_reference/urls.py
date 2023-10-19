from django.contrib import admin
from django.urls import path, include

from reference import urls
from reference.views import page_not_found


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include(urls))
]

handler404 = page_not_found

admin.site.site_header = 'Панель администрирования'
admin.site.index_title = ''

