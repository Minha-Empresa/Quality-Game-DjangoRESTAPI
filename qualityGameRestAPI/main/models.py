from django.db import models

# Create your models here.
# Cada usuario terá um estado de jogo que será atualizado a cada nível concluído
class GameState(models.Model):

    class Meta:
        db_table = 'gamestate'

    current_cash = models.FloatField()
    current_approval = models.IntegerField()
    current_client_satisfaction = models.IntegerField()
    current_employees_satisfaction = models.IntegerField()
    current_overrall_satisfaction = models.IntegerField()
    current_level = models.IntegerField()

class User(models.Model):

    class Meta:
        db_table = 'user'
    user_name = models.CharField(max_length=200)
    user_current_state = models.ForeignKey(GameState, on_delete=models.CASCADE)
    user_profile_picture_path = models.CharField(max_length=200, blank=True)

# Cada carta contem um nível ee sua descrição e opções
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

class Event(models.Model):

    class Meta:
        db_table = 'event'

    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    card_cash_ct_effect = models.IntegerField()
    card_cash_wr_effect = models.IntegerField()
    card_approval_ct_effect = models.IntegerField()
    card_approval_wr_effect = models.IntegerField()