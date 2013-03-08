# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Friend'
        db.create_table(u'fandjango_friend', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('facebook_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('friend_of', self.gf('django.db.models.fields.related.ForeignKey')(related_name='friends', to=orm['fandjango.User'])),
        ))
        db.send_create_signal(u'fandjango', ['Friend'])

        # Adding model 'Like'
        db.create_table(u'fandjango_like', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('facebook_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='likes', to=orm['fandjango.User'])),
            ('like_id', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'fandjango', ['Like'])


    def backwards(self, orm):
        # Deleting model 'Friend'
        db.delete_table(u'fandjango_friend')

        # Deleting model 'Like'
        db.delete_table(u'fandjango_like')


    models = {
        u'fandjango.friend': {
            'Meta': {'object_name': 'Friend'},
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'friend_of': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friends'", 'to': u"orm['fandjango.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'fandjango.like': {
            'Meta': {'object_name': 'Like'},
            'category': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'facebook_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'likes'", 'to': u"orm['fandjango.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'fandjango.oauthtoken': {
            'Meta': {'object_name': 'OAuthToken'},
            'expires_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issued_at': ('django.db.models.fields.DateTimeField', [], {}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'fandjango.user': {
            'Meta': {'object_name': 'User'},
            'authorized': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'facebook_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_seen_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'oauth_token': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['fandjango.OAuthToken']", 'unique': 'True'}),
            'political_views': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'profile_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quotes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'relationship_status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'verified': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fandjango']