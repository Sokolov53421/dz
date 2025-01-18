seconds = int(input("Enter nums🕛:"))

if 0 <= seconds < 8640000:
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    result_seconds = seconds % 60
    result_minutes = minutes % 60
    result_hours = hours % 24
    if days > 1:
        days_word = "days"
    else:
        days_word = "day"

    print(f"{days} {days_word} {result_hours:02d}:{result_minutes:02d}:{result_seconds:02d}")

else:
    print("Error")