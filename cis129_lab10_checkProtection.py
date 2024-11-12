#!/usr/bin/env python
# coding: utf-8

# Input a dollar amount from the user
amount = float(input("Enter a dollar amount: "))

# Format the amount with leading asterisks in a field of 10 characters
formatted_amount = f"{amount:*>10.2f}"

# Print the formatted amount
print(formatted_amount)

