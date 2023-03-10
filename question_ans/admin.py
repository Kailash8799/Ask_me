from django.contrib import admin
from .models import Question,Answer,Tags,Contact

# # Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['que_id','user','title','likes','date_created']
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['ans_id','user','que_ans','likes','date_created']
@admin.register(Tags)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['t_id','t_name','t_used']
@admin.register(Contact)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['c_id','user','desc','date']
