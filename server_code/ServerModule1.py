# Fichier ServerModule1.py corrigé

# 🚨 AJOUTEZ CETTE LIGNE MANQUANTE 🚨
import anvil 
# -----------------------------------

import anvil.email
import anvil.server
import anvil.pdf
from anvil.pdf import PDFRenderer
import datetime 

@anvil.server.callable
# Mise à jour des arguments
def create_pdf(email, name, title, organisation, event):
  # ... (reste du code inchangé)
  # Date Dynamique : génère la date/heure actuelle au format désiré
  date_badge = datetime.datetime.now().strftime("Émis le %d %B %Y à %H:%M") 

  # Génération du PDF : 
  # 'email' n'est pas passé au render_form car il n'est pas dans le template Ticket
  pdf = PDFRenderer(filename=f'{name} Badge.pdf').render_form(
    'Ticket', 
    name=name, 
    date=date_badge, 
    title=title, 
    organisation=organisation, 
    event=event # Événement choisi
  )
  return pdf

@anvil.server.callable
def send_pdf_email(email, name, title, organisation, event):
  # 🚨 CORRECTION 2 : L'email DOIT être passé à create_pdf 🚨
  # Appelle la fonction de création PDF mise à jour
  pdf = create_pdf(email, name, title, organisation, event) 

  anvil.email.send(
    from_address='no-reply',
    from_name='Events & Certificats', 
    to=email, 
    subject='Votre Badge d\'Accès',
    text='Merci de votre inscription ! Votre badge est joint à cet e-mail. Veuillez le conserver pour l\'accès.',
    attachments=pdf
  )
  return pdf