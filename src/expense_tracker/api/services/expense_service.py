from typing import List
from sqlalchemy.orm import Session
from src.expense_tracker.api.schemas.expense import Expense, ExpenseCreate
from src.expense_tracker.api.models.expense import ExpenseModel

class ExpenseService:

	def __init__(self, db: Session):
		self.db = db

	def get_all_expenses(self) -> List[ExpenseModel]:
		# SELECT * FROM expenses;
		return self.db.query(ExpenseModel).all()
	
	def create_expense(self, expense_in: ExpenseCreate) -> ExpenseModel:
		db_expense = ExpenseModel(**expense_in.model_dump())

		self.db.add(db_expense)

		self.db.commit()

		self.db.refresh(db_expense)

		return db_expense