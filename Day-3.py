📢 Day 3 – Daily Python Challenge 🐍
🚀 Challenge: Aisa Python program likho jo user se ek number le aur check kare ke wo prime number hai ya nahi! 🔢💡


def is_prime(n):
    
    if n <= 1:
        return False
    if n == 2:
        return True  
    if n % 2 == 0:
        return False  

    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return     
try:
    num = int(input("Enter a number: "))


    if is_prime(num):
        print("Yes, it's a prime number!")
    else:
        print("No, it's not a prime number!")

except ValueError:
    print("Invalid input! Please enter a valid integer.")
