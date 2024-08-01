from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Question, Topic, Question
from django.views.decorators.csrf import csrf_protect
from datetime import timedelta


def dashboard(request):
    return render(request, 'dashboard.html')


def quiz_view(request, topic_name):
    topic = get_object_or_404(Topic, name=topic_name)
    questions = Question.objects.filter(topic=topic).order_by('?')[:10]  # Shuffle and get 10 questions

    context = {
        'topic': topic,
        'questions': questions,
    }
    return render(request, 'quiz_page.html', context)


def quiz_result(request, topic_name):
    if request.method == 'POST':
        topic = get_object_or_404(Topic, name=topic_name)
        questions = Question.objects.filter(topic=topic)
        score = 0
        total_questions = questions.count()

        for question in questions:
            selected_answer = request.POST.get(f'question{question.id}')
            if selected_answer == question.correct_answer:
                score += 1

        # Calculate time taken for the quiz
        time_taken_seconds = int(request.POST.get('time_taken', '0'))
        time_taken = timedelta(seconds=time_taken_seconds)

        return render(request, 'quiz_result.html', {
            'topic': topic,
            'score': score,
            'total_questions': total_questions,
            'time_taken': time_taken
        })
    else:
        return redirect('dashboard')
