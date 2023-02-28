from django.contrib import admin
from django.urls import path, include

# WYSIWYG Editor
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # bulletin board
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('posts.urls')),

    # accounts
    # path('accounts/', include('django.contrib.auth.urls')),
    # for sign up, need to be directly below built-up auth app
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),

    # WYSIWYG Editor
    path('summernote/', include('django_summernote.urls')),
]

# WYSIWYG Editor
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
