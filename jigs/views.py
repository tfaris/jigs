from puzzle.models import Puzzle,PuzzleSession

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def home(request):
    context = RequestContext(request)
    context['puzzles'] = Puzzle.objects.all()
    return render_to_response("jigs/index.html",context_instance=context)