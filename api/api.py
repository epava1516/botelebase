from .models import User, UserComment, Group, GroupComment, UserGroupRelation, UserGallery, GroupGallery
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, uCommentSerializer, GroupSerializer, gCommentSerializer, ugRelationSerializer, userGallerySerializer, groupGallerySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class uCommentViewSet(viewsets.ModelViewSet):
    queryset = UserComment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = uCommentSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GroupSerializer

class gCommentViewSet(viewsets.ModelViewSet):
    queryset = GroupComment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = gCommentSerializer

class ugRelationViewSet(viewsets.ModelViewSet):
    queryset = UserGroupRelation.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ugRelationSerializer

class userGalleryViewSet(viewsets.ModelViewSet):
    queryset = UserGallery.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = userGallerySerializer

class groupGalleryViewSet(viewsets.ModelViewSet):
    queryset = GroupGallery.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = groupGallerySerializer
