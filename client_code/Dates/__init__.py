from ._anvil_designer import DatesTemplate
from anvil import *
from datetime import date

class Dates(DatesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    self.update_label()
  def date_picker_2_change(self, **event_args):
    """This method is called when the selected date changes"""
    self.update_label()
    
  def label_1_show(self, **event_args):
    """This method updates the label with the difference between two dates."""
    if self.date_picker_1.date is not None and self.date_picker_2.date is not None:
       date_diff = self.date_picker_2.date - self.date_picker_1.date
       self.label_1.text = str(date_diff.days) + " days"
       x = 7
       if 0 < x <= 5:
          print('x is between 0 and 5')        
       elif x == 6:
          print('x is 6')
       elif x > 6:
          print('x is greater than 6')
       else:        
          print('x is less than zero')
       
       print('x is 6' if x == 6 else 'x is not 6')
      
