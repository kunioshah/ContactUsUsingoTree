
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'ContactUs'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    Name = models.StringField(label='What is your Name?')
    Email = models.StringField(label='What is your email?')
    Question = models.StringField(label='Why are you contacting us?')
class ContactUs(Page):
    form_model = 'player'
    form_fields = ['Email', 'Name', 'Question']
class ThankYou(Page):
    form_model = 'player'
page_sequence = [ContactUs, ThankYou]