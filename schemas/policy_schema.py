from pydantic import BaseModel, Field
from datetime import date
from typing import Literal


class PolicyInput(BaseModel):
    dob: date
    gender: Literal["Male", "Female"]
    premium: int = Field(..., ge=10000, le=50000)
    pt: int = Field(..., ge=10, le=20)
    ppt: int = Field(..., ge=5, le=10)
    frequency: Literal["Yearly", "Half-Yearly", "Monthly"]
    sum_assured: int