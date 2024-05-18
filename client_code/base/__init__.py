from ._anvil_designer import baseTemplate
from anvil import *
from ..Home import Home


class base(baseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Home())

    
