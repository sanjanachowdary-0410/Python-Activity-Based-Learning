# Case Study 2: Progressive Electricity Billing

## Problem Statement
Calculate monthly household electricity bills using progressive consumption slabs, fixed charges, surcharges, and rebates, compare bills across multiple months, and flag unusual month-to-month consumption increases.

## Objectives
* Compute slab-wise energy charges accurately using loops and conditionals.
* Apply fixed charges, surcharges, and rebates cleanly.
* Detect unusually high month-over-month jumps ($> 30\%$) across a sequence of months.

## Assumptions
* Monthly unit readings are stored in a list as non-negative numbers.
* Slab rates: First $100$ units @ `Rs. 3.00/unit`; next $100$ units ($101\text{--}200$) @ `Rs. 4.50/unit`; above $200$ units @ `Rs. 6.00/unit`.
* Fixed charge = `Rs. 75.00/month`; $5\%$ surcharge applies if units $> 300$; `Rs. 50.00` rebate applies if units $\le 100$.
* A month-over-month increase greater than $30\%$ over the previous month is flagged as an unusual increase.

## Algorithm
1. Start with a list of monthly unit readings and month names.
2. For each month's units, calculate slab charges using progressive thresholds.
3. Add fixed charge, apply surcharge if units $> 300$, and subtract rebate if units $\le 100$.
4. Store each month's total bill in a list.
5. Compare consecutive months; if percentage increase $> 30\%$, record a warning.
6. Display monthly bills, average bill, and any unusual increase alerts.

## Flowchart
```text
[Start] --> [Load Months & Units] --> [Loop Each Month]
  --> [Calculate Slab Cost + Fixed + Surcharge - Rebate] --> [Save Bill]
  --> [More Months? (Yes -> Loop / No -> Compare Consecutive Months)]
  --> [Increase > 30%? (Yes -> Flag Alert / No -> Continue)]
  --> [Print Summary & Alerts] --> [End]
```

## Pseudocode
```text
BEGIN
    months = ["Jan", "Feb", "Mar", "Apr"]
    units_list = [90, 145, 260, 360]
    bills = []
    FOR i FROM 0 TO LENGTH(units_list) - 1 DO
        u = units_list[i]
        cost = 0
        IF u <= 100 THEN
            cost = u * 3.0
        ELSE IF u <= 200 THEN
            cost = 100 * 3.0 + (u - 100) * 4.5
        ELSE
            cost = 100 * 3.0 + 100 * 4.5 + (u - 200) * 6.0
        END IF
        cost = cost + 75.0
        IF u > 300 THEN cost = cost * 1.05 END IF
        IF u <= 100 THEN cost = cost - 50.0 END IF
        APPEND cost TO bills
    END FOR
    FOR i FROM 1 TO LENGTH(units_list) - 1 DO
        IF units_list[i - 1] > 0 THEN
            pct = ((units_list[i] - units_list[i - 1]) / units_list[i - 1]) * 100
            IF pct > 30 THEN PRINT "Alert at " + months[i] END IF
        END IF
    END FOR
END
```

## Test Cases & Expected Output
* **Test Case 1 (Standard multi-month progression):** `monthly_units = [90, 145, 260, 360]`.
  * Jan: `90 * 3 + 75 - 50 = 295.00`
  * Feb: `300 + 45*4.5 + 75 = 577.50` (jump: `61.1%` -> flagged)
  * Mar: `300 + 450 + 60*6 + 75 = 1185.00` (jump: `79.3%` -> flagged)
  * Apr: `300 + 450 + 160*6 + 75 = 1785.00`, plus $5\%$ surcharge = `1874.25` (jump: `38.5%` -> flagged)
* **Test Case 2 (Steady usage):** `monthly_units = [120, 130, 125]` -> no alerts triggered.

```text
--- Monthly Electricity Bills ---
January: 90 units -> Rs. 295.00
February: 145 units -> Rs. 577.50
March: 260 units -> Rs. 1185.00
April: 360 units -> Rs. 1874.25

--- Unusual Consumption Increases (> 30%) ---
February jumped by 61.1% (90 -> 145 units)
March jumped by 79.3% (145 -> 260 units)
April jumped by 38.5% (260 -> 360 units)

Average Monthly Bill: Rs. 982.94
```

## Conclusion
Progressive slab billing and trend comparison work cleanly with parallel lists and conditional thresholds, helping households spot sudden energy spikes early.
