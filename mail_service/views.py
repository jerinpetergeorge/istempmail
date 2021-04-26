from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BlackListDomain
from .serializer import DomainSerializer


class DomainCheckAPI(APIView):
    def get(self, request):
        serializer = DomainSerializer(data=request.query_params)
        serializer.is_valid(True)

        name = serializer.validated_data["name"]
        blocked = BlackListDomain.objects.filter(name__exact=name).exists()
        return Response({"domain": name, "blocked": blocked}, status=status.HTTP_200_OK)
