# uavlists/api/views.py
from rest_framework import viewsets, status
from uav_management.models import UAV
from .serializers import UavListSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.decorators.http import require_POST

class UavListViewSet(viewsets.ModelViewSet):
    queryset = UAV.objects.all()
    serializer_class = UavListSerializer
    
    @action(detail=True, methods=['DELETE'])
    def delete_uav(self, request, pk=None):
        uav = self.get_object()
        uav.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['PUT'])
    def update_uav(self, request, pk=None):
        uav = self.get_object()
        serializer = UavListSerializer(uav, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
