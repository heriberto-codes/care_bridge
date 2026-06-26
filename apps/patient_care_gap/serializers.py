from rest_framework import serializers

from apps.patient_care_gap.models import Patient, CareGap

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'age', 'language']
        
class CareGapSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareGap
        fields = ['id', 'patient', 'care_gap_type', 'priority', 'status', 'notes', 'created_at', 'updated_at']