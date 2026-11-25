# Case Study 27: Advanced Numeric Pattern Generator

## Problem Statement
Generate a symmetric hollow numeric diamond pattern based on user-specified half-height `n`, validate input dimensions, and align spacing neatly.

## Objectives
* Validate `n >= 2` so the diamond has a clear hollow interior.
* Use nested loops and string formatting to construct the upper and lower halves symmetrically.

## Assumptions
* `n` represents the number of rows from the top tip to the widest middle row (`n = 4` produces `7` total rows).
* Each row prints symmetric numbers `1..k..1` on the outer edges with spaces in the hollow middle.

## Algorithm
1. Validate `n >= 2`.
2. Loop `row` from `1` to `n` (top half): compute leading spaces, print left number, inner spaces (for `row > 1`), and matching right number (for `row > 1`).
3. Loop `row` from `n - 1` down to `1` (bottom half) using the exact same symmetry.

## Flowchart
```text
[Start] --> [Set n] --> [n >= 2?] --No--> [Print Error & Stop]
  --Yes--> [Loop row = 1..n] --> [Print Left/Hollow/Right]
  --> [Loop row = n-1..1] --> [Print Left/Hollow/Right] --> [End]
```

## Pseudocode
```text
BEGIN
    n = 4
    IF n < 2 THEN
        PRINT "Invalid dimension"
        STOP
    END IF
    FOR r FROM 1 TO n DO
        spaces_out = "  " * (n - r)
        IF r == 1 THEN
            PRINT spaces_out + "1"
        ELSE
            spaces_in = "  " * (2 * r - 3)
            PRINT spaces_out + STR(r) + spaces_in + STR(r)
        END IF
    END FOR
    FOR r FROM n - 1 DOWNTO 1 DO
        spaces_out = "  " * (n - r)
        IF r == 1 THEN
            PRINT spaces_out + "1"
        ELSE
            spaces_in = "  " * (2 * r - 3)
            PRINT spaces_out + STR(r) + spaces_in + STR(r)
        END IF
    END FOR
END
```

## Test Cases & Expected Output
* **Test Case 1 (`n = 4`):** Produces a 7-row hollow numeric diamond.
* **Test Case 2 (`n = 1`):** Rejected with validation message.

```text
      1
    2   2
  3       3
4           4
  3       3
    2   2
      1
```

## Conclusion
Separating outer and inner spacing expressions makes hollow numeric symmetry easy to reason about and maintain.
