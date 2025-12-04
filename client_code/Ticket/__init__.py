from ._anvil_designer import TicketTemplate
from anvil import *
import anvil.server

# Fichier Ticket.py (Template de Badge)

class Ticket(TicketTemplate):
  # Constructeur pour accepter toutes les données (et passées par le serveur)
  def __init__(self, name, date, title, organisation, event, **properties): 

    self.init_components(**properties)

    self.name_label.text = name
    self.date_label.text = date # Date d'émission dynamique
    self.title_label.text = title
    self.organisation_label.text = organisation
    self.event_label.text = event