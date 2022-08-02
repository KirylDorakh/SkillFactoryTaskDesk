from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # bulletin board
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('posts.urls')),

    # accounts
    path('accounts/', include('django.contrib.auth.urls'))
]
