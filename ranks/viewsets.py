from .models import Rank
from .serializers import RankSerializer

from rest_framework.viewsets import ModelViewSet

from rest_framework.decorators import action

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST
)

class RankViewSet(ModelViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer
    lookup_field = "slug"