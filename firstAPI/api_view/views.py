import json
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from .models import Person, Group
from rest_framework.generics import ListAPIView, GenericAPIView, get_object_or_404
from .serializer import PersonSerializer, GroupSerializer
class PersonListView(ListAPIView):
    model = Person
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonView(RetrieveModelMixin, ListModelMixin, DestroyModelMixin, CreateModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, *kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class GroupListView(ListAPIView):
    model = Person
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class GroupView(RetrieveModelMixin, ListModelMixin, DestroyModelMixin, CreateModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, *kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

def api_home(request, *arg, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['nombre'] = request.GET['nombre']
    print(data['nombre'])
    return JsonResponse({
        'message': data['nombre']
    })

def api_home(request, *arg, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['nombre'] = request.GET['nombre']
    print(data['nombre'])
    return JsonResponse({
        'message': data['nombre']
    })
