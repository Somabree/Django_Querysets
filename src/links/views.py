from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DestroyView
from django.views.generic.detail import RetrieveView


from src.links.serializers import LinkSerializer
from .models import Link

# Create your views here.
class PostListApi(ListView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(CreateView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDetailApi(RetrieveView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostUpdateApi(UpdateView):
    queryset = Link.object.filter(active=True)
    serializer = LinkSerializer
    
class PostDeleteApi(DestroyView):
    queryset = Link.objects.filter(active=True)
    serializer = LinkSerializer
    
