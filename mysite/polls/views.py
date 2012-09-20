from polls.models import Poll, Choice
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    object_list = Poll.objects.all().order_by("-pub_date")[:5]
    return render_to_response("polls/poll_list.html", {"object_list": object_list})


def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response("polls/poll_detail.html", {"object": p})


def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response("polls/results.html", {"object": p})


@csrf_exempt
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selectede_choice = p.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response("polls/poll_dletail.html", {
            "object": p,
            "error_message": "You didn't select a choice."
            })
    else:
        selectede_choice.votes += 1
        selectede_choice.save()
    # always return an hhtpresponseredirect after succesfully dealing
    # with POST data. Prevents data from being posted twice if
    # a user hits back button
        return HttpResponseRedirect(reverse("poll_results", args=(p.id, )))
