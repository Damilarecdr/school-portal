from django.urls import path
from .views import list_courses, register_courses, download_registrations, registration_success, registered_courses, payment, payment_callback, payment_receipt, view_approved_applications, change_student_class

urlpatterns = [
    path('courses/', list_courses, name='list_courses'),
    path('register/', register_courses, name='register_courses'),
    path('registration-success/', registration_success, name='registration_success'),
    path('registered-courses/', registered_courses, name='registered_courses'),  # Add this line
    path('download/<int:course_id>/', download_registrations, name='download_registrations'),
    path('payment/', payment, name='payment'),
    path('payment/callback/', payment_callback, name='payment_callback'),
    path('payment/receipt/', payment_receipt, name='payment_receipt'),
    path('students/', view_approved_applications, name='students'),
    path('change-class/<int:application_id>/', change_student_class, name='change_student_class'),
]








