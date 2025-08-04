# coffee prices for different age brackets
customer_age = int(input('enter your age: '))
if customer_age < 18:
    print("coffee price = 20% youth discount")
elif customer_age > 60:
    print("coffee price = 30% senior discount")
else:
    print("coffee price = normal price")
    
