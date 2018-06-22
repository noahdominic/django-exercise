from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from .models import Question, Choice


class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '../accounts/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'


    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = "../../accounts/login"
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(LoginRequiredMixin, generic.DetailView):
    login_url = "../../../accounts/login"
    model = Question
    template_name = 'polls/results.html'

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/results.html', {
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
