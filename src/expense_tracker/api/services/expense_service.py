from typing import List
from datetime import date
from src.expense_tracker.api.schemas.expense import Expense, ExpenseCreate


DUMMY_DB: List[Expense] = [
	Expense(id=1, title="Coffee", amount=4.50, category="Food", date=date.today()),
	Expense(id=2, title="Internet Bill", amount=60.00, category="Utilities", date=date.today())
]

class ExpenseService:
	def get_all_expenses(self) -> List[Expense]:
		return DUMMY_DB
	
	def create_expense(self, expense_in: ExpenseCreate) -> Expense:
		new_id = len(DUMMY_DB) + 1
		new_expense = Expense(id=new_id, **expense_in.model_dump())
		DUMMY_DB.append(new_expense)
		return new_expense