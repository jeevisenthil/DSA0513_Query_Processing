import pandas as pd

# Create sales data
data = {
    "Item": ["Television","Home Theater","Television","Cell Phone","Television",
             "Home Theater","Television","Television","Television","Home Theater",
             "Television","Home Theater","Home Theater","Television",
             "Desk","Video Games","Home Theater","Cell Phone"],
    "Units": [95,50,36,27,56,60,75,90,32,60,90,29,81,35,2,16,28,64]
}

sales_data = pd.DataFrame(data)

# Pivot Table - Item wise total units
pivot2 = pd.pivot_table(
    sales_data,
    values="Units",
    index="Item",
    aggfunc="sum"
)

print("Item Wise Units Sold:")
print(pivot2)
