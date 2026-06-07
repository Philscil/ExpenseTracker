from fastapi import FastAPI
from src.expense_tracker.api.routers import health, expenses

def create_app() -> FastAPI:

	app = FastAPI(
		title="Expense Tracker API",
		description="A clean API for tracking expenses",
		version="0.1.0"
	)

	# Include routers
	app.include_router(health.router)
	app.include_router(expenses.router)

	return app

app = create_app()