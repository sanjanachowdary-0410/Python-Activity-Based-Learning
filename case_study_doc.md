Case Study 1: #2 – Progressive Electricity BillingProblem StatementCalculate household electricity bills across multiple months using progressive consumption slabs, fixed charges, surcharges, and rebates, then compare monthly bills to identify unusual increases.   ObjectivesCompute monthly units consumed and apply slab-based tariffs accurately.   Incorporate fixed charges, surcharges, and rebates based on consumption rules.   Detect unusual month-over-month bill increases and summarize results.   AssumptionsTariff slabs per month: 0–100 units @ ₹3.00/unit, 101–300 units @ ₹5.00/unit, >300 units @ ₹7.50/unit.Fixed monthly charge: ₹75.00.Rebate: 5% of slab energy charge if monthly consumption is <= 150 units; surcharge: 10% of slab energy charge if monthly consumption is > 500 units.An "unusual increase" occurs when a month's final bill is more than 25% higher than the previous month's final bill.AlgorithmStart and initialize monthly consumption list (units_list), slab rates, fixed charge, and spike threshold (0.25).For each month's units, calculate progressive slab charges.Apply rebate (-5%) if units <= 150, surcharge (+10%) if units > 500, and add fixed charge (₹75).Store each month's total bill in a list.Compare each month (from the 2nd month onward) against the previous month; flag any increase > 25%.Display monthly breakdown and unusual increase alerts.FlowchartPlaintext[Start]
   |
   v
[Read Monthly Units List]
   |
   v
[Loop Over Each Month's Units]
   |---> Calculate Slab Cost (0-100, 101-300, >300)
   |---> Apply Rebate (<=150) or Surcharge (>500)
   |---> Add Fixed Charge -> Store Bill
   |
   v
[Compare Consecutive Months]
   |---> ((Curr - Prev) / Prev) > 0.25 ? --Yes--> [Flag Unusual Increase]
   |                                        --No---> [Continue]
   v
[Print Monthly Summary & Alerts]
   |
   v
[End]
PseudocodePlaintextBEGIN
    units_list = [95, 180, 340, 560]
    fixed_charge = 75.0
    bills = []

    FOR u IN units_list:
        slab_cost = 0.0
        IF u <= 100:
            slab_cost = u * 3.0
        ELSE IF u <= 300:
            slab_cost = (100 * 3.0) + ((u - 100) * 5.0)
        ELSE:
            slab_cost = (100 * 3.0) + (200 * 5.0) + ((u - 300) * 7.5)

        adjustment = 0.0
        IF u <= 150:
            adjustment = -0.05 * slab_cost
        ELSE IF u > 500:
            adjustment = 0.10 * slab_cost

        total = slab_cost + adjustment + fixed_charge
        APPEND ROUND(total, 2) TO bills
    END FOR

    FOR i FROM 1 TO LENGTH(bills) - 1:
        increase_pct = (bills[i] - bills[i - 1]) / bills[i - 1]
        IF increase_pct > 0.25:
            PRINT "Unusual increase at Month", i + 1
        END IF
    END FOR
END
Python Source CodePythondef calculate_slab_energy(units):
    energy = 0.0
    if units <= 100:
        energy = units * 3.0
    elif units <= 300:
        energy = (100 * 3.0) + ((units - 100) * 5.0)
    else:
        energy = (100 * 3.0) + (200 * 5.0) + ((units - 300) * 7.5)
    return energy


def analyze_electricity_bills(monthly_units, fixed_charge=75.0, spike_threshold=0.25):
    records = []
    for month_idx, units in enumerate(monthly_units, start=1):
        if units < 0:
            print(f"Month {month_idx}: Invalid negative units ({units}) skipped.")
            continue

        energy_charge = calculate_slab_energy(units)
        if units <= 150:
            adjustment = -0.05 * energy_charge
            note = "5% Rebate"
        elif units > 500:
            adjustment = 0.10 * energy_charge
            note = "10% Surcharge"
        else:
            adjustment = 0.0
            note = "Standard"

        total_bill = round(energy_charge + adjustment + fixed_charge, 2)
        records.append((month_idx, units, energy_charge, adjustment, total_bill, note))

    print("\n--- Monthly Electricity Bill Report ---")
    for m_idx, u, eng, adj, bill, note in records:
        print(
            f"Month {m_idx}: Units={u} | Energy=Rs.{eng:.2f} | "
            f"Adj=Rs.{adj:+.2f} ({note}) | Fixed=Rs.{fixed_charge:.2f} | Total=Rs.{bill:.2f}"
        )

    print("\n--- Unusual Increase Analysis (>25% vs Previous Month) ---")
    found_spike = False
    for i in range(1, len(records)):
        prev_month, _, _, _, prev_bill, _ = records[i - 1]
        curr_month, _, _, _, curr_bill, _ = records[i]
        if prev_bill > 0:
            pct_change = ((curr_bill - prev_bill) / prev_bill) * 100
            if pct_change > spike_threshold * 100:
                found_spike = True
                print(
                    f"ALERT: Month {curr_month} bill (Rs.{curr_bill:.2f}) increased by "
                    f"{pct_change:.1f}% from Month {prev_month} (Rs.{prev_bill:.2f})."
                )
    if not found_spike:
        print("No unusual month-over-month bill increases detected.")


# Test execution
sample_units = [95, 180, 340, 560]
analyze_electricity_bills(sample_units)
Test Cases & Expected OutputTest Case 1 (Normal + Spike): Input [95, 180, 340, 560]:Month 1 (95 units): Energy 285.00, Rebate -14.25, Fixed 75.00 -> Rs.345.75Month 2 (180 units): Energy 700.00, Adj 0.00, Fixed 75.00 -> Rs.775.00 (+124.1% -> ALERT)Month 3 (340 units): Energy 1600.00, Adj 0.00, Fixed 75.00 -> Rs.1675.00 (+116.1% -> ALERT)Month 4 (560 units): Energy 3250.00, Surcharge +325.00, Fixed 75.00 -> Rs.3650.00 (+117.9% -> ALERT)Test Case 2 (Steady Usage): Input [120, 125, 130] -> No alerts (<25% change each month).Test Case 3 (Invalid Input): Input [-10, 100] -> Skips -10 with warning and processes 100.ConclusionUsing conditional slab logic, lists, and tuple unpacking, the program accurately calculates progressive utility bills and flags sudden consumption spikes for further investigation.   Case Study 2: #27 – Advanced Numeric Pattern GeneratorProblem StatementGenerate a hollow diamond numeric pattern based on a user-specified dimension n, with input validation for invalid dimensions and clean alignment.   ObjectivesValidate that n is a positive odd integer (n >= 3 and n % 2 == 1).   Construct a symmetric hollow diamond of numbers using nested loops and string alignment.   Assumptionsn represents the total height (number of rows) of the diamond, so n must be odd and >= 3 (e.g., n = 5 or n = 7).Row r (1-indexed from center outward) prints digit r at the left and right boundaries of the hollow diamond.AlgorithmRead integer n; validate n >= 3 and n % 2 == 1. If invalid, display an error message.Let mid = n // 2.Loop row from 0 to n - 1:Compute distance from center: dist = abs(mid - row).Compute number value: num = (mid - dist) + 1.Leading spaces = dist * 2.If dist == mid (top or bottom tip): print str(num).Else: compute inner spaces = (mid - dist) * 2 - 1 and print f"{num}{' ' * (inner_spaces * 2 + 1)}{num}" (spaced for clean visual symmetry).FlowchartPlaintext[Start]
   |
   v
[Input n] --> [n >= 3 and n % 2 == 1?] --No--> [Print Error & Stop]
                      |
                     Yes
                      v
             [mid = n // 2]
                      |
                      v
         [For row = 0 to n - 1]
                      |
                      v
     [dist = |mid - row|, num = mid - dist + 1]
                      |
                      v
          [dist == mid?] --Yes--> [Print Tip]
                |
               No
                v
      [Print Hollow Row with Spaces]
                      |
                      v
         [More Rows?] --Yes--> (Next Row)
                |
               No
                v
              [End]
PseudocodePlaintextBEGIN
    INPUT n
    IF n < 3 OR n MOD 2 == 0 THEN
        PRINT "Invalid dimension. Enter an odd integer >= 3."
        STOP
    END IF

    mid = n DIV 2
    FOR row FROM 0 TO n - 1 DO
        dist = ABS(mid - row)
        num = (mid - dist) + 1
        lead_spaces = " " * (dist * 2)
        IF dist == mid THEN
            PRINT lead_spaces + TO_STRING(num)
        ELSE
            inner_gap = " " * (((mid - dist) * 2) - 1)
            PRINT lead_spaces + TO_STRING(num) + inner_gap + TO_STRING(num)
        END IF
    END FOR
END
