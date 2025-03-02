# 📢 Day 6 – Daily Python Challenge 🐍
# 🚀 Challenge:
# Aisa Python program likhna hai jo user se ek integer number lega aur uska binary (0s aur 1s) me conversion karega,
# phir check karega ke ye palindrome hai ya nahi! 🔄✨



def is_palindrome(s):
    return s == s[::-1]

def main():
    # User se integer input lena
    num = int(input("Ek integer number daalein: "))
    
    # Number ka binary conversion
    binary_representation = bin(num)[2:]  # '0b' prefix ko hataana
    
    # Palindrome check karna
    if is_palindrome(binary_representation):
        print(f"Binary: {binary_representation}\nOutput: Palindrome ✅")
    else:
        print(f"Binary: {binary_representation}\nOutput: Not a Palindrome ❌")

if __name__ == "__main__":
    main()