from sqlalchemy.orm import Session
from ..schemas.invoice import CreateInvoiceRequest


def create_invoice(createInvoiceRequest: CreateInvoiceRequest, db: Session):
    '''
    create invoice header 
    create invoice bill sundry 
    create invoice items
    '''
    
    ...


def get_invoice(invoice_uuid: str, db: Session):
    ...

def get_invoice_list(invoice_uuid: str, limit: int, offest: int, db: Session):
    ...

def update_invoices(update_invoice_request, db: Session):
    pass

def delete_invoices(invoice_uuid: str, db: Session):
    ...