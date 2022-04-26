from authentication.models import User
from django.db import models


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wiki_title = models.CharField(max_length=50)
    target_lang = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return '{} : {}'.format(self.user.full_name, self.wiki_title)


class Sentence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    target_lang = models.CharField(max_length=2)
    original_sentence = models.TextField(blank=True, null=True)
    translated_sentence = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'sentences'

    def __str__(self):
        return '{} : {}'.format(self.user.full_name, self.id)
