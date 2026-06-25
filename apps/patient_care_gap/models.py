from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    language = models.CharField(max_length=100)
    
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
        max_length=6,
        choices=Priority.choices,
        default=Priority.LOW
    )
    
    class Status(models.TextChoices):
        NOT_STARTED = "NS", "Not Started"
        CONTACTED = "CONT", "Contacted"
        FOLLOW_UP_NEEDED = "FUN", "Follow-up Needed"
        COMPLETED = "COM", "Completed"
    
    status = models.CharField(
        max_length=16,
        choices=Status,
        default=Status.NOT_STARTED
    )
    
    notes = models.TextField(
        blank=True,
    )
    