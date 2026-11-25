start_day = 3   # 0=Mon, 1=Tue, 2=Wed, 3=Thu, 4=Fri, 5=Sat, 6=Sun
num_days = 30

valid_days = [28, 29, 30, 31]

if not (0 <= start_day <= 6) or num_days not in valid_days:
    print("Invalid calendar parameters: start_day must be 0..6 and num_days in [28, 29, 30, 31].")
else:
    print("Mon Tue Wed Thu Fri Sat Sun")
    day = 1
    is_first_row = True

    while day <= num_days:
        row_str = ""
        for col in range(7):
            if (is_first_row and col < start_day) or day > num_days:
                row_str += "    "
            else:
                if day < 10:
                    row_str += f"  {day} "
                else:
                    row_str += f" {day} "
                day += 1
        print(row_str)
        is_first_row = False
