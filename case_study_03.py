balance = 15000.0
withdrawal_limit = 10000.0

transactions = [
    ("DEPOSIT", 5000.0),
    ("WITHDRAW", 12000.0),  # Exceeds Rs. 10,000 limit
    ("WITHDRAW", 4500.0),
    ("WITHDRAW", 25000.0),  # Exceeds available balance
    ("DEPOSIT", -200.0),    # Invalid negative amount
    ("DEPOSIT", 3000.0),
]

accepted_count = 0
rejected_count = 0

for tx_type, amount in transactions:
    if amount <= 0:
        print(f"REJECTED: {tx_type} Rs. {amount:.2f} (Amount must be positive)")
        rejected_count += 1
    elif tx_type == "DEPOSIT":
        balance += amount
        accepted_count += 1
        print(f"ACCEPTED: DEPOSIT Rs. {amount:.2f} | Balance: Rs. {balance:.2f}")
    elif tx_type == "WITHDRAW":
        if amount > withdrawal_limit:
            print(f"REJECTED: WITHDRAW Rs. {amount:.2f} (Exceeds Rs. {withdrawal_limit:.2f} limit)")
            rejected_count += 1
        elif amount > balance:
            print(f"REJECTED: WITHDRAW Rs. {amount:.2f} (Insufficient balance)")
            rejected_count += 1
        else:
            balance -= amount
            accepted_count += 1
            print(f"ACCEPTED: WITHDRAW Rs. {amount:.2f} | Balance: Rs. {balance:.2f}")
    else:
        print(f"REJECTED: Unknown type {tx_type}")
        rejected_count += 1

print("\n--- ATM Summary ---")
print(f"Final Balance: Rs. {balance:.2f}")
print(f"Accepted Transactions: {accepted_count}")
print(f"Rejected Transactions: {rejected_count}")
