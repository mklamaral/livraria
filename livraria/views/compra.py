from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from livraria.models import Compra
from livraria.serializers.compra import CompraSerializer, CriarEditarCompraSerializer

from usuario.models import Usuario


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["usuario", "status", "data"]
    ordering_fields = ["usuario", "status", "data"]

    def get_queryset(self):
        usuario = self.request.user

        if (
            usuario.tipo_usuario == Usuario.TipoUsuario.GERENTE
            or usuario.is_superuser
            or usuario.groups.filter(name="Administradores").exists()
        ):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
