import UUIDField

from PIL import Image

from django.db import models,transaction
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings

import os,shutil,random


class Puzzle(models.Model):
    guid = UUIDField.UUIDField(primary_key=True)
    
    directory = property(fget=lambda self:os.path.join(settings.MEDIA_ROOT,self.guid))
    
    def get_piece_paths(self):
        return [os.path.join(self.directory,"%s.jpg"%piece.pk) for piece in self.puzzlepiece_set.all()]


class PuzzlePiece(models.Model):
    puzzle = models.ForeignKey(Puzzle)
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField(default=100)
    height = models.IntegerField(default=100)
    
    path = property(fget=lambda self:self.puzzle.guid+"/%s.jpg"%self.pk)


class PuzzleSession(models.Model):
    guid = UUIDField.UUIDField(primary_key=True)
    puzzle = models.ForeignKey(Puzzle)

    def create_session_dict(self):
        d = {}
        for sess_piece in self.puzzlesessionpiece_set.all():
            d[str(sess_piece.piece.pk)] = {"pos": (sess_piece.x, sess_piece.y),
                                           "size": (sess_piece.piece.width, sess_piece.piece.height),
                                           "locked_by": None,
                                           "path": sess_piece.piece.path}
        return d

    
class PuzzleSessionPiece(models.Model):
    session = models.ForeignKey(PuzzleSession)
    piece   = models.ForeignKey(PuzzlePiece)
    x = models.IntegerField()
    y = models.IntegerField()    


def start_session(puzzle):
    session = PuzzleSession(puzzle=puzzle)
    session.save()
    pieces = puzzle.puzzlepiece_set.all()
    possible_points = []    
    for piece in pieces:
        possible_points.append((piece.x,piece.y))
    
    for piece in pieces:
        x,y = random.choice(possible_points)
        session_piece = PuzzleSessionPiece(session=session,piece=piece,x=x,y=y)
        session_piece.save()
        possible_points.remove((x,y))
    return session



def create_puzzle(image_path,piece_width=100,piece_height=100):
    img = Image.open(image_path)
    w,h = piece_width,piece_height
    tiles_x,tiles_y = img.size[0]/w,img.size[1]/h
        
    with transaction.commit_on_success():
        puzzle = Puzzle()
        puzzle.save()
        guid = puzzle.guid
        
        piece_dir = puzzle.directory
        if not os.path.exists(piece_dir):
            os.makedirs(piece_dir)
        
        for y in range(0,tiles_y):
            for x in range(0,tiles_x):
                left=x*w
                top=y*h
                right=x*w+w
                bottom=y*h+h
                region = img.crop((left,top,right,bottom))
                
                piece = PuzzlePiece(puzzle=puzzle,x=left,y=top,width=w,height=h)
                piece.save()
                region.save( os.path.join(piece_dir,"%s.jpg"%piece.pk))
    return puzzle
                
@receiver(post_delete)
def delete_puzzle(sender, instance, **kwargs):
    if sender == Puzzle:
        shutil.rmtree(instance.directory)