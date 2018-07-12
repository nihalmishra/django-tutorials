from django.contrib import admin
from blog.models import Post
from polls.models import Choice, Question

# Register your models here.

admin.site.register(Post)
# admin.site.register(Question)
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    ordering = ['-pub_date']
admin.site.register(Question, QuestionAdmin)    
# admin.site.register(Choice)