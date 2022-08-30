from rest_framework.routers import SimpleRouter

from .viewsets import (
    RankViewSet,
)

api_router = SimpleRouter()
api_router.register("rank", RankViewSet, basename="api-rank")

urlpatterns = api_router.urls