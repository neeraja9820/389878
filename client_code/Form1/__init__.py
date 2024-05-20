from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
     
    
   

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    my_message = self.text_box_1.text
    alert("Hi" + my_message +"!") 
    self.text_box_1.text = ''
    self.text_box_1.focus()
    
    
