import random
import time

while True:

    print("""
▒█▀▀█ ▒█▀▀█ ░░ ▒█▀▀█ █▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ 
▒█░░░ ▒█░░░ ▀▀ ▒█░▄▄ █▀▀ █░░█ █▀▀ █▄▄▀ █▄▄█ ░░█░░ █░░█ █▄▄▀ 
▒█▄▄█ ▒█▄▄█ ░░ ▒█▄▄█ ▀▀▀ ▀░░▀ ▀▀▀ ▀░▀▀ ▀░░▀ ░░▀░░ ▀▀▀▀ ▀░▀▀
          """)

    adet = int(input("How Many Cards You Want: "))

    def generate_credit_card():
        first_digit = random.choice(['4', '5'])
        card_number = first_digit + ''.join(random.choices('0123456789', k=15))
        expiration_month = random.randint(1, 12)
        expiration_year = random.randint(2024, 2034)
        expiration_date = f"{expiration_month:02d}|{expiration_year}"
        cvv = ''.join(random.choices('0123456789', k=3))
        return card_number, expiration_date, cvv

    for _ in range(adet):
        card_number, expiration_date, cvv = generate_credit_card()
        print(f"{card_number}|{expiration_date}|{cvv}")

    choice = input("Do you want to generate more cards? (y/n): ")
    if choice.lower() != "y":
        print("Goodbye ! ")
        time.sleep(1)
        break