from rest_framework import serializers
from .models import User, UserComment, Group, GroupComment, UserGroupRelation, UserGallery, GroupGallery

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'firstName', 'lastName', 'username', 'galeryPath', 'description', 'age', 'genre', 'nationality', 'phone_prefix', 'phone', 'show_phone', 'email', 'show_email', 'dni', 'dniPhoto', 'addressCity', 'addressCountry', 'addressPostalcode', 'addressState', 'addressZone', 'addressStreet', 'services', 'isWorker', 'isDeleted', 'updatedAt', 'createdAt')
        read_only_fields = ('createdAt',)

class uCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComment
        fields = ('id', 'userId', 'rate', 'description', 'createdBy', 'isDeleted', 'updatedAt', 'createdAt')
        read_only_fields = ('createdAt',)

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'createdBy', 'addressCity', 'addressCountry', 'addressPostalcode', 'addressState', 'addressStreet', 'services', 'isDeleted', 'updatedAt', 'createdAt')
        read_only_fields = ('createdAt',)

class gCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupComment
        fields = ('id', 'groupId', 'rate', 'description', 'createdBy', 'isDeleted', 'updatedAt', 'createdAt')
        read_only_fields = ('createdAt',)

class ugRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroupRelation
        fields = ('id', 'userId', 'isAdmin', 'groupId', 'updatedAt', 'createdAt')
        read_only_fields = ('createdAt',)

class userGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGallery
        fields = ('id', 'userId', 'photo', 'checksum',)
        # read_only_fields = ('checksum',)

class groupGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupGallery
        fields = ('id', 'groupId', 'photo', 'checksum',)
        # read_only_fields = ('checksum',)