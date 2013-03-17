# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Puzzle.image_path'
        db.add_column(u'puzzle_puzzle', 'image_path',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Puzzle.image_path'
        db.delete_column(u'puzzle_puzzle', 'image_path')


    models = {
        u'puzzle.puzzle': {
            'Meta': {'object_name': 'Puzzle'},
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'puzzle.puzzlepiece': {
            'Meta': {'object_name': 'PuzzlePiece'},
            'height': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puzzle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['puzzle.Puzzle']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        },
        u'puzzle.puzzlesession': {
            'Meta': {'object_name': 'PuzzleSession'},
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'puzzle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['puzzle.Puzzle']"})
        },
        u'puzzle.puzzlesessionpiece': {
            'Meta': {'object_name': 'PuzzleSessionPiece'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piece': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['puzzle.PuzzlePiece']"}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['puzzle.PuzzleSession']"}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['puzzle']