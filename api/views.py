# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import Student
# from .serializers import StudentSerializer

# class StudentListCreateView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         students = Student.objects.filter(added_by=request.user)
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(added_by=request.user)
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from .models import Student
# from .serializers import StudentSerializer
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(added_by=self.request.user)

# def home(request):
#     return HttpResponse("Welcome to the Student Management System")


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

def home(request):
    return HttpResponse("Welcome to the Student Management System")

