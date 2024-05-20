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
    my_message = "This text contains 'single quotes'"

    my_othermessage = 'This text contains "double quotes"'

    my_bigmessage = '''
    This text 
    contains multiple lines, 
    as well as 'single quotes'
    and "double quotes"
    '''

    # variables can also be assigned to numbers, and other types of data:

    my_number = 48
    alert(my_bigmessage)
    
   

    # Any code you write here will run before the form opens.
