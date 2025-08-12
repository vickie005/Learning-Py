
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

"""
# Prompt user for inputs
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Get final price using the function
final_price = calculate_discount(price, discount_percent)

# Output the result
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Price: ${price:.2f}")
"""

# Prompt user for inputs (with validation)
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    if price <= 0 or discount_percent < 0:
        print("Error: Price and discount percentage must be non-negative.")
    elif discount_percent > 100:
        print("Error: Discount percentage cannot be more than 100%.")
    else:
        final_price = calculate_discount(price, discount_percent)
        if discount_percent >= 20:
            print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
        else:
            print(f"No discount applied. Price: ${price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values for price and discount.")
    