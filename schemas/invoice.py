from pydantic import BaseModel
from typing import List


class BillSundry(BaseModel):
    billSundryName: str
    amount: float

    '''
        Validations for BillSundrys:
        The amount can be negative or positive.
    '''

class InvoiceHeader(BaseModel):
    date: str
    invoiceNumber: int
    customerName: str
    billingAddress: str
    shippingAddress: str
    GSTIN: str
    totalAmount: float
    '''
        Validations for Invoice:
        TotalAmount = Sum(InvoiceItems's Amount) + Sum(InvoiceBillSundry's Amount)
        InvoiceNumber should autoincremental and hence should be unique.
    '''


class InvoiceItem(BaseModel):
    itemName: str
    quantity: float
    price: float
    amount: float
    '''
        Validations for InvoiceItems:
        Amount = Quantity x Price
        Price, Quantity, and Amount must be greater than zero.
    '''



class CreateInvoiceRequest(BaseModel):
    invoiceHeader: InvoiceHeader
    billSundry: BillSundry
    invoiceItems: List[InvoiceItem]