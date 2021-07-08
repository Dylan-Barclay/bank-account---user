from user import User

user1 = User('Adam Jones', 'adamjones@example.com')

user1.make_deposit(900).make_deposit(50).make_deposit(5).make_withdraw(300).display_user_balance()