from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["System"])

@router.get("/")
async def health_check() -> dict[str, str]:
	"""Check if the API is up and running."""
	return {"status": "ok", "message": "Expense Tracker API is alive!"}