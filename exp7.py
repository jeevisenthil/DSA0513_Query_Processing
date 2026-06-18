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
    "Item": ["Television","Home Theater","Television","Cell Phone","Television",
             "Home Theater","Television","Television","Television","Home Theater",
             "Television","Home Theater","Home Theater","Television",
             "Desk","Video Games","Home Theater","Cell Phone"],
    "Sale_amt": [113810,25000,43128,6075,67088,30000,89850,107820,38336,30000,
                 107820,14500,40500,41930,250,936,14000,14400],
    "Units": [95,50,36,27,56,60,75,90,32,60,90,29,81,35,2,16,28,64]
}

sales_data = pd.DataFrame(data)

# Q7 Pivot Table
pivot1 = pd.pivot_table(
    sales_data,
    values="Sale_amt",
    index="Item",
    aggfunc=["max", "min"]
)

print("Maximum and Minimum Sale Value of Items:")
print(pivot1)
