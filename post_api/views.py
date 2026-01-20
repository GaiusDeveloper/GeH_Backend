from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.views import ConfirmEmailView
from django.shortcuts import redirect
from django.conf import settings

from .models import Product
from .serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    ProductWriteSerializer,
    CustomLoginResponseSerializer
)


# ==================== Custom Login View ====================
class CustomLoginView(LoginView):
    """
    Override dj-rest-auth LoginView to return custom response
    """
    response_serializer = CustomLoginResponseSerializer


# ==================== Product ViewSet ====================
class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet to handle all CRUD operations for Products
    """
    queryset = Product.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['product_category']  # Filter by category
    search_fields = ['title']  # Search by title

    def get_serializer_class(self):
        """
        Return the correct serializer depending on action
        """
        if self.action == 'list':
            return ProductListSerializer
        elif self.action in ('retrieve',):
            return ProductDetailSerializer
        # For create/update
        return ProductWriteSerializer

    def create(self, request, *args, **kwargs):
        """
        Handle product creation, including optional image/video uploads
        """
        # Make a mutable copy of request data
        data = request.data.copy()

        # Attach files if they exist
        if 'image' in request.FILES:
            data['image'] = request.FILES['image']
        if 'video' in request.FILES:
            data['video'] = request.FILES['video']

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        # Return product in list serializer format (for dashboard)
        return Response(ProductListSerializer(product, context={'request': request}).data,
                        status=status.HTTP_201_CREATED)


# ==================== Custom Email Confirmation ====================
class CustomConfirmEmailView(ConfirmEmailView):
    """
    Redirect to frontend after confirming email
    """
    def get(self, *args, **kwargs):
        return redirect(f"{settings.FRONTEND_URL}/email-verified")



# from rest_framework import viewsets,  permissions
# from rest_framework.response import Response
# from rest_framework import status
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Product
# from .serializers import ProductListSerializer, ProductDetailSerializer, ProductWriteSerializer, CustomLoginResponseSerializer
# from .permissions import IsAuthenticatedOrReadOnly
# from dj_rest_auth.registration.views import ConfirmEmailView
# from django.shortcuts import redirect
# from django.conf import settings
# from rest_framework import filters
# from django.core.files.storage import FileSystemStorage
# from dj_rest_auth.views import LoginView



# class CustomLoginView(LoginView):
#     response_serializer = CustomLoginResponseSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all().order_by('-created_at')
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['product_category']  #Filter based on category
#     search_fields = ['title']
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         product =serializer.save()
        
#         return Response(ProductWriteSerializer(product).data, status=status.HTTP_201_CREATED)
    
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return ProductListSerializer
#         if self.action in ['retrieve']:
#             return ProductDetailSerializer
#         # create/update -> write serializer that accepts nested specs
#         return ProductWriteSerializer
    



# class CustomConfirmEmailView(ConfirmEmailView):
#     # Override to customize email confirmation behavior
#     def get(self, *args, **kwargs):
#         return redirect(f'{settings.FRONTEND_URL}/email-verified')