import pandas as pd

df = pd.read_csv("weight_and_height.csv")

df["BMI"] = df["Weight"] / df["Height"]

def bmi_to_risk(bmi):
    if bmi < 18.5:
        return "Nutrient deficient"
    elif bmi < 25:
        return "Lower risk"
    elif bmi < 30:
        return "Heart disease risk"
    elif bmi < 35:
        return "Higher risk of diabetes, heart disease"
    else:
        return "Serious health condition risk"

df["Risk"] = df["BMI"].apply(bmi_to_risk)

print(df.head())
