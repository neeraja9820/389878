from ._anvil_designer import baseTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Home import Home


class base(baseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Home())

  def title_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    self.content_panel.clear()
    self.content_panel.add_component(Home())

    
