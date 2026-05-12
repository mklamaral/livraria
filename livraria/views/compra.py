from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from livraria.models import Compra
from livraria.serializers.compra import CompraSerializer, CriarEditarCompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["usuario", "status", "data"]
    ordering_fields = ["usuario", "status", "data"]
    
    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all()
        if usuario.groups.filter(name="Administradores"):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)