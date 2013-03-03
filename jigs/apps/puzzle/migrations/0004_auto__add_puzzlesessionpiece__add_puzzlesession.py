# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PuzzleSessionPiece'
        db.create_table(u'puzzle_puzzlesessionpiece', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['puzzle.PuzzleSession'])),
            ('piece', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['puzzle.PuzzlePiece'])),
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('y', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'puzzle', ['PuzzleSessionPiece'])

        # Adding model 'PuzzleSession'
        db.create_table(u'puzzle_puzzlesession', (
            ('guid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('puzzle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['puzzle.Puzzle'])),
        ))
        db.send_create_signal(u'puzzle', ['PuzzleSession'])


    def backwards(self, orm):
        # Deleting model 'PuzzleSessionPiece'
        db.delete_table(u'puzzle_puzzlesessionpiece')

        # Deleting model 'PuzzleSession'
        db.delete_table(u'puzzle_puzzlesession')


    models = {
        u'puzzle.puzzle': {
            'Meta': {'object_name': 'Puzzle'},
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
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