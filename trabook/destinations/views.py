from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Destination, VacationPlan, Blog
from .serializers import DestinationSerializer, VacationPlanSerializer, BlogSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    @action(detail=False)
    def by_country(self, request):
        country = self.request.query_params.get('country', None)
        destinations = Destination.objects.filter(country=country)
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)

class VacationPlanViewSet(viewsets.ModelViewSet):
    queryset = VacationPlan.objects.all()
    serializer_class = VacationPlanSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

