from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
	fields = [
	(None, 'pub_date'), 
	('Date information', 'question_text')]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
