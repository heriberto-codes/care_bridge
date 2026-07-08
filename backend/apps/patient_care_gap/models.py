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
        ANNUAL_WELLNESS_VISIT = "Annual Wellness Visit", "Annual Wellness Visit"
        MEDICATION_CHECK = "Medication Check", "Medication Check"
        SCREENING_REMINDER = "Screening Reminder", "Screening Reminder"
        POST_DISCHARGE_FOLLOW_UP = "Post-Discharge Follow-Up", "Post-Discharge Follow-Up"
        
    care_gap_type = models.CharField(
        max_length=30,
        choices=CareGapType.choices,
        default=CareGapType.ANNUAL_WELLNESS_VISIT
    )
    
    class Priority(models.TextChoices):
        LOW = "Low", "Low"
        MEDIUM = "Medium", "Medium"
        HIGH = "High", "High"
    
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.LOW
    )
    
    class Status(models.TextChoices):
        NOT_STARTED = "Not Started", "Not Started"
        CONTACTED = "Contacted", "Contacted"
        FOLLOW_UP_NEEDED = "Follow-up Needed", "Follow-up Needed"
        COMPLETED = "Completed", "Completed"
    
    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.NOT_STARTED
    )
    
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient} - {self.get_care_gap_type_display()}"
    
    
    
    