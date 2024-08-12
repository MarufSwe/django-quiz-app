# from django.shortcuts import render, get_object_or_404
# from .models import Topic, Question
#
# def quiz_view(request, topic_name):
#     topic = get_object_or_404(Topic, name=topic_name)
#     questions = Question.objects.filter(topic=topic).order_by('?')[:10]  # Shuffle and get 10 questions
#
#     context = {
#         'topic': topic,
#         'questions': questions,
#     }
#     return render(request, 'quiz.html', context)
