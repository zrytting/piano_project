from django.db import models
from django.urls import reverse

# Create your models here.
class Portfolio(models.Model):
    
    title = models.CharField(max_length=200)
    contact_email = models.CharField("Contact Email", max_length=200)
    is_active = models.BooleanField(default=True)
    about = models.TextField(max_length=2000)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("portfolio_details", args=(str(self.id)))

class Student(models.Model):
    MAJOR = (
        ('CSCI-BS', 'BS in Computer Science'),
        ('CPEN-BS', 'BS in Computer Engineering'),
        ('BIGD-BI', 'BI in Game Design and Development'),
        ('BICS-BI', 'BI in Computer Science'),
        ('BISC-BI', 'BI in Computer Security'),
        ('CSCI-BA', 'BA in Computer Science'),
        ('DASE-BS', 'BS in Data Analytics and Systems Engineering')
    )
    name = models.CharField(max_length=200)
    email = models.CharField("UCCS Email", max_length=200)
    major = models.CharField(max_length=200,choices=MAJOR)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("student_details", args=[str(self.Portfolio_id)])
    Portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE, primary_key=True)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("project_detail", args=[str(self.id)])
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)