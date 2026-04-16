# IRR Calculation Functions

import numpy_financial as npf

def calculate_irr(cashflows: list) -> float:
    irr = npf.irr(cashflows)
    return round(irr * 100, 2) if irr is not None else None