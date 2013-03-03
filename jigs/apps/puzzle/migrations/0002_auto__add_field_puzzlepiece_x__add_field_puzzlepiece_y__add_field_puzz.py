# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PuzzlePiece.x'
        db.add_column(u'puzzle_puzzlepiece', 'x',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'PuzzlePiece.y'
        db.add_column(u'puzzle_puzzlepiece', 'y',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'PuzzlePiece.width'
        db.add_column(u'puzzle_puzzlepiece', 'width',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Adding field 'PuzzlePiece.height'
        db.add_column(u'puzzle_puzzlepiece', 'height',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PuzzlePiece.x'
        db.delete_column(u'puzzle_puzzlepiece', 'x')

        # Deleting field 'PuzzlePiece.y'
        db.delete_column(u'puzzle_puzzlepiece', 'y')

        # Deleting field 'PuzzlePiece.width'
        db.delete_column(u'puzzle_puzzlepiece', 'width')

        # Deleting field 'PuzzlePiece.height'
        db.delete_column(u'puzzle_puzzlepiece', 'height')


    models = {
        u'puzzle.puzzle': {
            'Meta': {'object_name': 'Puzzle'},
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'puzzle.puzzlepiece': {
            'Meta': {'object_name': 'PuzzlePiece'},
            'height': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'neighbors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['puzzle.PuzzlePiece']", 'symmetrical': 'False'}),
            'puzzle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['puzzle.Puzzle']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['puzzle']