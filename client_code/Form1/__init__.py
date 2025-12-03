from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.


  def register_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.name_box.text
    email = self.email_box.text
    date = self.date_dropdown.selected_value
  
    if name and email and date:
      alert(f'Thanks for registering! Your ticket is downloading and will be sent to {email}.')
  
      pdf = anvil.server.call('send_pdf_email', email, name, date)
      anvil.media.download(pdf)
  
    else:
      alert('You have not completed all required fields')