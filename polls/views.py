from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


# the render() function takes the request object as its first argument, a
# template name as its second argument and a dictionary as its optional third
# argument. It returns an HttpResponse object of the given template rendered
# with the given context.
def index(request) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question": question})


def results(request, question_id: int) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id: int) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)
