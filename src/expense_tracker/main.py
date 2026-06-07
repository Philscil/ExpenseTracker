from fastapi import FastAPI
from src.expense_tracker.api.routers import health

def create_app() -> FastAPI:

	app = FastAPI(
		title="Expense Tracker API",
		description="A clean API for tracking expenses",
		version="0.1.0"
	)

	# Include routers
	app.include_router(health.router)

	return app

app = create_app()