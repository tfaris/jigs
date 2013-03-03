# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Puzzle'
        db.create_table(u'puzzle_puzzle', (
            ('guid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
        ))
        db.send_create_signal(u'puzzle', ['Puzzle'])

        # Adding model 'PuzzlePiece'
        db.create_table(u'puzzle_puzzlepiece', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('puzzle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['puzzle.Puzzle'])),
        ))
        db.send_create_signal(u'puzzle', ['PuzzlePiece'])

        # Adding M2M table for field neighbors on 'PuzzlePiece'
        db.create_table(u'puzzle_puzzlepiece_neighbors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_puzzlepiece', models.ForeignKey(orm[u'puzzle.puzzlepiece'], null=False)),
            ('to_puzzlepiece', models.ForeignKey(orm[u'puzzle.puzzlepiece'], null=False))
        ))
        db.create_unique(u'puzzle_puzzlepiece_neighbors', ['from_puzzlepiece_id', 'to_puzzlepiece_id'])


    def backwards(self, orm):
        # Deleting model 'Puzzle'
        db.delete_table(u'puzzle_puzzle')

        # Deleting model 'PuzzlePiece'
        db.delete_table(u'puzzle_puzzlepiece')

        # Removing M2M table for field neighbors on 'PuzzlePiece'
        db.delete_table('puzzle_puzzlepiece_neighbors')


    models = {
        u'puzzle.puzzle': {
            'Meta': {'object_name': 'Puzzle'},
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'puzzle.puzzlepiece': {
            'Meta': {'object_name': 'PuzzlePiece'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'neighbors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['puzzle.PuzzlePiece']", 'symmetrical': 'False'}),
            'puzzle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['puzzle.Puzzle']"})
        }
    }

    complete_apps = ['puzzle']