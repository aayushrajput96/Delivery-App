# # # # """
# # # # URL configuration for delivery_app project.

# # # # The `urlpatterns` list routes URLs to views. For more information please see:
# # # #     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# # # # Examples:
# # # # Function views
# # # #     1. Add an import:  from my_app import views
# # # #     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# # # # Class-based views
# # # #     1. Add an import:  from other_app.views import Home
# # # #     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# # # # Including another URLconf
# # # #     1. Import the include() function: from django.urls import include, path
# # # #     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# # # # """
# # # # # from django.contrib import admin
# # # # # from django.urls import path, include
# # # # # from rest_framework.routers import DefaultRouter
# # # # # from orders.views import OrderViewSet

# # # # # router = DefaultRouter()
# # # # # router.register(r'orders', OrderViewSet)

# # # # # urlpatterns = [
# # # # #     path('admin/', admin.site.urls),
# # # # #     path('api/', include(router.urls)),
# # # # # ]

# # # # # delivery_app/urls.py

# # # # from django.contrib import admin
# # # # from django.urls import path, include
# # # # from django.http import HttpResponse

# # # # # Create a simple view for the root URL
# # # # def home_view(request):
# # # #     return HttpResponse('Welcome to the Delivery App!')

# # # # urlpatterns = [
# # # #     path('admin/', admin.site.urls),
# # # #     path('api/', include('api.urls')),  # your api urls
# # # #     path('', home_view, name='home'),  # root URL handler
# # # # ]
# # # from django.urls import path
# # # from api.views import RegisterUser, LoginUser, LogoutUser

# # # urlpatterns = [
# # #     path('register/', RegisterUser.as_view(), name='register'),
# # #     path('login/', LoginUser.as_view(), name='login'),
# # #     path('logout/', LogoutUser.as_view(), name='logout'),
# # # ]

# # # delivery_app/urls.py
# # from django.contrib import admin
# # from django.urls import path, include

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('api/', include('api.urls')),  # Include the API URLs
# # ]
# from django.contrib import admin
# from django.urls import path, include
# from django.http import HttpResponse
# from api import views

# # Temporary view for the root URL
# def home(request):
#     return HttpResponse("Welcome to the Delivery App!")

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('api.urls')),
#     path('', views.home, name='home'),  # Add this line
# ]
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Temporary API root endpoint
def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Delivery App API!",
        "api_endpoints": {
            "orders": "/api/orders/",
            "users": "/api/users/",
            # Add other API endpoints as needed
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', api_root, name='api-root'),  # Root URL serves API information
]
