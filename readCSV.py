import csv
import emtmp

email_list = []
with open('contacts.csv', 'r', encoding='utf8')as csv_file:
    contacts = csv.DictReader(csv_file)
    for contact in contacts:
        email = contact['Email']
        if email:
            info = {'Name': contact['First Name'], 'Email': email}
            if info not in email_list:
                email_list.append(info)

#
# with open('contacts_clean.csv',mode='w',encoding='utf8')as csv_file:
#     fieldnames = ['Names','Email']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
    for i, e in enumerate(email_list):
        print(i, e)
        emtmp.send_email(e[1])
