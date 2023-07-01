import random

min_num = 1
max_num = 1024

print("1dan 1024gacha son oylang men topaman")
input("O'yladingizmi...")

# Raqamni taxmin qilish uchun qator
guesses = 0
while True:
    # Minimal va maksimal qiymatlar oraasidagi tahmin
    guess = (min_num + max_num) // 2
    guesses += 1
    
    # Taxmin tog'ri yoki notog'riligini topuvchi 
    response = input("Bu son tog'rimi " + str(guess) + "? (y/n): ")
    
    if response == 'y':
        print("Men sizni oylagan soningizni ", guesses, "urinishda topdim!")
        input("Siz bilan oynaganimdan hursantman...")
        break
    elif response == 'n':
        # Javobga qarab taxmin doirasini qisqartiruvchi code
        response = input("Sizning oylagan soningiz " + str(guess) + "dan katami yoki kichik? (h\l): ")
        if response == 'h':
            min_num = guess + 1
        elif response == 'l':
            max_num = guess - 1
