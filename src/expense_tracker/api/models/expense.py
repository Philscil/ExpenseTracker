from sqlalchemy import Column, Integer, String, Float, Date
from src.expense_tracker.api.core.database import Base

class ExpenseModel(Base):
	# This tells SQLAlchemy to name our table "expenses"
	__tablename__ = "expenses"

	# Defining the colums of the table
	id = Column(Integer, primary_key=True, index=True)
	title = Column(String, index=True, nullable=False)
	amount = Column(Float, nullable=False)
	category = Column(String, index=True, nullable=False)
	date = Column(Date, nullable=False)