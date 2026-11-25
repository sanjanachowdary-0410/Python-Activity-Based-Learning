# Case Study 29: Password Policy Validation Engine

## Problem Statement
Evaluate sample password strings against minimum length, character-category rules (uppercase, lowercase, digit, special character), consecutive character repetition limits, and forbidden substrings, explaining every failed rule.

## Objectives
* Check each password against all rules without stopping at the first failure.
* Report clear, human-readable reasons for any rule violation.

## Assumptions
* Minimum length = `8` characters.
* Must contain at least one uppercase letter, one lowercase letter, one digit, and one special character from `"!@#$%^&*_-+"`.
* No more than `2` identical characters in a row (e.g., `"aaa"` fails).
* Forbidden substrings (case-insensitive): `["password", "admin", "1234", "qwerty"]`.

## Algorithm
1. Store sample passwords in a list.
2. For each password, initialize a `reasons` list.
3. Check length, character types via loops, consecutive runs, and forbidden substrings.
4. Print `"STRONG"` if `reasons` is empty; otherwise print each reason.

## Flowchart
```text
[Start] --> [For Each Password] --> [Check Length >= 8]
  --> [Check Upper, Lower, Digit, Special] --> [Check Max Consecutive <= 2]
  --> [Check Forbidden Substrings] --> [Any Failures? (Yes -> List Reasons / No -> Strong)]
  --> [End]
```

## Pseudocode
```text
BEGIN
    passwords = ["Pass123!abc", "weak", "AAAbbb1!@#", "Secure_99#xyz"]
    forbidden = ["password", "admin", "1234", "qwerty"]
    FOR pwd IN passwords DO
        reasons = []
        IF LENGTH(pwd) < 8 THEN APPEND "Length < 8" TO reasons END IF
        # Check categories, runs, and substrings
        IF LENGTH(reasons) == 0 THEN PRINT pwd + " -> VALID" ELSE PRINT reasons END IF
    END FOR
END
```

## Test Cases & Expected Output
* **Test Case 1 (`"Secure_99#xyz"`):** Passes all checks.
* **Test Case 2 (`"MyPassword!23"`):** Fails due to `"password"` substring.

```text
[PASS] Secure_99#xyz
[FAIL] weak
       - Must be at least 8 characters long
       - Missing uppercase letter
       - Missing digit
       - Missing special character
[FAIL] MyPassword!23
       - Contains forbidden substring 'password'
[FAIL] AAAbbb1!@#
       - Too many repeated characters in a row (3)
[FAIL] NoSpecial123
       - Missing special character
```

## Conclusion
Accumulating every violation into a list gives clear diagnostic feedback rather than hiding multiple issues behind a single check.
