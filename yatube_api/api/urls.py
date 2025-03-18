from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.views import PostViewSet, GroupViewSet, CommentViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path(
        'v1/posts/<int:post_id>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='comments'
    ),
    path(
        'v1/posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='comment_detail'
    )
]
