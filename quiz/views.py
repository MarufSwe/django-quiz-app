from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Question, Topic, Question, Quiz, QuizQuestion
from datetime import timedelta
from django.utils.cache import add_never_cache_headers


def dashboard(request):
    return render(request, 'dashboard.html')


def quiz_view(request, topic_name):
    topic = get_object_or_404(Topic, name=topic_name)
    questions = Question.objects.filter(topic=topic).order_by('?')[:10]  # Get 10 random questions

    response = render(request, 'quiz_page.html', {
        'topic': topic,
        'questions': questions,
    })

    # Add headers to prevent caching (new questions and time for redirect to quiz page)
    add_never_cache_headers(response)
    return response


# def quiz_result(request, topic_name):
#     if request.method == 'POST':
#         topic = get_object_or_404(Topic, name=topic_name)
#         questions = Question.objects.filter(topic=topic)
#         score = 0
#         total_questions = questions.count()
#
#         for question in questions:
#             selected_answer = request.POST.get(f'question{question.id}')
#             if selected_answer == question.correct_answer:
#                 score += 1
#
#         # Calculate time taken for the quiz
#         time_taken_seconds = int(request.POST.get('time_taken', '0'))
#         time_taken = timedelta(seconds=time_taken_seconds)
#
#         return render(request, 'quiz_result.html', {
#             'topic': topic,
#             'score': score,
#             'total_questions': total_questions,
#             'time_taken': time_taken
#         })
#     else:
#         return redirect('dashboard')


def quiz_result(request, topic_name):
    if request.method == 'POST':
        topic = get_object_or_404(Topic, name=topic_name)
        questions = Question.objects.filter(topic=topic)
        score = 0
        total_questions = questions.count()

        question_details = []
        for question in questions:
            selected_answer = request.POST.get(f'question{question.id}')
            is_correct = selected_answer == question.correct_answer
            if is_correct:
                score += 1

            question_details.append({
                'question': question,
                'selected_answer': selected_answer,
                'correct_answer': question.correct_answer,
                'is_correct': is_correct
            })

        # Calculate time taken for the quiz
        time_taken_seconds = int(request.POST.get('time_taken', '0'))
        time_taken = timedelta(seconds=time_taken_seconds)

        return render(request, 'quiz_result.html', {
            'topic': topic,
            'score': score,
            'total_questions': total_questions,
            'time_taken': time_taken,
            'question_details': question_details
        })
    else:
        return redirect('dashboard')