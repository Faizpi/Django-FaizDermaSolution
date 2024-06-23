import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    name = models.CharField(max_length=200, blank=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    file = models.FileField(upload_to='files', blank=True)
    image = models.FileField(upload_to='images', blank=True)

    class Meta:
        db_table = u'firstapp_question'

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return self.image

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
