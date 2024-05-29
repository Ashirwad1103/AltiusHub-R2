from fastapi import APIRouter
from .endpoints.invoice import invoice_router

api_router = APIRouter(prefix="/api")


api_router.include_router(invoice_router)

