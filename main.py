from user import User

user1 = User('Adam Jones', 'adamjones@example.com')
user2 = User('Tim Randolf', 'randolftim@example.com')
user3 = User('Hazel May', 'bestdog@example.com')

user1.make_deposit(900).make_deposit(50).make_deposit(5).make_withdraw(300).display_user_balance().interest()
user2.make_deposit(300).make_deposit(500).make_withdraw(100).make_withdraw(200).display_user_balance().interest()
user3.make_deposit(100).make_withdraw(90).make_withdraw(5).make_withdraw(10).display_user_balance().interest()