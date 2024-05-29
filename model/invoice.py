from ..session import Base



class BillSundry(Base):
    id: int
    uuid: str
    billSundryName: str
    amount: float

class InvoiceHeader(Base):
    id: int
    uuid: str
    BillSundryUUID: str #add foreign key here
    date: str
    invoiceNumber: int
    customerName: str
    billingAddress: str
    shippingAddress: str
    GSTIN: str
    totalAmount: float

class InvoiceItem(Base):
    id: int
    uuid: str
    BillSundryUUID: str #add foreign key here
    itemName: str
    quantity: float
    price: float
    amount: float