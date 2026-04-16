# Core Calculation Engine Functions

from .validators import validate_inputs
from .irr import calculate_irr
from .config import BONUS_RATES

def run_calculation(data: dict) -> dict:
    # Step 1: Validate
    validate_inputs(data)

    premium = data["premium"]
    pt = data["pt"]
    ppt = data["ppt"]
    sum_assured = data["sum_assured"]

    illustration = []
    cashflows = []
    accumulated_bonus = 0

    for year in range(1, pt + 1):
        # Premium logic
        yearly_premium = premium if year <= ppt else 0

        # Bonus
        bonus_rate = BONUS_RATES[min(year - 1, len(BONUS_RATES) - 1)]
        bonus_amount = bonus_rate * sum_assured
        accumulated_bonus += bonus_amount

        # Maturity benefit
        total_benefit = 0
        if year == pt:
            total_benefit = sum_assured + accumulated_bonus

        # Net cashflow
        net_cashflow = total_benefit - yearly_premium
        cashflows.append(net_cashflow)

        illustration.append({
            "year": year,
            "premium": yearly_premium,
            "bonus_rate": bonus_rate,
            "bonus_amount": round(bonus_amount, 2),
            "total_benefit": round(total_benefit, 2),
            "net_cashflow": round(net_cashflow, 2)
        })

    # IRR
    irr = calculate_irr(cashflows)

    return {
        "irr": irr,
        "illustration": illustration
    }