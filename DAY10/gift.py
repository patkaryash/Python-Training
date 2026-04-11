#WAP to help manager pick the gift for players
#input - 1)products types
# 2)interger representing given value k
# 3)prices of the products

#output -1) price difference in the product

n = 6
k = 13
prices = [10,15,23,14,2,15]
count = 0
for i in range(len(prices)):
    for j in range(len(prices)):
        if prices[j] - prices[i] == k:
            count += 1
print(count)