from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import *
# Create your views here.
# views are a type of web page in the Django app
# They will all have their own template as part of a specific function.
# these will set a specific URL in place. The argument "request" is the request to the page (IE GET, POST ETC)
# The argument question_id is the question id that is input
# HTTP response is what the page will post
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)