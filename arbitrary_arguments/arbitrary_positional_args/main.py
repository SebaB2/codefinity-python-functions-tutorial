def calculate_total(*values):
    if not values:
        return "Your cart is empty."

    total = sum(values)

    if sum(values) >= 200:
        total *= (1-0.2)  # 20% discount
    elif 100 <= sum(values) < 200:
        total *= (1-0.1)  # 10% discount

    return f"Final total: ${total:.2f}"

# Testing the result
print(calculate_total(30, 20, 50))
print(calculate_total(100, 50, 80))
print(calculate_total(150, 100))
print(calculate_total())