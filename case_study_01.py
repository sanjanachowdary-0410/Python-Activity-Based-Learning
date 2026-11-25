months = ["January", "February", "March", "April"]
monthly_units = [90, 145, 260, 360]

bills = []
fixed_charge = 75.0

for i in range(len(monthly_units)):
    units = monthly_units[i]
    energy_charge = 0.0

    if units <= 100:
        energy_charge = units * 3.0
    elif units <= 200:
        energy_charge = (100 * 3.0) + ((units - 100) * 4.5)
    else:
        energy_charge = (100 * 3.0) + (100 * 4.5) + ((units - 200) * 6.0)

    total = energy_charge + fixed_charge

    if units > 300:
        total = total + (total * 0.05)  # 5% surcharge
    if units <= 100:
        total = total - 50.0  # Rebate for low usage

    bills.append(round(total, 2))

print("--- Monthly Electricity Bills ---")
for i in range(len(months)):
    print(f"{months[i]}: {monthly_units[i]} units -> Rs. {bills[i]:.2f}")

print("\n--- Unusual Consumption Increases (> 30%) ---")
found_alert = False
for i in range(1, len(monthly_units)):
    prev_u = monthly_units[i - 1]
    curr_u = monthly_units[i]
    if prev_u > 0:
        increase_pct = ((curr_u - prev_u) / prev_u) * 100
        if increase_pct > 30:
            print(f"{months[i]} jumped by {increase_pct:.1f}% ({prev_u} -> {curr_u} units)")
            found_alert = True

if not found_alert:
    print("No unusual spikes detected.")

avg_bill = sum(bills) / len(bills)
print(f"\nAverage Monthly Bill: Rs. {avg_bill:.2f}")
