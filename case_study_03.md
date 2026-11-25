# Case Study 13: ATM Transaction Sequence Simulation

## Problem Statement
Process a sequence of deposits and withdrawals, maintain a running balance, enforce per-withdrawal limits and non-negative balance rules, reject invalid operations, and print a summary.

## Objectives
* Validate every transaction in order using a loop and conditionals.
* Enforce a single-withdrawal cap and sufficient-funds check.
* Record accepted and rejected transactions for final reporting.

## Assumptions
* Initial balance = `Rs. 15,000.00`.
* Single withdrawal limit = `Rs. 10,000.00`.
* Transactions are stored as a list of tuples: `(tx_type, amount)` where `tx_type` is `"DEPOSIT"` or `"WITHDRAW"`.

## Algorithm
1. Initialize balance, withdrawal limit, and lists for accepted and rejected logs.
2. Loop through each `(tx_type, amount)` tuple via tuple unpacking.
3. Reject non-positive amounts or unknown types.
4. For `"DEPOSIT"`, add to balance and log acceptance.
5. For `"WITHDRAW"`, reject if `amount > limit` or `amount > balance`; otherwise subtract and log acceptance.
6. Print final balance and transaction counts.

## Flowchart
```text
[Start] --> [Set Balance = 15000, Limit = 10000] --> [For Each (Type, Amt)]
  --> [Amt > 0?] --No--> [Reject]
  --> [Type == DEPOSIT?] --Yes--> [Add Amt & Log]
  --> [Type == WITHDRAW & Amt <= Limit & Amt <= Balance?]
        --Yes--> [Subtract Amt & Log] --No--> [Reject]
  --> [Print Final Balance & Summary] --> [End]
```

## Pseudocode
```text
BEGIN
    balance = 15000.0
    max_withdraw = 10000.0
    transactions = [("DEPOSIT", 5000), ("WITHDRAW", 12000), ("WITHDRAW", 4000), ("WITHDRAW", 20000)]
    accepted = 0
    rejected = 0
    FOR tx_type, amount IN transactions DO
        IF amount <= 0 THEN
            rejected = rejected + 1
        ELSE IF tx_type == "DEPOSIT" THEN
            balance = balance + amount
            accepted = accepted + 1
        ELSE IF tx_type == "WITHDRAW" THEN
            IF amount <= max_withdraw AND amount <= balance THEN
                balance = balance - amount
                accepted = accepted + 1
            ELSE
                rejected = rejected + 1
            END IF
        ELSE
            rejected = rejected + 1
        END IF
    END FOR
    PRINT balance, accepted, rejected
END
```

## Test Cases & Expected Output
* **Test Case 1 (Mixed valid/invalid operations):** `15000 + 5000 - 4500 + 3000 = 18500.00`, with 3 rejections.
* **Test Case 2 (Exact withdrawal limit):** `WITHDRAW 10000.0` when balance is $\ge 10000.0$ -> accepted.

```text
ACCEPTED: DEPOSIT Rs. 5000.00 | Balance: Rs. 20000.00
REJECTED: WITHDRAW Rs. 12000.00 (Exceeds Rs. 10000.00 limit)
ACCEPTED: WITHDRAW Rs. 4500.00 | Balance: Rs. 15500.00
REJECTED: WITHDRAW Rs. 25000.00 (Insufficient balance)
REJECTED: DEPOSIT Rs. -200.00 (Amount must be positive)
ACCEPTED: DEPOSIT Rs. 3000.00 | Balance: Rs. 18500.00

--- ATM Summary ---
Final Balance: Rs. 18500.00
Accepted Transactions: 3
Rejected Transactions: 3
```

## Conclusion
Tuple unpacking paired with guard checks ensures invalid or over-limit requests never corrupt account balances.
