##################### Hard Starting Project ######################
from datetime import datetime
import pandas
import random
import smtplib

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

today = datetime.now()
today_tuple = (today.month, today.day)

#info
my_email = "folafako05@gmail.com"
password = "icsegsnoukdsxwwd"

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }


data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row['month'], data_row['day']):data_row for (index, data_row) in data.iterrows()}
#print(birthday_dict)

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
if (today_tuple) in birthday_dict:
    #print(birthday_dict[today_tuple]["name"])
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_dict[today_tuple]["name"])
        print(content)
        #file.write(content)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # encrypts the content the mail
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_dict[today_tuple]["email"],
                                msg=f"Subject:Happy Birthday!\n\n{content}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp



# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



