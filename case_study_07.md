# Case Study 37: Nested Loop Calendar Generator

## Problem Statement
Generate a formatted monthly calendar given a starting weekday index and number of days in the month, aligning weeks cleanly and validating inputs.

## Objectives
* Validate `start_day` (`0..6`, where `0` = Monday) and `num_days` (`28..31`).
* Use nested loops to format 7-column weeks with aligned day numbers.

## Assumptions
* `0` = Mon, `1` = Tue, `2` = Wed, `3` = Thu, `4` = Fri, `5` = Sat, `6` = Sun.
* Valid month lengths are `28`, `29`, `30`, or `31`.

## Algorithm
1. Check that `0 <= start_day <= 6` and `num_days in [28, 29, 30, 31]`.
2. Print weekday header row.
3. Use a `while` loop over `day = 1..num_days` and an inner `for` loop across the 7 columns (`col = 0..6`), printing blanks before `start_day` on week 1 and after `num_days`.

## Flowchart
```text
[Start] --> [Validate start_day & num_days] --Invalid--> [Print Error]
  --Valid--> [Print Header] --> [Loop Weeks Until day > num_days]
  --> [Inner Loop col = 0..6] --> [Print Day or Blank] --> [Print Newline] --> [End]
```

## Pseudocode
```text
BEGIN
    start_day = 2   # Wednesday
    num_days = 31
    IF start_day < 0 OR start_day > 6 OR num_days NOT IN [28, 29, 30, 31] THEN
        PRINT "Invalid input"
        STOP
    END IF
    PRINT "Mon Tue Wed Thu Fri Sat Sun"
    day = 1
    first_week = TRUE
    WHILE day <= num_days DO
        line = ""
        FOR col FROM 0 TO 6 DO
            IF (first_week AND col < start_day) OR day > num_days THEN
                line = line + "    "
            ELSE
                IF day < 10 THEN
                    line = line + "  " + STR(day) + " "
                ELSE
                    line = line + " " + STR(day) + " "
                END IF
                day = day + 1
            END IF
        END FOR
        PRINT line
        first_week = FALSE
    END WHILE
END
```

## Test Cases & Expected Output
* **Test Case 1 (`start_day = 3`, `num_days = 30`):** Starts on Thursday (`col = 3`) and runs through `30`.
* **Test Case 2 (`num_days = 32`):** Rejected as invalid month length.

```text
Mon Tue Wed Thu Fri Sat Sun
             1   2   3   4 
  5   6   7   8   9  10  11 
 12  13  14  15  16  17  18 
 19  20  21  22  23  24  25 
 26  27  28  29  30        
```

## Conclusion
Nested loops with fixed column widths make grid-based calendar formatting straightforward and predictable.
