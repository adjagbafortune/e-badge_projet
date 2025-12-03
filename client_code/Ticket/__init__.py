from ._anvil_designer import TicketTemplate
from anvil import *
import anvil.server

class Ticket(TicketTemplate):
  def __init__(self, name, date, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_label.text = name
    self.date_label.text = date
    # Any code you write here will run before the form opens.
