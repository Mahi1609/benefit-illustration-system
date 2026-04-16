from engine.calculation_engine import run_calculation
from datetime import date


def test_calculation_success():
    data = {
        "dob": date(1995, 5, 10),
        "gender": "Male",
        "premium": 20000,
        "pt": 15,
        "ppt": 10,
        "frequency": "Yearly",
        "sum_assured": 500000
    }

    result = run_calculation(data)

    assert "irr" in result
    assert isinstance(result["irr"], float)
    assert len(result["illustration"]) == 15