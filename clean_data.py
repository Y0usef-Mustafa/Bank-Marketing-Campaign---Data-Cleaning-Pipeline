import pandas as pd
import numpy as np

#change directory
df = pd.read_csv("bank_marketing.csv")

for col in ["credit_default", "mortgage", "previous_outcome", "campaign_outcome"]:
    print(col)
    print("--------------")
    print(df[col].value_counts())

# Client.csv
# Ensure columns are of string type before using .str accessor
df["job"] = df["job"].astype(str).str.replace(".", "_", regex=False)
df["education"] = df["education"].astype(str).str.replace(".", "_", regex=False)
df["education"] = df["education"].replace("unknown", np.NaN)
df["credit_default"] = df["credit_default"] == "yes"
df["mortgage"] = df["mortgage"] == "yes"
subset_df_clints = df[["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]]

print(subset_df_clints)
subset_df_clints.to_csv("client.csv", index=False)

##campaign.csv
#subset_df_campaign= df[["client_id", "number_contacts", "contact_duration", "previous_campaign_contacts", "previous_outcome","campaign_outcome","last_contact_date"]]
df["previous_outcome"] = df["previous_outcome"] == "success"
df["campaign_outcome"] = df["campaign_outcome"] == "yes"
df["year"] = "2022"
date_str = df["year"] + "-" + df["month"].astype(str) + "-" + df["day"].astype(str)
df["last_contact_date"] = pd.to_datetime(date_str)
subset_df_campaign = df[["client_id", "number_contacts", "contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome", "last_contact_date"]]
print(subset_df_campaign)
subset_df_campaign.to_csv("campaign.csv",index= False)

#econimic.csv
subset_df_econimic = df[["client_id", "cons_price_idx", "euribor_three_months"]]
subset_df_econimic.to_csv("campaign.csv",index= False)
