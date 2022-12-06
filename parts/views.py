from django.shortcuts import render
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from parts.models import Part, TopWord
from parts.serializers import PartsSerializer, TopWordsSerializer
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'parts': reverse('parts-list', request=request, format=format)
    })


class PartsViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartsSerializer
    permission_classes = [permissions.IsAuthenticated]

words_limit_param = openapi.Parameter('n', openapi.IN_QUERY, description="words limit", type=openapi.TYPE_INTEGER, default=5)

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="get top words for describing parts",
    manual_parameters=[words_limit_param]
))
class TopWordsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TopWord.objects.all()
    serializer_class = TopWordsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        n = int(self.request.query_params.get('n', 5))
        return TopWord.objects.all().order_by('-count')[:n]
