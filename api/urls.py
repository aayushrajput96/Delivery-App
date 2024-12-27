# # api/urls.py
# # from django.urls import path
# # from .views import SomeApiView  # Import your view here

# # urlpatterns = [
# #     path('some-endpoint/', SomeApiView.as_view(), name='some-endpoint'),
# #     path('register/', RegisterUser.as_view(), name='register'),
# #     path('login/', LoginUser.as_view(), name='login'),
# #     path('logout/', LogoutUser.as_view(), name='logout'),
# # ]
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import OrderViewSet

# router = DefaultRouter()
# router.register(r'orders', OrderViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]
# urls.py
from django.urls import path
from .views import OrderListCreateView, UpdateOrderStatusView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
   path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
   path('orders/<int:pk>/update-status/', UpdateOrderStatusView.as_view(), name='update-order-status'),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
