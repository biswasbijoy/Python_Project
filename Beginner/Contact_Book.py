#Python Project. Beginner Level. Level 1
names = []
phone_numbers = []
emails = []
tot_contact = int(input("Enter the number of contact for save: "))
for i in range (tot_contact) :
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    names.append(name)
    phone_numbers.append(phone)
    emails.append(email)

print("\nName \t\t Phone \t\t\t\t Email")
for i in range(tot_contact) :
    print("{} \t\t {} \t\t {}".format(names[i], phone_numbers[i], emails[i]))

search = input("\nSearch here: ")

if search in names:
    index = names.index(search)
    phone = phone_numbers[index]
    email = emails[index]
    print(f'Search result: Name: {search}, Phone Number: {phone}, Email: {email}')
elif search in phone_numbers:
    index = phone_numbers.index(search)
    name = names[index]
    email = emails[index]
    print(f'Search result: Name: {name}, Phone Number: {search}, Email: {email}')
elif search in emails:
        index = emails.index(search)
        name = names[index]
        phone = phone_numbers[index]
        print(f'Search result: Name: {name}, Phone Number: {phone}, Email: {search}')
else:
    print("Search result: Sorry! No record found.")