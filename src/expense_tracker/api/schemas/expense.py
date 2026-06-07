from pydantic import BaseModel, Field
from datetime import date

# Base properties shared across all Expense models
class ExpenseBase(BaseModel):
	title: str = Field(..., description="A short description of the expense", examples=["API Tokens"])
	amount: float = Field(..., gt=0, description="The cost must be greater than zero")
	category: str = Field(..., examples=["Food", "Utilities", "Entertainment", "Tech"])
	date: date

# Used when the client sends data to create a new expense
class ExpenseCreate(ExpenseBase):
	pass

# Used when we return an expense t the client (includes the database ID)
class Expense(ExpenseBase):
	id: int

	# This config tells Pydantic to play nicely with our Database Models later
	model_config = {"from_attributes": True}