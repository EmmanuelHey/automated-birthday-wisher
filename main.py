import smtplib
import datetime as dt
import random

#info
my_email = "emmanuelfakunle44@gmail.com"
password = "zdagodtvlqendjhq"


#
# now = dt.datetime.now().weekday()
# if (now == 3):
#     with open("quotes.txt", "r") as file:
#         data = file.readlines()
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()  # encrypts the content the mail
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="tolufako06@gmail.com",
#                             msg=f"Subject:Monday Motivation\n\n"
#                                 f"{random.choice(data)}")
#
# #
#
# #connection.close()
#
#
# # date_of_birth = dt.datetime(year=2003, month=12, day=8)
# # print(date_of_birth.year)