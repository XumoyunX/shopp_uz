from django.db import models




class Categoriya(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Book(models.Model):
    categoriya = models.ForeignKey(Categoriya, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.PositiveBigIntegerField()
    text = models.TextField()
    aftur = models.CharField(max_length=250)
    dete_added = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)


    def __str__(self):
        return self.name



