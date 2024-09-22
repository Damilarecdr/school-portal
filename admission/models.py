from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    CLASS_CHOICES = [
        ('CREACH', 'CREACH'),
        ('KG 1','KG 1'),
        ('KG 2','KG 2'),
        ('NURSERY 1', 'NURSERY 1'),
        ('NURSERY 2', 'NURSERY 3'),
        ('NURSERY 3', 'NURSERY 3'),
        ('PRIMARY 1', 'PRIMARY 1'),
        ('PRIMARY 2', 'PRIMARY 2'),
        ('PRIMARY 2', 'PRIMARY 2'),
        ('PRIMARY 3', 'PRIMARY 3'),
        ('PRIMARY 4', 'PRIMARY 4'),
        ('PRIMARY 5', 'PRIMARY 4'),
        ('JSS 1', 'JSS 1'),
        ('JSS 2', 'JSS 2'),
        ('JSS 3', 'JSS 3'),
        ('SSS 1', 'SSS 1'),
        ('SSS 2', 'SSS 2'),
        ('SSS 3', 'SSS 3'),
    ]
    STATE_CHOICES = [
        ('ABIA', 'Abia'),
        ('ADAMAWA', 'Adamawa'),
        ('AKWA IBOM', 'Akwa Ibom'),
        ('ANAMBRA', 'Anambra'),
        ('BAUCHI', 'Bauchi'),
        ('BAYELSA', 'Bayelsa'),
        ('BENUE', 'Benue'),
        ('BORNO', 'Borno'),
        ('CROSS RIVER', 'Cross River'),
        ('DELTA', 'Delta'),
        ('EBONYI', 'Ebonyi'),
        ('EDO', 'Edo'),
        ('EKITI', 'Ekiti'),
        ('ENUGU', 'Enugu'),
        ('GOMBE', 'Gombe'),
        ('IMO', 'Imo'),
        ('JIGAWA', 'Jigawa'),
        ('KADUNA', 'Kaduna'),
        ('KANO', 'Kano'),
        ('KATSINA', 'Katsina'),
        ('KEBBI', 'Kebbi'),
        ('KOGI', 'Kogi'),
        ('KWARA', 'Kwara'),
        ('LAGOS', 'Lagos'),
        ('NASARAWA', 'Nasarawa'),
        ('NIGER', 'Niger'),
        ('OGUN', 'Ogun'),
        ('ONDO', 'Ondo'),
        ('OSUN', 'Osun'),
        ('OYON', 'Oyo'),
        ('PLATEAU', 'Plateau'),
        ('RIVERS', 'Rivers'),
        ('SOKOTO', 'Sokoto'),
        ('TARABA', 'Taraba'),
        ('YOBE', 'Yobe'),
        ('ZAMFARA', 'Zamfara'),
        ('FCT', 'Federal Capital Territory'),
    ]

    

    DEPARTMENT_CHOICES = [
        ('SCIENCE', 'SCIENCE'),
        ('ART', 'ART'),
        ('SOCIAL_SCIENCE', 'SOCIAL_SCIENCE')
    ]
 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admission_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    surname = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    disability = models.CharField(max_length=255, blank=True, null=True)
    passport = models.ImageField(upload_to='passports/')
    last_class = models.CharField(max_length=100)

    # Address Section
    state_of_origin = models.CharField(max_length=100, choices=STATE_CHOICES)
    lga = models.CharField(max_length=100)
    current_address = models.TextField()

    # Parent/Guardian Details
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=20)
    parent_address = models.TextField()
    parent_relationship = models.CharField(max_length=100)
    parent_email = models.EmailField()

    # Educational Needs
    special_needs = models.BooleanField(default=False)

    # Class Applying to
    class_applying = models.CharField(max_length=10, choices=CLASS_CHOICES)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    
    # Declaration
    declaration = models.BooleanField(default=False)

    # Admission Status
    is_approved = models.BooleanField(default=False)
    date_admission_approved = models.DateField(blank=True, null=True) 

    def __str__(self):
        return f'{self.surname} {self.other_names} - {self.class_applying}'

    @property
    def email(self):
        return self.user.email  # Accessing the email from the User model



class School_Fee_Payment(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    school_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    is_paid = models.BooleanField(default=False)
    date_paid = models.DateField(blank=True, null=True)  # Optional field for payment date
    transaction_reference = models.CharField(max_length=100, blank=True, null=True)  # New field

    def __str__(self):
        return f'{self.application.user} - Paid: {self.is_paid}'


class Session(models.Model):
    current_session = models.CharField(max_length=100)

    def __str__(self):
        return self.current_session


from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.course.name}'
