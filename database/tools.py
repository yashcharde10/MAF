from sqlalchemy.orm import Session
from database.models import SupportTickets

# Here we will add tools 
def save_ticket_to_db(session: Session, email: str, problem: str)
    new_ticket = SupportTickets(user_email = email, description = problem)
    session.add(new_ticket)
    session.commit()
    return f"Ticket {new_ticket.id} have been saved successsfully."