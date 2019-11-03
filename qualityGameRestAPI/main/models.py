from django.db import models

# Create your models here.


class Card(models.Model):

    class Meta:

        db_table = 'card'

    card_title = models.CharField(max_length=200)
    card_description = models.CharField(max_length=200)
    card_level = models.IntegerField()
    card_ct_choice = models.CharField(max_length=200)
    card_wr_choice = models.CharField(max_length=200)
    card_image_path = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.card_title