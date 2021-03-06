from django.db import models
import datetime


class Poll(models.Model):

    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    class Meta:
        verbose_name = ('Poll')
        verbose_name_plural = ('Polls')

    def __unicode__(self):
        return self.question

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = "Published today?"
    was_published_today.boolean = True


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    class Meta:
        verbose_name = ('Choice')
        verbose_name_plural = ('Choices')

    def __unicode__(self):
        return self.choice
