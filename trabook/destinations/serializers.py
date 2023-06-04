from rest_framework import serializers
from .models import Destination, VacationPlan, Blog

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class VacationPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationPlan
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'