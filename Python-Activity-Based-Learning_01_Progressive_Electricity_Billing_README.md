# Case Study 01: Progressive Electricity Billing (Problem #2)

**Source Code File:** [`electricity_billing.py`](./electricity_billing.py)

## 1. Problem Statement
Calculate household electricity bills using multiple consumption slabs, fixed charges, surcharges, and rebates, then compare bills across several months and identify unusual increases.

## 2. Objectives
- Compute monthly electricity consumption charges using progressive tariff slabs.
- Apply conditional rebates and surcharges alongside fixed monthly meter charges.
- Compare month-over-month bills to detect and flag unusual increases.

## 3. Assumptions
- Consumption slabs: 0-100 units @ Rs.3.00/unit, 101-300 units @ Rs.5.00/unit, >300 units @ Rs.7.50/unit.
- Fixed monthly charge: Rs.75.00.
- Rebate: 5% of slab energy charge if monthly units <= 150; Surcharge: 10% of slab energy charge if monthly units > 500.
- Unusual increase threshold: >25% increase compared to the immediately preceding month.

## 4. Algorithm
1. Start and read the list of monthly unit readings.
2. For each month, skip invalid negative readings and compute progressive slab energy charges.
3. Apply conditional rebate (-5%) or surcharge (+10%) and add the fixed charge (Rs.75.00).
4. Store monthly billing records as tuples in a list.
5. Compare consecutive months from index 1 onward; flag any month with >25% increase.
6. Display itemized bills and unusual increase alerts, then stop.

## 5. Flowchart
```text
[Start]
   |
   v
[Read monthly_units List]
   |
   v
[Loop Over Each Month's Units]
   |---> [Calculate Progressive Slab Energy Cost]
   |---> [Apply Rebate (<=150) or Surcharge (>500)]
   |---> [Add Fixed Charge -> Append Record Tuple]
   |
   v
[Compare Consecutive Months (i = 1 to n-1)]
   |---> [((curr_bill - prev_bill) / prev_bill) > 0.25?]
   |        |--Yes--> [Flag Unusual Increase Alert]
   |        |--No---> [Continue]
   v
[Display Billing Statement & Alerts]
   |
   v
[End]
```

## 6. Pseudocode
```text
BEGIN
    SET monthly_units = [95, 180, 340, 560]
    SET fixed_charge = 75.0
    SET records = []

    FOR m_idx FROM 1 TO LENGTH(monthly_units) DO
        units = monthly_units[m_idx - 1]
        IF units <= 100 THEN
            energy = units * 3.0
        ELSE IF units <= 300 THEN
            energy = (100 * 3.0) + ((units - 100) * 5.0)
        ELSE
            energy = (100 * 3.0) + (200 * 5.0) + ((units - 300) * 7.5)
        END IF

        IF units <= 150 THEN
            adj = -0.05 * energy
        ELSE IF units > 500 THEN
            adj = 0.10 * energy
        ELSE
            adj = 0.0
        END IF

        total = energy + adj + fixed_charge
        APPEND (m_idx, units, energy, adj, total) TO records
    END FOR

    FOR i FROM 1 TO LENGTH(records) - 1 DO
        pct = (records[i][4] - records[i - 1][4]) / records[i - 1][4]
        IF pct > 0.25 THEN
            PRINT "Alert: Month", records[i][0], "increased by", pct * 100, "%"
        END IF
    END FOR
END
```

## 7. Test Cases
- Input `[95, 180, 340, 560]`: Month 1 = `Rs.345.75` (5% rebate), Month 2 = `Rs.775.00` (+124.1% Alert), Month 3 = `Rs.1675.00` (+116.1% Alert), Month 4 = `Rs.3650.00` (10% surcharge, +117.9% Alert).
- Input `[120, 125, 130]`: Steady consumption; outputs `No unusual month-over-month increases detected.`
- Input `[-10, 100]`: Skips negative reading with warning and processes valid reading.

## 8. Output Screenshot
> *Run `python electricity_billing.py` in your terminal and attach/embed your output screenshot here (e.g., `![Output](output.png)`).*

## 9. Conclusion
Progressive tariff slabs, conditional rebates/surcharges, and month-over-month spike detection were implemented cleanly using basic loops, conditionals, lists, and tuple unpacking.
