from django.contrib import admin

from core.models import (
    University,
    Course,
    Exam,
    Question,
    McqChoices,
)


# Configure admin site
admin.site.site_title = 'EMS Admin'
admin.site.site_header = 'Exam Management System'

# Register models
admin.site.register(University)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(McqChoices)
