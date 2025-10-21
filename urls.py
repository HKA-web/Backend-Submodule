from rest_framework import routers
from sample.views.user import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
