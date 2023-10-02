from django.shortcuts import render, get_object_or_404, reverse
from django.http import Http404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice


def index(request):
    # template = loader.get_template("polls/index.html")
    context = {"latest_questions_list": Question.objects.all()}
    return render(request, "polls/index.html", context)


def detail(request, q_id):
    qn = get_object_or_404(Question, pk=q_id)
    return render(request, "polls/detail.html", {"question": qn})


def result(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    return render(request, "polls/result.html", {"question": question})


def vote(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    try:
        choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice",
            }
        )
    else:
        choice.votes += 1
        choice.save()
    return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))

