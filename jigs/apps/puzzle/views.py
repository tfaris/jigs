from models import Puzzle,PuzzlePiece,PuzzleSession,start_session

from django.shortcuts import render_to_response, get_object_or_404,redirect
from django.http import HttpResponse,Http404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.core.urlresolvers import reverse

import json


def start_puzzle_session(request, guid):
    puzzle = get_object_or_404(Puzzle,guid=guid)
    session = start_session(puzzle)
    return redirect("%s?session=%s" % (reverse("puzzle", args=(guid,)),session.guid))


def session_key(session_guid):
    return "session-%s" % session_guid


def workon_session(request, guid):
    try:
        session_guid = request.GET['session']
        session_dict = cache.get(session_key(session_guid))
        if session_dict is None:
            session = get_object_or_404(PuzzleSession,guid=session_guid)
            session_dict = session.create_session_dict()

        context = RequestContext(request)
        context['session_data'] = session_dict
        context['session_guid'] = session_guid

        cache.set(session_key(session_guid), session_dict)
        return render_to_response("puzzle/puzzle_view.html",context_instance=context)
    except KeyError:
        return Http404()
        
@csrf_exempt        
def session_status(request, guid):
    try:
        data = json.loads(request.body)
    except:
        data = request.GET

    session_guid = data.get('session') or data.get('session')
    session_dict = cache.get(session_key(session_guid))
    if session_dict is None:
        session = get_object_or_404(PuzzleSession, guid=session_guid)
        session_dict = session.create_session_dict()

    try:
        context = RequestContext(request)
        
        if request.method == "POST":
            for key, value in data.items():
                if key.startswith("sessp"):
                    sp_id = key.replace("sessp","")
                    piece_dict = session_dict.get(sp_id)
                    if piece_dict:
                        print "Rewriting %s to %s" % (sp_id, value)
                        piece_dict["pos"] = (value[0], value[1])

        cache.set(session_key(session_guid), session_dict)
        return HttpResponse(json.dumps(session_dict),mimetype='application/json')
    except KeyError:
        return Http404()    