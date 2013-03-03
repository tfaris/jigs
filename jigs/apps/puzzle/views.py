from models import Puzzle,PuzzlePiece,PuzzleSession,start_session

from django.shortcuts import render_to_response, get_object_or_404,redirect
from django.http import HttpResponse,Http404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

import json

def start_puzzle_session(request,guid):
    puzzle = get_object_or_404(Puzzle,guid=guid)
    session = start_session(puzzle)
    return redirect("/puzzle/%s?session=%s" % (puzzle.guid,session.guid))

def workon_session(request,guid):
    puzzle = get_object_or_404(Puzzle,guid=guid)
    try:
        session_guid = request.GET['session']
        session = get_object_or_404(PuzzleSession,guid=session_guid)
        context = RequestContext(request)
        context['puzzle'] = puzzle
        context['session'] = session
        return render_to_response("puzzle/puzzle_view.html",context_instance=context)
    except KeyError:
        return Http404()
        
@csrf_exempt        
def session_status(request,guid):
    try:
        data = json.loads(request.body)
    except:
        data = request.GET
    puzzle = get_object_or_404(Puzzle,guid=guid)
    try:
        session_guid = data.get('session') or data.get('session')
        session = get_object_or_404(PuzzleSession,guid=session_guid)
        context = RequestContext(request)
        
        if request.method == "POST":
            for key,value in data.items():
                if key.startswith("sessp"):
                    sp_id = key.replace("sessp","")
                    session.puzzlesessionpiece_set.filter(piece__id=sp_id).update(x=value[0],y=value[1])
        
        status = {}
        for sess_piece in session.puzzlesessionpiece_set.all():
            status[sess_piece.piece.pk] = sess_piece.x,sess_piece.y
        
        return HttpResponse(json.dumps(status),mimetype='application/json')
    except KeyError:
        return Http404()    