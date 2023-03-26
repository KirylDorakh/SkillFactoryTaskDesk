from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    PostSearchList,
                    UserPostListView,

                    CustomPermissionDeniedView,
                    )

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('search/', PostSearchList.as_view(), name='search'),
    path('user_posts/', UserPostListView.as_view(), name='user_posts'),

    path('permission_denied/', CustomPermissionDeniedView.as_view(), name='permission_denied')
]
