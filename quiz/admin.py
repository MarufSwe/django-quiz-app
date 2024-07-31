from django.contrib import admin
from .models import Topic, Question, Quiz, QuizQuestion


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'topic', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer')
    list_filter = ('topic',)
    search_fields = ('question_text', 'option_a', 'option_b', 'option_c', 'option_d')


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'start_time', 'end_time', 'score')
    list_filter = ('topic', 'start_time', 'end_time')
    search_fields = ('topic__name',)


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'question', 'answer')
    list_filter = ('quiz',)
    search_fields = ('quiz__id', 'question__question_text')
