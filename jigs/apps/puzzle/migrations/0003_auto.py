# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field neighbors on 'PuzzlePiece'
        db.delete_table('puzzle_puzzlepiece_neighbors')


    def backwards(self, orm):
        # Adding M2M table for field neighbors on 'PuzzlePiece'
        db.create_table(u'puzzle_puzzlepiece_neighbors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_puzzlepiece', models.ForeignKey(orm[u'puzzle.puzzlepiece'], null=False)),
            ('to_puzzlepiece', models.ForeignKey(orm[u'puzzle.puzzlepiece'], null=False))
        ))
        db.create_unique(u'puzzle_puzzlepiece_neighbors', ['from_puzzlepiece_id', 'to_puzzlepiece_id'])


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
        }
    }

    complete_apps = ['puzzle']