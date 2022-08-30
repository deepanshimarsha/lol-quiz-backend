from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField, ModelSerializer, SerializerMethodField
from .models import Rank
from rest_framework.reverse import reverse

class RankSerializer(HyperlinkedModelSerializer):

  class Meta:
        model = Rank
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-rank-detail",
            }
        }
