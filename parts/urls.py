from django.contrib import admin
from django.urls import path, include

from parts.views import PartsViewSet, TopWordsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'topwords', TopWordsViewSet)
router.register(r'parts', PartsViewSet)


urlpatterns = router.urls