# 📢 Day 4 – Daily Python Challenge 🐍
# 🚀 Challenge:Write a Python program that converts numbers into words! 🔢➡️🔡

import inflect

def number_to_words(i):
    p = inflect.engine()
    return p.number_to_words(i).replace(",", "")

num1 = int(input("Enter Your Number: "))

print(f'Input: {num1}\nOutput: "{number_to_words(num1).title()}"')

