from rest_framework.serializers import ModelSerializer
from .models import User, UserComment, Group, GroupComment, UserGroupRelation, UserGallery, GroupGallery

class uCommentSerializer(ModelSerializer):
    class Meta:
        model = UserComment
        fields = ['id', 'userId', 'rate', 'description', 'createdBy', 'isDeleted', 'updatedAt', 'createdAt']
        read_only_fields = ['createdAt']

class UserSerializer(ModelSerializer):
    comments = uCommentSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'username', 'tUserID', 'photos', 'description', 'age', 'genre', 'nationality', 'phonePrefix', 'phone', 'showPhone', 'email', 'comments','showEmail', 'dni', 'dniPhoto', 'coordinates', 'addressCity', 'addressCountry', 'addressPostalcode', 'addressState', 'addressMuni', 'addressZone', 'addressStreet', 'services', 'isWorker', 'credits', 'isPremium', 'creditInUse', 'isDeleted', 'updatedAt', 'createdAt']
        read_only_fields = ['createdAt']

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'createdBy', 'addressCity', 'addressCountry', 'addressPostalcode', 'addressState', 'addressStreet', 'services', 'isDeleted', 'updatedAt', 'createdAt']
        read_only_fields = ['createdAt']

class gCommentSerializer(ModelSerializer):
    class Meta:
        model = GroupComment
        fields = ['id', 'groupId', 'rate', 'description', 'createdBy', 'isDeleted', 'updatedAt', 'createdAt']
        read_only_fields = ['createdAt']

class ugRelationSerializer(ModelSerializer):
    class Meta:
        model = UserGroupRelation
        fields = ['id', 'userId', 'isAdmin', 'groupId', 'updatedAt', 'createdAt']
        read_only_fields = ['createdAt']

class userGallerySerializer(ModelSerializer):
    class Meta:
        model = UserGallery
        fields = ['id', 'userId', 'photo', 'checksum']
        # read_only_fields = ['checksum']

class groupGallerySerializer(ModelSerializer):
    class Meta:
        model = GroupGallery
        fields = ['id', 'groupId', 'photo', 'checksum']
        # read_only_fields = ['checksum']
