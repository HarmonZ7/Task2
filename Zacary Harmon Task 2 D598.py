import pandas as pd

df = pd.read_excel('D598_Data_Set.xlsx')

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.rename(columns={"total_long-term_debt" : "total_long_term_debt"})
df[df.duplicated("business_id")]

df_statistics = df.groupby("business_state").mean(numeric_only=True)

df_neg_debt_equity = df[df["debt_to_equity"] < 0]
df_neg_debt_equity[["business_id", "business_state", "debt_to_equity"]]

df_debt_income = pd.DataFrame({"debt_to_income": df["total_long_term_debt"] / df["total_revenue"]})
df_debt_income["business_id"] = df["business_id"]

df_combined = pd.concat([df, df_debt_income["debt_to_income"]], axis=1)

