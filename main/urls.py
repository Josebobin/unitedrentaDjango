
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'website.views.error_404_view'
