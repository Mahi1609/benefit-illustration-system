import json
from db.database import SessionLocal
from db.models import Calculation


def serialize_data(data: dict):
    return json.loads(json.dumps(data, default=str))


def save_calculation(input_data, result_data, irr, user_id):
    db = SessionLocal()

    # 🔥 Convert to JSON-safe
    input_data = serialize_data(input_data)
    result_data = serialize_data(result_data)

    record = Calculation(
        user_id=user_id,  # ✅ ADD THIS
        input_data=input_data,
        result_data=result_data,
        irr=irr
    )

    db.add(record)
    db.commit()
    db.refresh(record)
    db.close()

    return record


def get_user_history(user_id: int):
    db = SessionLocal()

    records = db.query(Calculation).filter(
        Calculation.user_id == user_id
    ).order_by(Calculation.created_at.desc()).all()

    db.close()

    return records