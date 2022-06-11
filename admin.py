from django.contrib import admin
# <HINT> Import any new Models here
from .models import Choice, Course, Lesson, Instructor, Learner, Submission, Question


# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInline(admin.StackedInline):
    model = Question

class ChoiceInline(admin.TabularInline):
    model = Choice

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    exclude = ['total_enrollment']
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    #inlines = [QuestionInline]
    list_display = ['title', 'course']
    list_filter = ['course']


# <HINT> Register Question and Choice models here
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    #fields = ('question_text', 'grade')
    #fields = ('lesson', ('question_text', 'grade'))
    list_display = ['question_text', 'course']
    list_filter = ['course']

#class ChoiceAdmin(admin.ModelAdmin):
#   fields = ('choice_text', 'is_correct')    
     
class InstructorAdmin(admin.ModelAdmin):
    exclude = ("total_learners")


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Submission)
