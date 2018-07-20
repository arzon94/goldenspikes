from django.db import models
# from time
# Create your models here.

class Submission(models.Model):
    '''submissions from form'''
    entryTitle = models.TextField()
    client = models.TextField()
    division = models.TextField()
    category = models.TextField()
    status = models.TextField()
    name = models.TextField()
    email = models.EmailField()
    # entryForm = models.FileField(upload_to='submissions/{}/'.format(str(time.time()).replace('.', '')))
    entryForm = models.FileField(upload_to='submissions/')
    summary = models.FileField(upload_to='submissions/')
    file1 = models.FileField(upload_to='submissions/')
    file2 = models.FileField(upload_to='submissions/')
    file3 = models.FileField(upload_to='submissions/')
    link1 = models.URLField()
    link2 = models.URLField()
    link3 = models.URLField()
