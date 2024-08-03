from .models import Topic, Question, Topic, Question, Quiz, QuizQuestion
import random
from django.utils.cache import add_never_cache_headers
from django.shortcuts import render, get_object_or_404, redirect
from datetime import timedelta


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


def quiz_view(request, topic_name):
    topic = get_object_or_404(Topic, name=topic_name)
    questions = list(Question.objects.filter(topic=topic))
    random.shuffle(questions)
    selected_questions = questions[:10]

    # Store the question IDs in the session in the same order for shows to result page
    request.session['selected_question_ids'] = [q.id for q in selected_questions]

    return render(request, 'quiz_page.html', {
        'topic': topic,
        'questions': selected_questions
    })


def quiz_result(request, topic_name):
    if request.method == 'POST':
        topic = get_object_or_404(Topic, name=topic_name)
        question_ids = request.session.get('selected_question_ids', [])
        questions = Question.objects.filter(id__in=question_ids)

        # Create a dictionary to map question IDs to questions
        question_map = {q.id: q for q in questions}

        score = 0
        user_answers = []

        for question_id in question_ids:
            question = question_map.get(question_id)
            if question:
                selected_answer = request.POST.get(f'question{question.id}')
                correct = selected_answer == question.correct_answer if selected_answer else False
                if correct:
                    score += 1
                user_answers.append({
                    'question': question,
                    'selected_answer': selected_answer,
                    'correct': correct
                })

        # Calculate time taken for the quiz
        time_taken_seconds = int(request.POST.get('time_taken', '0'))
        time_taken = timedelta(seconds=time_taken_seconds)

        return render(request, 'quiz_result.html', {
            'topic': topic,
            'score': score,
            'total_questions': len(questions),
            'time_taken': time_taken,
            'user_answers': user_answers
        })
    else:
        return redirect('dashboard')
