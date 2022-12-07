from rest_framework import routers
from .api import UserViewSet, uCommentViewSet, GroupViewSet, gCommentViewSet, ugRelationViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet, 'users')
router.register('ucomments', uCommentViewSet, 'ucomments')
router.register('groups', GroupViewSet, 'groups')
router.register('gcomments', gCommentViewSet, 'gcomments')
router.register('ugrelations', ugRelationViewSet, 'ugrelations')

urlpatterns = router.urls
