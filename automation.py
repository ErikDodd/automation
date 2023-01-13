import re

# use context manager to open and read the file
with open("./potential_contacts.txt", "r") as f:
    text_from_potential_contacts = f.read()

    #print(text_from_potential_contacts)

    # Got this regex code from ChatGPT. Special thank you/attribution
    phone_regex_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

    # Find All phone numbers in potential contacts
    phone_numbers = re.findall(phone_regex_pattern, text_from_potential_contacts)

    # Check the total amount of phone numbers in the list = 112
    total_phone_numbers = len(phone_numbers)

    # Remove duplicates and prints the list of numbers
    phone_without_duplicates = list(set(phone_numbers))

    # Sort the phone numbers in Ascending Order
    sorted_phone_numbers = phone_without_duplicates.sort()

    # Check new total amount of phone numbers without duplicates = 100
    total_phone_without_duplicates = len(phone_without_duplicates)


    # Regex Email pattern. A special thank you/attribute to ChatGPT for providing the basis for this line of code
    email_regex_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # Find all the email addresses in potential_contacts
    email_addresses = re.findall(email_regex_pattern, text_from_potential_contacts)

    email_without_duplicates = list(set(email_addresses))

    total_email_without_duplicates = len(email_without_duplicates)

    # Check the total amount of email addresses = 115
    total_number_of_email = len(email_addresses)

with open("phone_numbers.txt", "w") as f:
    for phone in phone_without_duplicates:
        f.write(phone + '\n')

with open('emails.txt', 'w') as f:
    for email in email_without_duplicates:
        f.write(email + '\n')



    # Print Statements for checking phone numbers and emails
    # print(phone_numbers)
    #print(f"Total phone numbers with duplicates: {total_phone_numbers}")
    #print(f"Total phone numbers without duplicates: {total_phone_without_duplicates}")
    #print(phone_without_duplicates)
    # print(f"email_addresses)
    #print(f"Total number of email with duplicates: {total_number_of_email}")
    #print(f"Total number of email without duplicates: {total_email_without_duplicates}")

