from django.urls import path, include
from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()
router.register(r'terms', viewsets.TermViewset)
router.register(r'acceptances/terms', viewsets.TermAcceptanceViewset)
router.register(r'privacies', viewsets.PrivacyViewset)
router.register(r'acceptances/privacies', viewsets.PrivacyAcceptanceViewset)

urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)
