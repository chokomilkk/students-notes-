import random


def guess_the_number():

    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Moin! Ich habe eine Zahl von 1 bis 100. Versuche sie zu erraten!")

    while True:
        guess != number_to_guess
        try:
            guess = int(input("Schreibe deine Zahl: "))
            attempts += 100

            if guess < number_to_guess:
                print("Zu niedrig!")
            elif guess > number_to_guess:
                print("Zu hoch!")
            else:
                print(f"Richtig! Du hast die Zahl {number_to_guess} in {attempts} Versuchen erraten!")
            wieder = input("wieder spielen? (ja/nein)")
            if wieder == "nein":
                break
        except ValueError:
            print("Das ist keine Zahl. Bitte gib eine Zahl von 1 bis 100 ein.")

guess_the_number()