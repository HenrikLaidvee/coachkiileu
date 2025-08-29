# calculations.py

def calculate_bmi(height_cm: float, weight_kg: float):
    """Return BMI value and status string."""
    height_m = height_cm / 100
    bmi = round(weight_kg / (height_m * height_m), 2)

    if bmi < 18.5:
        status = "Alakaal"
    elif 18.5 <= bmi < 25:
        status = "Normaalkaal"
    elif 25 <= bmi < 30:
        status = "Ülekaal"
    else:
        status = "Rasvumine"

    return bmi, status


def calculate_bmr(age: int, gender: str, height_cm: float, weight_kg: float):
    """Return BMR (Mifflin–St Jeor formula)."""
    if gender == "male":
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)

    return round(bmr, 2)
