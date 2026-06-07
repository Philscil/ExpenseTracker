from fastapi import APIRouter, HTTPException
from typing import List
from src.expense_tracker.api.schemas.expense import Expense, ExpenseCreate
from datetime import date

router = APIRouter(prefix="/expenses", tags=["Expenses"])

# Temporary Database

DUMMY_DB: List[Expense] = [
	Expense(id=1, title="Coffee", amount=4.50, category="Food", date=date.today()),
	Expense(id=2, title="Internet Bill", amount=60.00, category="Utilities", date=date.today())
]

@router.get("/", response_model=List[Expense])
async def get_expenses() -> List[Expense]:
	"""Retrieve a list of all expenses"""
	return DUMMY_DB

@router.post("/", response_model=Expense, status_code=201)
async def create_expense(expense_in: ExpenseCreate) -> Expense:
	"""Create a new expense"""

	# Generate a fake ID
	new_id = len(DUMMY_DB) + 1

	# expense_in.model.dump() converts the Pydantic object back to a dictionary
	# so we can unpack it (**) into our new Expense object
	new_expense = Expense(id=new_id, **expense_in.model_dump())

	DUMMY_DB.append(new_expense)
	return new_expense