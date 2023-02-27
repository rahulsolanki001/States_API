from rest_framework import routers
from .api import StateViewSet

router=routers.DefaultRouter()
router.register('api/states',StateViewSet,'states')

urlpatterns=router.urls