# Case Study 11: Examination Result and Grace-Mark Validation

## Problem Statement
Process student marks across multiple subjects, apply subject-wise pass criteria and a grace-mark policy, and assign final classifications without exceeding maximum marks per subject.

## Objectives
* Check each subject against a minimum pass mark.
* Distribute limited grace marks only where needed and never exceed `max_marks`.
* Classify final results (`Distinction`, `First Class`, `Pass`, or `Fail`).

## Assumptions
* Each subject is out of `100` marks, with a minimum pass mark of `35`.
* Total grace pool per student is up to `10` marks, at most `5` grace marks per subject.
* Classification (when all subjects pass): $\ge 75\%$ Distinction, $\ge 60\%$ First Class, $< 60\%$ Pass.

## Algorithm
1. Read student name, subject names, raw marks list, and grace pool.
2. Copy raw marks into `final_marks`.
3. For each subject below `35`, calculate needed marks (`35 - mark`), cap at `5` and remaining grace pool, add to `final_marks`, and deduct from grace pool.
4. Check if every subject is $\ge 35$; compute percentage and classification.
5. Print subject-wise adjustments, percentage, and classification.

## Flowchart
```text
[Start] --> [Input Marks & Grace Pool] --> [Loop Subjects]
  --> [Mark < 35? (Yes -> Add Grace up to 5 & Pool, Cap at 100 / No -> Keep Mark)]
  --> [All Subjects >= 35? (Yes -> Calc % & Grade / No -> Fail)]
  --> [Display Result] --> [End]
```

## Pseudocode
```text
BEGIN
    marks = [32, 78, 34, 85, 66]
    grace_pool = 10
    final_marks = COPY(marks)
    FOR i FROM 0 TO LENGTH(final_marks) - 1 DO
        IF final_marks[i] < 35 AND grace_pool > 0 THEN
            needed = 35 - final_marks[i]
            grant = MIN(needed, 5, grace_pool)
            IF final_marks[i] + grant <= 100 THEN
                final_marks[i] = final_marks[i] + grant
                grace_pool = grace_pool - grant
            END IF
        END IF
    END FOR
    passed_all = TRUE
    FOR m IN final_marks DO
        IF m < 35 THEN passed_all = FALSE END IF
    END FOR
    IF passed_all THEN
        avg = SUM(final_marks) / LENGTH(final_marks)
        ...
    ELSE
        grade = "Fail"
    END IF
END
```

## Test Cases & Expected Output
* **Test Case 1 (Recoverable deficits):** `[32, 78, 33, 84, 68]` with `grace_available = 10` -> Math gets `+3` (to `35`), Chemistry gets `+2` (to `35`), total `59.0%` -> `Pass`.
* **Test Case 2 (Unrecoverable deficit):** `[20, 78, 33, 84, 68]` -> Math reaches only `25` (`< 35`) -> `Fail`.

```text
Student: Ananya Rao
  Math: 32 -> 35
  Physics: 78 -> 78
  Chemistry: 33 -> 35
  English: 84 -> 84
  CS: 68 -> 68
Grace Used: 5 | Percentage: 59.00% | Result: Pass
```

## Conclusion
Applying bounded grace marks before checking overall pass status prevents invalid passes while strictly respecting per-subject caps.
