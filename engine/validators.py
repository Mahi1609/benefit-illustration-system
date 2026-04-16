from datetime import date

VALID_FREQUENCIES = {"Yearly", "Half-Yearly", "Monthly"}

def calculate_acb(dob: date) -> int:
    today = date.today()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age


def validate_inputs(data: dict):
    errors = []

    premium = data["premium"]
    pt = data["pt"]
    ppt = data["ppt"]
    freq = data["frequency"]
    sum_assured = data["sum_assured"]
    dob = data["dob"]

    # 1. Range checks
    if not (10000 <= premium <= 50000):
        errors.append("Premium must be between 10,000 and 50,000")

    if not (10 <= pt <= 20):
        errors.append("Policy Term must be between 10 and 20")

    if not (5 <= ppt <= 10):
        errors.append("Premium Payment Term must be between 5 and 10")

    # 2. PT > PPT
    if pt <= ppt:
        errors.append("Policy Term must be greater than PPT")

    # 3. Frequency check
    if freq not in VALID_FREQUENCIES:
        errors.append("Invalid premium frequency")

    # 4. Sum Assured rule
    if sum_assured < max(10 * premium, 500000):
        errors.append("Sum assured must be >= max(10×premium, 500000)")

    # 5. Age validation
    age = calculate_acb(dob)
    if not (23 <= age <= 56):
        errors.append("Age must be between 23 and 56")

    if errors:
        raise ValueError(errors)