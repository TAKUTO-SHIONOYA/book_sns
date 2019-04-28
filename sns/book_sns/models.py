from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_id = models.IntegerField(default=0)
    password = models.CharField(max_length=10)
    mail_address = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user_name) + str(self.user_id)


class Already_book(models.Model):
    user_id = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    days = models.DateField()
    comment = models.CharField(max_length=100)
    good =  models.IntegerField(default=0)

    def __str__(self):
        return '<book:id' + str(self.id) + ',' 'user:id' + str(self.user_id)+\
            'title:' + str(self.title) + ',' + 'author:' + str(self.author) +\
            ',' + 'days:' + str(self.days) + ',' + 'comment:' + str(self.comment)
class Not_Yet_Read_Book(models.Model):
    user_id = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    days = models.DateField()
    def __str__(self):
        return '<title:' + str(self.title) + ',' +'author:' + str(self.suthor)
class Response(models.Model):
    user_id = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    response = models.CharField(max_length=100)

    def __str__(self):
        return str(self.response)
