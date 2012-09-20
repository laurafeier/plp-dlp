from polls.models import Poll
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    latest_polls = Poll.objects.all().order_by("-pub_date")[:5]
    return render_to_response("polls/index.html", {"latest_polls": latest_polls})


def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response("polls/detail.html", {"poll": p})


def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response("polls/result.html", {"poll": p})


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response("polls/vote.html", {"poll": p})
