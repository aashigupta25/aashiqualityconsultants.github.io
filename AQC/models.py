from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key= True)
    name= models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    service = models.TextField()
    desc = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add= True, blank = True)

    def __str__(self):
        return 'Message from' + self.name + ' - ' + self.email