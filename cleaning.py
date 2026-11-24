import csv

with open(
    "WA_Fn-UseC_-HR-Employee-Attrition.csv", mode="r", encoding="utf-8-sig"
) as infile:
  reader = csv.DictReader(infile)
  fieldnames = reader.fieldnames + [
      "Attrition_Flag",
      "Annual_Income",
      "Est_Replacement_Cost",
      "Tenure_Bracket",
      "Age_Group",
  ]
  rows = []

  for row in reader:
    attrition = row["Attrition"]
    monthly_income = float(row["MonthlyIncome"])
    years = int(row["YearsAtCompany"])
    age = int(row["Age"])

    annual_income = monthly_income * 12
    row["Attrition_Flag"] = 1 if attrition == "Yes" else 0
    row["Annual_Income"] = int(annual_income)
    row["Est_Replacement_Cost"] = (
        round(annual_income * 1.5, 2) if attrition == "Yes" else 0
    )

    if years <= 2:
      row["Tenure_Bracket"] = "0–2 Years"
    elif years <= 5:
      row["Tenure_Bracket"] = "3–5 Years"
    elif years <= 10:
      row["Tenure_Bracket"] = "6–10 Years"
    else:
      row["Tenure_Bracket"] = "10+ Years"

    if age <= 25:
      row["Age_Group"] = "18–25"
    elif age <= 35:
      row["Age_Group"] = "26–35"
    elif age <= 45:
      row["Age_Group"] = "36–45"
    else:
      row["Age_Group"] = "46+"

    rows.append(row)

with open(
    "hr_attrition_cleaned.csv", mode="w", newline="", encoding="utf-8"
) as outfile:
  writer = csv.DictWriter(outfile, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerows(rows)

print(f"Done! Saved {len(rows)} rows to hr_attrition_cleaned.csv")