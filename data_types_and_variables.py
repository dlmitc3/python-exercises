# 1

 rental_price = 3.0
 the_little_mermaid_days = 3
 brother_bear_days = 5
 hercules_days = 1
 total_days = the_little_mermaid_days + brother_bear_days + hercules_days
 print (total_days)
 amount_spent = total_days * rental_price
 print(amount_spent)
 print(f'Amount spent on Disney products was ${amount_spent}')

 # 2
 google_rate = 400
 amazon_rate = 380
 facebook_rate = 350

 google_hours = 6
 amazon_hours = 4
 facebook_hours = 10
 total_comp = (google_rate * google_hours) + (amazon_rate * amazon_hours) + (facebook_rate * facebook_hours)
 print(f'Total pay for the week is {total_comp}')

 # 3

class_has_room = True
schedule_has_room = False
student_can_enroll = class_has_room and schedule_has_room
print(f'Can the student enroll? \n {student_can_enroll}')

 # 4
 is_premium_member = True
 more_than_two_items = False
 offer_not_expired = True
 discount_valid = offer_not_expired and (is_premium_member or more_than_two_items)
 print('Is discount valid?')
 print(discount_valid)

 # Continue working in your data_types_and_variables.py file. 
 # Use the following code to follow the instructions below:
 username = 'codeup'
 password = 'notastrongpassword'
 password_is_long_enough = len(password) >= 5
 username_is_short_enough = len(username) <= 20
 username_and_password_are_different = username != password
 username_has_spaces = username != username.strip()
 password_has_spaces = password != password.strip()
 username_good = username_is_short_enough and username_and_password_are_different and not username_has_spaces
 password_good = password_is_long_enough and username_and_password_are_different and not password_has_spaces
 valid_credentials = username_good and password_good
 print('Username good?')
 print(username_good)
 print('password good?')
 print(password_good)
 print('credentials valid?')
 print(valid_credentials) 
