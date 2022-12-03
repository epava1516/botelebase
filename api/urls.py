from rest_framework import routers
from .api import UserViewSet, uCommentViewSet, GroupViewSet, gCommentViewSet, ugRelationViewSet, userGalleryViewSet, groupGalleryViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet, 'users')
router.register('ucomments', uCommentViewSet, 'ucomments')
router.register('groups', GroupViewSet, 'groups')
router.register('gcomments', gCommentViewSet, 'gcomments')
router.register('ugrelations', ugRelationViewSet, 'ugrelations')
router.register('ugrelations', ugRelationViewSet, 'ugrelations')
router.register('ugrelations', ugRelationViewSet, 'ugrelations')
router.register('usergallery', userGalleryViewSet, 'usergallery')
router.register('groupgallery', groupGalleryViewSet, 'groupgallery')

urlpatterns = router.urls
