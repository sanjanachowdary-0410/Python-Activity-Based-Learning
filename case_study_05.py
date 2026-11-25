sample_passwords = [
    "Secure_99#xyz",
    "weak",
    "MyPassword!23",
    "AAAbbb1!@#",
    "NoSpecial123",
]

special_chars = "!@#$%^&*_-+"
forbidden_subs = ["password", "admin", "1234", "qwerty"]

for pwd in sample_passwords:
    failures = []

    if len(pwd) < 8:
        failures.append("Must be at least 8 characters long")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    max_run = 1
    current_run = 1

    for i in range(len(pwd)):
        ch = pwd[i]
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_digit = True
        elif ch in special_chars:
            has_special = True

        if i > 0 and pwd[i] == pwd[i - 1]:
            current_run += 1
            if current_run > max_run:
                max_run = current_run
        else:
            current_run = 1

    if not has_upper:
        failures.append("Missing uppercase letter")
    if not has_lower:
        failures.append("Missing lowercase letter")
    if not has_digit:
        failures.append("Missing digit")
    if not has_special:
        failures.append("Missing special character")
    if max_run > 2:
        failures.append(f"Too many repeated characters in a row ({max_run})")

    lower_pwd = pwd.lower()
    for sub in forbidden_subs:
        if sub in lower_pwd:
            failures.append(f"Contains forbidden substring '{sub}'")

    if len(failures) == 0:
        print(f"[PASS] {pwd}")
    else:
        print(f"[FAIL] {pwd}")
        for reason in failures:
            print(f"       - {reason}")
