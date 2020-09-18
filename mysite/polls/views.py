from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.views import generic
from django.utils import timezone
# Create your views here.
# views are a type of web page in the Django app
# They will all have their own template as part of a specific function.
# these will set a specific URL in place. The argument "request" is the request to the page (IE GET, POST ETC)
# The argument question_id is the question id that is input
# HTTP response is what the page will post
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
 """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
        pub_date_lte=timezone.now()
    ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
#request.POST is dictionary like and lets you access data(always strings) by key name
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votees += 1
        selected_choice.save()
        #Always return an HttpResponseRedirect after succesfully dealing
        #with POST data. This prevents data from being posted twice if a user 
        # hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(questionid,)))
def results(request, question_id):
    question = get_object_or_404(Question, pk=question.id)
    return render(request, 'polls/results.html', {'question': question})


class DetailView(generic.DetailView):
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date_lte=timezone.now())

        