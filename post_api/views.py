
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer, ProductWriteSerializer
from .permissions import IsAuthenticatedOrReadOnly
from dj_rest_auth.registration.views import ConfirmEmailView
from django.shortcuts import redirect
from django.conf import settings
from rest_framework import filters

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['product_category']  #Filter based on category
    search_params = ['name']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        # if serializer.is_valid():
        #     self.perform_create(serializer)
        # else:
        #     print("Product POST error", serializer.errors)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        if self.action in ['retrieve']:
            return ProductDetailSerializer
        # create/update -> write serializer that accepts nested specs
        return ProductWriteSerializer
    



class CustomConfirmEmailView(ConfirmEmailView):
    # Override to customize email confirmation behavior
    def get(self, *args, **kwargs):
        return redirect(f'{settings.FRONTEND_URL}/email-verified')