#!/usr/bin/python3

your_name = input("Введіть Ваше ім'я (українською): \n > ")

print("Ваше ім'я у вигляді послідовності байтів:")
print(your_name.encode('utf-8'))