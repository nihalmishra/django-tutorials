from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# from django.http import Http404
# from django.template import loader
from  .models import Choice, Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]

    # output = ', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template('polls/home.html')

    # A dictionary for mapping template variable names to Python objects
    context = {
        'latest_question_list': latest_question_list,
    }

    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # common idiom/way to verify existence of object or raise exception
        # try:
        #     question = Question.objects.get(pk=question_id)
        # except Question.DoesNotExist:
        #     raise Http404("Question does not exist!")

    # shortcut provided by Django called get_object_or_404()
    question = get_object_or_404(Question, pk=question_id)
    context =  {'question': question}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didnt select a choice!"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button. https://docs.djangoproject.com/en/1.11/ref/urlresolvers/#django.urls.reverse
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))