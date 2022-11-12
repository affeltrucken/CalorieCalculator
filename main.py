#!/usr/bin/env python3

from colorama import Fore


# CONSTANTS
YELLOW = Fore.LIGHTYELLOW_EX
ORANGE = Fore.YELLOW
RED = Fore.LIGHTRED_EX

RESET = Fore.RESET


def mifflinEquation(weight, height, age, gender, activity) -> float:
    print(f"Using: {YELLOW}Mifflin-St Jeor Equation")
    
    if gender == "male":
        calories = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == "female":
        calories = (10 * weight) + (6.25 * height) - (5 * age) - 161

    calories = calories * activity

    return calories


def getActivityFactor() -> float:
    print(f"""
{YELLOW}Exercise{RESET} implies elevated heart activity for 15-30 minutes.
{ORANGE}Intense exercise{RESET} implies elevated heart activity for 45-120 minutes.
{RED}Very intensive exercise{RESET} implies 2+ hours of elevated heart activity.
""")

    activity_level_factors = {
        "0" : 1,
        "1" : 1.2,
        "2" : 1.375,
        "3" : 1.465,
        "4" : 1.55,
        "5" : 1.725,
        "6" : 1.9
    }

    activity_levels = [
        f"1. {YELLOW}BMR{RESET}\n  Basal Metabolic Rate\n",
        f"2. {YELLOW}Sedentary{RESET}\n  Little to no exercise\n",
        f"3. {YELLOW}Light{RESET}\n  Exercise 1-3 times/week\n",
        f"4. {YELLOW}Moderate{RESET}\n  Exercise 4-5 times/week\n",
        f"5. {YELLOW}Very Active{RESET}\n Intense exercise 6-7 times/week\n",
        f"6. {YELLOW}Extra Active{RESET}\n  Very intense exercise daily, or physical job\n"
    ]

    for level in activity_levels:
        print(level)

    try:
        activity_factor = activity_level_factors[input("\nActivity level (1-6): ")]
    except KeyError:
        print(f"\n{RED}Invalid option.")
        activity_factor = activity_level_factors[input("\nActivity level (1-6): ")]
    
    return activity_factor


def getGender() -> str:
    while True:
        gender = input(f"{RESET}Gender (m/f): {YELLOW}").lower()[0]
        print()

        if gender == "m":
            return "male"
        elif gender == "f":
            return "female"
        else:
            print(f"{RED}Invalid option.")


def main():
    print(RESET)

    gender = getGender()
    print()

    height = float(input(f"{RESET}Height (cm): {YELLOW}"))
    print()

    weight = float(input(f"{RESET}Weight (kg): {YELLOW}"))
    print()

    age = float(input(f"{RESET}Age (years): {YELLOW}"))
    print()

    activity_factor = getActivityFactor()
    print()

    maintainence_calories = mifflinEquation(
                        weight=weight,
                        height=height,
                        age=age,
                        gender=gender,
                        activity=activity_factor)

    print(f"\n{RESET}Daily calories: {YELLOW}{maintainence_calories}{RESET}\n")


if __name__ == "__main__":
    main()
