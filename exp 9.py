import pandas as pd

# Create sales data
data = {
    "Region": ["East","Central","Central","Central","West","East","Central",
               "Central","West","East","Central","East","East","East",
               "Central","East","Central","East"],
    "Manager": ["Martha","Hermann","Hermann","Timothy","Timothy","Martha","Martha",
                "Hermann","Douglas","Martha","Hermann","Martha","Douglas",
                "Martha","Douglas","Martha","Hermann","Martha"],
    "SalesMan": ["Alexander","Shelli","Luis","David","Stephen","Alexander","Steven",
                 "Luis","Michael","Alexander","Sigal","Diana","Karen",
                 "Alexander","John","Alexander","Sigal","Alexander"],
    "Sale_amt": [113810,25000,43128,6075,67088,30000,89850,107820,38336,30000,
                 107820,14500,40500,41930,250,936,14000,14400]
}

sales_data = pd.DataFrame(data)

# Pivot Table - Total sale grouped by Region, Manager, SalesMan
pivot3 = pd.pivot_table(
    sales_data,
    values="Sale_amt",
    index=["Region", "Manager", "SalesMan"],
    aggfunc="sum"
)

print("Total Sale Amount (Region, Manager, Salesman wise):")
print(pivot3)
