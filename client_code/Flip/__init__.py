from ._anvil_designer import FlipTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import time


class Flip(FlipTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.image_1.source = None
    coins = ['http://re-bol.com/heads.jpg', 'http://re-bol.com/tails.jpg']
    coin = random.choice(coins)
    time.sleep(1)
    self.image_1.source = URLMedia(coin)
