from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=255)
    user_name = models.TextField()
    
    class Meta:
        managed = False
        db_table = u'\"{}\".\"user\"'.format('sample')
        app_label = 'sample'