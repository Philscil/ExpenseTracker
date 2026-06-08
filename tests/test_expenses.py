import pytest
from fastapi.testclient import TestClient
from typing import List

# Import the app and the dependency we want to override

from src.expense_tracker.main import app
from src.expense_tracker.api.routers.expenses import get_expense_service
from src.expense_tracker.api.services.expense_service import ExpenseService
from src.expense_tracker.api.schemas.expense import Expense, ExpenseCreate
from datetime import date

# 1. Create a "Mock" Service for testing

class MockExpenseService(ExpenseService):
	def __init__(self):
		# Start with a fresh, empty list for every test
		self.mock_db: List[Expense] = []

	def get_all_expenses(self) -> List[Expense]:
		return self.mock_db
	
	def create_expense(self, expense_in: ExpenseCreate) -> Expense:
		new_id = len(self.mock_db) + 1
		new_expense = Expense(id=new_id, **expense_in.model_dump())
		self.mock_db.append(new_expense)
		return new_expense
	
# 2. Tell FastAPI to use our Mock Service instead of the real one

def override_get_expense_service():
	return MockExpenseService()

app.dependency_overrides[get_expense_service] = override_get_expense_service

# 3. Create the test client
client = TestClient(app)

# --- The Test ---

def test_get_expenses_empty():
	"""Test that the API returns an empty list when no expenses exist"""
	response = client.get("/expenses")
	assert response.status_code == 200
	assert response.json() == []

def test_create_expense():
	"""Test that we can create a new expense"""
	payload = {
		"title": "Test Pizza",
		"amount": 15.50,
		"category": "Food",
		"date": str(date.today())
	}

	response = client.post("/expenses/", json=payload)

	# Check that it succeeded

	assert response.status_code == 201

	# Check that the returned data matche what we sent
	data = response.json()
	assert data["title"] == "Test Pizza"
	assert data["amount"] == 15.50
	assert "id" in data # Pydantic should have generate an ID

def test_create_invalid_expense():
	"""Test that Pydantic blocks negative amounts"""
	payload = {
		"title": "Free Money",
		"amount": -100.00, # INVALID
		"category": "Fraud",
		"date": str(date.today())
	}

	response = client.post("/expenses/", json=payload)

	assert response.status_code == 422