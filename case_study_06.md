# Case Study 35: Text Compression Using Character Runs

## Problem Statement
Encode strings using run-length encoding (grouping consecutive identical characters), compare original vs. encoded lengths, and identify when compression is not beneficial.

## Objectives
* Compress runs of repeated characters into `<char><count>`.
* Compare character lengths and report whether compression saves space.

## Assumptions
* Empty strings compress to `""`.
* Runs are case-sensitive (`"a"` $\neq$ `"A"`).
* Compression is considered beneficial only if `len(encoded) < len(original)`.

## Algorithm
1. Iterate through a list of test strings.
2. For non-empty strings, count consecutive matching characters and append `char + str(count)`.
3. Compare `len(encoded)` against `len(original)` and display the result.

## Flowchart
```text
[Start] --> [For Each Text] --> [Empty? (Yes -> "" / No -> Count Runs)]
  --> [Build Encoded String] --> [len(encoded) < len(text)?]
  --> [Print Comparison] --> [End]
```

## Pseudocode
```text
BEGIN
    texts = ["aaabbbbbcc", "abcd", "aabbaa"]
    FOR text IN texts DO
        IF LENGTH(text) == 0 THEN
            encoded = ""
        ELSE
            encoded = ""
            count = 1
            FOR i FROM 1 TO LENGTH(text) - 1 DO
                IF text[i] == text[i - 1] THEN
                    count = count + 1
                ELSE
                    encoded = encoded + text[i - 1] + STR(count)
                    count = 1
                END IF
            END FOR
            encoded = encoded + text[LENGTH(text) - 1] + STR(count)
        END IF
        PRINT text, encoded, LENGTH(text), LENGTH(encoded)
    END FOR
END
```

## Test Cases & Expected Output
* **Test Case 1 (`"aaabbbbbcc"`):** Encodes to `"a3b5c2"` (`6` chars vs `10` chars -> beneficial).
* **Test Case 2 (`"abcd"` or `"aabbcc"`):** Encodes to `"a1b1c1d1"` (`8` chars vs `4` chars) or `"a2b2c2"` (`6` chars vs `6` chars) -> not beneficial.

```text
Orig: 'aaabbbbbcc' (len=10) | Enc: 'a3b5c2' (len=6) | Beneficial: True
Orig: 'abcd' (len=4) | Enc: 'a1b1c1d1' (len=8) | Beneficial: False
Orig: 'aabbcc' (len=6) | Enc: 'a2b2c2' (len=6) | Beneficial: False
Orig: '' (len=0) | Enc: '' (len=0) | Beneficial: False
```

## Conclusion
Run-length encoding shrinks strings with long contiguous repeats, while short or non-repeating text can expand if every character gets a count suffix.
