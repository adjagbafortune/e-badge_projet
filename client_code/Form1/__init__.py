from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.


    # Indentation de la méthode à l'intérieur de la classe Form1
  def badge_button_click(self, **event_args): 
    """Appel méthode lorsque le bouton est cliqué."""
    # 1. Récupération des 5 variables
    name = self.nom_complet_box.text
    title = self.titre_box.text
    organisation = self.organisation_box.text
    email = self.email_box.text
    event = self.evenement_dropdown.selected_value

    # 2. Validation des champs
    if name and title and organisation and email and event:
      alert(f'Merci de votre inscription ! Votre badge est en cours de téléchargement et sera envoyé à {email}.')

      # 3. Appel au serveur avec nos arguments
      pdf = anvil.server.call('send_pdf_email', email, name, title, organisation, event)
      anvil.media.download(pdf)

    else:
      alert('Veuillez remplir tous les champs requis.')

  def card_content_container_1_show(self, **event_args):
    """This method is called when the component is shown on the screen."""
    pass

  def link_1_click(self, **event_args):
    """This method is called clicked"""
    pass
