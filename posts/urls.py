from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    PostSearchList,
                    UserPostListView,
                    CommentsPostListView,
                    CommentCreateView,
                    CommentDeleteView,
                    CommentResponse,

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
    path('comments/', CommentsPostListView.as_view(), name='comments'),
    path('comment/<int:pk>/new/', CommentCreateView.as_view(), name='comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:pk>/response/', CommentResponse.as_view(), name='comment_response'),

    path('permission_denied/', CustomPermissionDeniedView.as_view(), name='permission_denied')
]
