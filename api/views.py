# from rest_framework import status, permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from rest_framework.authtoken.models import Token
# from orders.models import Order
# class RegisterUser(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         email = request.data.get('email')
#         user = User.objects.create_user(username=username, password=password, email=email)
#         return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

# class LoginUser(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key}, status=status.HTTP_200_OK)
#         return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# class LogoutUser(APIView):
#     def post(self, request):
#         logout(request)
#         return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

# class UpdateOrderStatus(APIView):
#     def put(self, request, pk):
#         order = Order.objects.get(pk=pk)
#         order.status = request.data.get('status')
#         order.save()
#         return Response({"message": "Order status updated successfully"})

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from orders.serializers import OrderSerializer
from django.shortcuts import render

class OrderListCreateView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateOrderStatusView(APIView):
    def put(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        
        order.status = request.data.get('status', order.status)
        order.save()
        return Response({'status': 'Updated successfully'}, status=status.HTTP_200_OK)
    
def home(request):
    return render(request, 'home.html')  # Render a template