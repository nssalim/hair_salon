# Hair Salon
# Use loops (on lists of collected data) to calculate business operation metrics (past, present and future).

# Prices and Cuts
# names of the cuts offered
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# price of each hairstyle in the hairstyles list
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# number of purchases for each hairstyle type in the last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Note:-
# Each index in hairstyles corresponds to an associated index in prices and last_week


# AVERAGE price of a haircut
# sum of all the haircuts prices
total_price = 0
# Loop through the prices list
for price in prices:
  # add each price to the variable total_price
  total_price += price
# calculate AVERAGE price of haircut
  average_price = total_price / len(prices)
  print("Average Haircut Price: " + str(average_price))


# list comprehension (all haircut prices cut by 5 dollars)
new_prices = [price - 5 for price in prices]
# calculate each PRICE (when reduced by 5 dollars )
print("Each haircut price reduced by 5 dollars: " + str(new_prices))


# amount of revenue  brought in last week
total_revenue = 0
# calculate AMOUNT of revenue brought in last week
for i in range(len(hairstyles)):
# Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step
  total_revenue += prices[i] * last_week[i]
  print("Total Revenue: " + str(total_revenue))


# AVERAGE daily revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: " + str (average_daily_revenue)) 


# list comprehension (haircuts under 30 dollars)
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]
print("Haircuts under 30 dollars" + str(cuts_under_30))
  