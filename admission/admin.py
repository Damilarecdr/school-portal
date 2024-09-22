from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Application, School_Fee_Payment, Session

# Register the Application model
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'surname', 'other_names', 'class_applying', 'is_approved')
    list_filter = ('class_applying', 'is_approved')
    search_fields = ('surname', 'other_names', 'user__email')

# Register the Payment model
@admin.register(School_Fee_Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('application', 'school_fee', 'is_paid')
    list_filter = ('is_paid',)
    search_fields = ('application__user__email',)

class SessionAdmin(admin.ModelAdmin):
    list_display = ('current_session',)

admin.site.register(Session, SessionAdmin)

from django.contrib import admin
from .models import Course, Registration

class RegistrationInline(admin.TabularInline):
    model = Registration
    extra = 0
    readonly_fields = ('user', 'registration_date')  # Adjust as needed

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    inlines = [RegistrationInline]

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'registration_date')
    list_filter = ('course',)
    search_fields = ('user__username', 'course__name')
