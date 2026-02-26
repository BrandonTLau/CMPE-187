# Welson Kuang, {INSERT NAME}
# CMPE 187 Group MW 14
# 28 February 2026

""" Financial Aid Eligibility: The code goes through multiple decision statements to check if a student is eligible for a student aid package.
                                Our code aims to highlight Control Flow.
"""

# For stylistic separation of text
def dashes():
    print("-" * 100)

###

# Age Check
age = int(input("\nHow old are you?: "))

if (age < 18 or age > 24):
    dashes()
    print("\nNot eligible. Age requirement not met.\n")
    dashes()
    exit()

# CA Residency Check (& Dean's Consideration)
years_in_ca = float(input("\nHow many years have you lived in California?: "))
months_worked = int(input("\nHow many months have you worked in California?: "))
parents_in_ca = float(input("\nHow many years has your parent(s) lived in California?: "))
volunteered = (input("\nHave you volunteered for a public cause in California? (yes/no): ") == 'yes')

income = int(input("\nWhat is your household income?\n"))

residency_met = (
    years_in_ca >= 2 or
    months_worked >= 6 or
    parents_in_ca >= 2 or
    volunteered
)

if residency_met:
    dashes()
    print("\nEligible for financial aid package!\n")
    dashes()
elif (income < 5000):
    dashes()
    print("\nEligible by Dean's Consideration!\n")
    dashes()
else:
    dashes()
    print("\nNot eligible. US residency requirement not met.\n")
    dashes()