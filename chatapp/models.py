from django.db import models


class StatInfo(models.Model):
    id = models.IntegerField('ID', primary_key=True)
    count = models.IntegerField('Count connected')

    def __str__(self):
        if self.id == 1:
            return 'Bro = ' + str(self.count)
        else:
            return 'Sis = ' + str(self.count)


class MessageInfo(models.Model):
    id = models.IntegerField('ID', primary_key=True)
    username = models.CharField('User name', max_length=255)
    message = models.CharField('Message', max_length=5)

    def __str__(self):
        return self.username
