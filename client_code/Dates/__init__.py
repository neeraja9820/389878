from ._anvil_designer import DatesTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date

class Dates(DatesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
 

    # Any code you write here will run before the form opens.

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    if self.date_picker_2.date is not None and self.date_picker_2.date is not None:
     self.label_1.text = self.date_picker_2.date - self.date_picker_1.date

  def date_picker_2_change(self, **event_args):
    """This method is called when the selected date changes"""
    if self.date_picker_2.date is not None and self.date_picker_2.date is not None:
     self.label_1.text = self.date_picker_2.date - self.date_picker_1.date

x = 7
if x > 0 and x <= 5:
  print ('x is between 0 and 5')
elif x == 6:
  print ('x is 6')
elif x > 6:
  print ('x is greater than 6')
else:
  print ('x is less than zero')

# here are 2 common short 1-line formats:

if x == 6: print('x is 6')
print('x is 6' if x == 6 else 'x is not 6')
