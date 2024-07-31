from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..models.news_model import New
from ..serializers.news_serializers import NewSerializer
from ..paginators.news_paginator import NewPaginator


class NewListView(ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    pagination_class = NewPaginator


class NewDetailView(RetrieveAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    lookup_field = 'id'