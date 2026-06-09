from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from src.expense_tracker.api.schemas.expense import Expense, ExpenseCreate
from src.expense_tracker.api.services.expense_service import ExpenseService
from src.expense_tracker.api.core.database import get_db

router = APIRouter(prefix="/expenses", tags=["Expenses"])

# Dependency Provider: FastAPI uses this to inject the service
def get_expense_service(db: Session = Depends(get_db)) -> ExpenseService:
	return ExpenseService(db)

@router.get("/", response_model=List[Expense])
async def get_expenses(service: ExpenseService = Depends(get_expense_service)) -> List[Expense]:
	"""Retrieve a list of all expenses"""
	return service.get_all_expenses()

@router.post("/", response_model=Expense, status_code=201)
async def create_expense(
	expense_in: ExpenseCreate,
	service: ExpenseService = Depends(get_expense_service)
) -> Expense:
	"""Create a new expense"""

	return service.create_expense(expense_in)