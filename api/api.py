from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import User, UserComment, Group, GroupComment, UserGroupRelation
from .serializers import UserSerializer, uCommentSerializer, GroupSerializer, gCommentSerializer, ugRelationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ['age', 'description','genre', 'nationality', 'phone', 'email', 'addressCity', 'addressCountry', 'addressPostalcode', 'addressState', 'addressMuni', 'isWorker', 'isDeleted']
    search_fields = ['username', 'description', 'age', 'nationality', 'phone', 'email', 'services']
    ordering_fields = ['age', 'coordinates', 'updatedAt']
    ordering = ['id']
    pagination_class = PageNumberPagination

    # def list(self, request, *args, **kwargs):
    #     response = super(UserViewSet, self).list(request, *args, **kwargs)
    #     # response.data.update({'results': result for result in response.data['results']})
    #     response.data.update({'page_number': request.query_params.get('page', None)})
    #     # print(User.objects.all())
    #     return response

class uCommentViewSet(viewsets.ModelViewSet):
    queryset = UserComment.objects.all()
    serializer_class = uCommentSerializer
    filter_fields = ['userId','createdBy', 'isDeleted']
    ordering = ['id']

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_fields = ['createdBy', 'addressCity', 'addressCountry', 'addressPostalcode', 'addressState', 'addressStreet', 'isDeleted']
    search_fields = ['name', 'description', 'services']
    ordering_fields = ['addressCity', 'addressCountry', 'addressPostalcode', 'addressState', 'addressStreet']
    ordering = ['id']
    pagination_class = PageNumberPagination

    # def list(self, request, *args, **kwargs):
    #     response = super(GroupViewSet, self).list(request, *args, **kwargs)
    #     data = {}
    #     data['results'] = len(response.data)
    #     data['groups'] = response.data
    #     response.data = data
    #     return response

class gCommentViewSet(viewsets.ModelViewSet):
    queryset = GroupComment.objects.all()
    serializer_class = gCommentSerializer
    filter_fields = ['groupId', 'createdBy', 'isDeleted',]
    ordering = ['id']

class ugRelationViewSet(viewsets.ModelViewSet):
    queryset = UserGroupRelation.objects.all()
    serializer_class = ugRelationSerializer
    filter_fields = ['userId', 'isAdmin', 'groupId']
    ordering = ['id']

    # def list(self, request, *args, **kwargs):
    #     response = super(ugRelationViewSet, self).list(request, *args, **kwargs)
    #     data = {}
    #     data['results'] = len(response.data)
    #     data['users_groups'] = response.data
    #     response.data = data
    #     return response