from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name