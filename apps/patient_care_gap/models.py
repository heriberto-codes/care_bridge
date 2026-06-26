from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=0)
    language = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class CareGap(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="care_gaps")
    
    class CareGapType(models.TextChoices):
        ANNUAL_WELLNESS_VISIT = "AWV", "Annual Wellness Visit"
        MEDICATION_CHECK = "MC", "Medication Check"
        SCREENING_REMINDER = "SR", "Screening Reminder"
        POST_DISCHARGE_FOLLOW_UP = "PDFU", "Post-Discharge Follow-Up"
        
    care_gap_type = models.CharField(
        max_length=4,
        choices=CareGapType.choices,
        default=CareGapType.ANNUAL_WELLNESS_VISIT
    )
    
    class Priority(models.TextChoices):
        LOW = "L", "Low"
        MEDIUM = "M", "Medium"
        HIGH = "H", "High"
    
    priority = models.CharField(
        max_length=1,
        choices=Priority.choices,
        default=Priority.LOW
    )
    
    class Status(models.TextChoices):
        NOT_STARTED = "NS", "Not Started"
        CONTACTED = "CONT", "Contacted"
        FOLLOW_UP_NEEDED = "FUN", "Follow-up Needed"
        COMPLETED = "COM", "Completed"
    
    status = models.CharField(
        max_length=5,
        choices=Status.choices,
        default=Status.NOT_STARTED
    )
    
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient} - {self.get_care_gap_type_display()}"
    
    
    
    