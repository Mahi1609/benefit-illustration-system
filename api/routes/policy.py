from fastapi import APIRouter, HTTPException
from engine.calculation_engine import run_calculation
from schemas.policy_schema import PolicyInput
from core.logger import logger
from repositories.calculation_repo import save_calculation
from auth.dependencies import get_current_user
from fastapi import Depends
from repositories.calculation_repo import get_user_history

router = APIRouter()

@router.post("/calculate")
def calculate_policy(data: PolicyInput, user_id: int = Depends(get_current_user)):
    try:
        safe_data = data.model_dump()
        safe_data.pop("dob", None)  # remove sensitive fields if needed

        logger.info(f"Calculation request received")
        logger.info(f"Input (masked): {safe_data}")

        result = run_calculation(data.dict())

        # Save to DB
        save_calculation(input_data=data.dict(), result_data=result, irr=result["irr"], user_id=user_id)

        return {
            "status": "success",
            "message": "Calculation completed successfully",
            "input": data.dict(),
            "data": result
        }

    except ValueError as e:
        logger.warning(f"Validation error: {e.args[0]}")
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "message": "Validation failed",
                "errors": e.args[0]
            }
        )

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "message": "Internal server error"
            }
        )
    

@router.get("/history")
def get_history(user_id: int = Depends(get_current_user)):
    records = get_user_history(user_id)

    history = []

    for record in records:
        history.append({
            "id": record.id,
            "input": record.input_data,
            "result": record.result_data,
            "irr": record.irr,
            "created_at": record.created_at
        })

    return {
        "status": "success",
        "count": len(history),
        "data": history
    }