from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cats.models import Breed, Cat
from cats.permissions import IsOwnerOrReadOnly
from cats.serializers import BreedSerializer, CatSerializer


# Create your views here.
class BreedViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

    @action(methods=['get'], url_path='cats', detail=True)
    def cats(self, request, pk: int):
        breed = Breed.objects.filter(id=pk).exists()
        if not breed:
            return Response({"detail": "breed is not existing"}, status=status.HTTP_404_NOT_FOUND)
        cats = Cat.objects.filter(breed=pk).prefetch_related('grades')
        page = self.paginate_queryset(cats)
        cats_serializer = CatSerializer(page, many=True)
        paginated_response = self.paginator.get_paginated_response(cats_serializer.data)
        return Response(paginated_response.data, status=status.HTTP_200_OK)


class CatsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Cat.objects.all().prefetch_related('grades')
    serializer_class = CatSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

    # TODO permisions


