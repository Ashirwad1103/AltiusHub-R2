from sqlalchemy.orm import Session
from typing import List
from ..schemas.invoice import BillSundry, InvoiceHeader, InvoiceItem
from ..model.invoice import InvoiceHeader, BillSundry, InvoiceItem

def create_billSundry(billSundry: BillSundry, db: Session):
    pass

def create_invoice_items(invoiceItemss: List[InvoiceItem] , db: Session):
    pass

def create_invoice_header(invoiceHeader: InvoiceHeader, db: Session):
    pass