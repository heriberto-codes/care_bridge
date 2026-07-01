from .models import Patient, CareGap
from .serializers import PatientSerializer, CareGapSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def patient_list(request):
    # query the data from DB 
    patients = Patient.objects.all()
    # serialze data 
    serializer = PatientSerializer(patients, many=True)
    # return data
    return Response(serializer.data)

@api_view(['POST'])
def patient_create(request):
    serializer = PatientSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def care_gap_list(request):
    care_gaps = CareGap.objects.all()
    serializer = CareGapSerializer(care_gaps, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def care_gap_create(request):
    serializer = CareGapSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
