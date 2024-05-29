

from fastapi import APIRouter, Depends
from ..session import get_db
from sqlalchemy.orm import Session
from ..services.invoice import create_invoice, get_invoice, get_invoice_list, update_invoices, delete_invoices
from ..schemas.invoice import CreateInvoiceRequest

invoice_router = APIRouter(prefix="/invoices", tags=["invoices"])

@invoice_router.post("/invoices")
def create_invoice(createInvoiceRequest: CreateInvoiceRequest, db: Session = Depends(get_db)):
    return create_invoice(createInvoiceRequest=createInvoiceRequest, db=db)


@invoice_router.get("/invoices")
def get_invoice(invoice_uuid: str, db: Session = Depends(get_db)):
    return get_invoice(invoice_uuid=invoice_uuid, db=db)

@invoice_router.get("/invoices/all")
def get_invoice_list(limit: int = 5, offest: int = 0, db: Session = Depends(get_db)):
    return get_invoice_list(limit=limit, offest=offest, db=db)

@invoice_router.put("/invoices")
def update_invoices(update_invoice_request, db: Session = Depends(get_db)):
    return update_invoices(update_invoice_request=update_invoice_request, db=db)

@invoice_router.delete("/invoices")
def delete_invoices(invoice_uuid: str, db: Session = Depends(get_db)):
    return delete_invoices(invoice_uuid=invoice_uuid, db=db)