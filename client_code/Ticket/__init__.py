from ._anvil_designer import TicketTemplate
from anvil import *
import anvil.server

# Fichier Ticket.py (Template de Badge)

class Ticket(TicketTemplate):
  # Le constructeur doit accepter TOUTES les données passées par le serveur
  def __init__(self, name, date, title, organisation, event, **properties): 
    # 'date' sera la date dynamique générée par le serveur
    # 'event' est l'ancien champ 'date', mais nous le gardons ici

    self.init_components(**properties)

    # Assurez-vous que vous avez des Labels pour ces propriétés dans votre Design View du Badge
    self.name_label.text = name
    self.date_label.text = date # Date d'émission dynamique
    self.title_label.text = title
    self.organisation_label.text = organisation
    self.event_label.text = event 
    # ... mettez à jour tous les labels pour correspondre à votre design