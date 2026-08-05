Birthday = input("Enter your birthday (date month year): ")
currrent = "20-08-2026"
exact_age = int(currrent.split('-')[2]) - int(Birthday.split('-')[2])

print("exact age is:", exact_age)

birthday = input("Enter Birth Year: ")
current_year = 2026

exact_age = current_year - int(birthday)
print("exact age is:", exact_age)