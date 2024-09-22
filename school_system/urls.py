from django.contrib import admin
from django.urls import path, include
from admission import views
from allauth.account.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Allauth URLs
    path('', include('admission.urls')), # This adds all Allauth URL
    path('', LoginView.as_view(), name='account_login'), 
    path('dashboard/', views.dashboard, name='dashboard'),  # User dashboard
    path('apply/', views.apply, name='apply'),  # Admission application
    path('applications/', views.admin_view_applications, name='applications'),  # Admin view applications
    path('approve/<int:application_id>/', views.approve_application, name='approve_application'),  # Admin approve application
    path('payment/', views.payment, name='payment'),
    path('dashboard/general_payment/', views.general_payment, name='general_payment'),
    path('admission-letter/', views.admission_letter, name='admission_letter'),
    path('download-approved-admissions/', views.download_approved_admissions, name='download_approved_admissions'),
    #path('application/', views.application_pdf, name='application_pdf'),
    path('print-application/', views.print_application, name='print_application'),
    #path('upgrade-class/<int:application_id>/', views.upgrade_student_class, name='upgrade_student_class'),
    #path('dashboard/register-courses/', views.register_for_courses, name='register_for_courses'),

    #path('dashboard/register-courses/', views.register_for_courses, name='register_for_courses'),
    # Other URL patterns


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)