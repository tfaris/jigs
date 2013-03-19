from puzzle.models import PuzzleSession, PuzzleSessionPiece
from puzzle.views import session_key

from celery.task import task

from django.core.cache import cache
from django.db import transaction

@task
def save_cached_sessions():
    """
    Detect any cached sessions and update the database to reflect their current state.
    """
    for session in PuzzleSession.objects.all():
        session_dict = cache.get(session_key(session.guid))
        if session_dict is not None:
            print "Updating session %s" % session.guid
            with transaction.commit_on_success():
                for piece_id, data in session_dict.items():
                    position = data.get("pos")
                    PuzzleSessionPiece.objects.filter(session=session,
                                                      piece__pk=piece_id).update(x=position[0],
                                                                                 y=position[1])
