from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
#from django.template import loader
# Shortcut for raising a 404 page
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone
from django.conf.urls import *


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions (Not including the ones that will be published in the future)"""
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        :return:
        """
        return Question.objects.filter(pub_date=timezone())


class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question



"""
Old code that was replaced with generic views
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')

    context = {
        'latest_question_list': latest_question_list,
    }
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)
"""


"""
Old code that was replaced with generic views
def detail(request, question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    # Originally returning an HttpResponse
    # return HttpResponse("You're looking at question %s." % question_id)
    #return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
"""


"""
Old code that was replaced with generic views
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""