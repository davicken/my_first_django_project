from django.contrib import admin
from .models import Question

# Register your models here.
from .models import Question
from .models import Choice
# admin.site.register(Question)

admin.site.register(Choice)

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#     admin.site.register(Question)

#     from django.contrib import admin
# from .models import Question
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,
    {'fields': ['question_text']}),
    ('Date information', {'fields': ['pub_date']}),
    ]
    admin.site.register(Question)