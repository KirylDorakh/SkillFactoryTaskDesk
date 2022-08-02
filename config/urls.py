from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # bulletin board
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('posts.urls')),

    # accounts
    path('accounts/', include('django.contrib.auth.urls')),
    # for sign up, need to be directly below built-up auth app
    path('accounts/', include('accounts.urls'))
]
