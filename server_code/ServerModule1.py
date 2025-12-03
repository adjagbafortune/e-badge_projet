import anvil.email
import anvil.server
import anvil.pdf
from anvil.pdf import PDFRenderer

@anvil.server.callable
def create_pdf(name, date):
  pdf = PDFRenderer(filename=f'{name} Ticket.pdf').render_form('Ticket', name, date)
  return pdf

  
@anvil.server.callable
def send_pdf_email(email, name, date):
  pdf = create_pdf(name, date)
  anvil.email.send(
    from_address='no-reply',
    from_name='Events', 
    to=email, 
    subject='Your Ticket',
    text='Thanks for registering! Your ticket is attached to this email.',
    attachments=pdf
  )
  return pdf
