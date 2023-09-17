#take in input
num_purchases = int(input('Number of purchases: '))
tax = float(input('Sales tax: '))

names = []
purchase_costs = []
for i in range(num_purchases):
    names.append(input('Name: '))
    purchase_costs.append(int(input('Cost: ')))

tax_costs = []
def add_tax(purchases, sales_tax):
    for cost in purchases:
        tax_costs.append(cost*(1.0+ sales_tax))

add_tax(purchase_costs, tax)

name_purchase = dict()
for i in range(len(names)):

    #if statement checks for duplicates
    if names[i] in name_purchase:
        name_purchase[names[i]] = name_purchase[names[i]] + tax_costs[i]
    else: 
        name_purchase[names[i]] = tax_costs[i]
print(name_purchase)