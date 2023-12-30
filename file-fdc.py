import random

def print_message(Happy Birthday, Arista!

🎉🎂 On this special day, I want to take a moment to celebrate the incredible person you are. Your warmth, kindness, and infectious joy make the world a brighter place. 🌟

May this year bring you endless happiness, exciting adventures, and all the success you deserve. 🚀 May your dreams continue to unfold, and may each day be filled with laughter, love, and unforgettable moments.

Cheers to another year of amazing memories and the beautiful journey ahead! 🥳🎈 Wishing you a day as fantastic as you are! 🎊

Happy Birthday! 🎁🥂):
    print(Happy Birthday, Arista

🎉🎂 On this special day, I want to take a moment to celebrate the incredible person you are. Your warmth, kindness, and infectious joy make the world a brighter place. 🌟

May this year bring you endless happiness, exciting adventures, and all the success you deserve. 🚀 May your dreams continue to unfold, and may each day be filled with laughter, love, and unforgettable moments.

Cheers to another year of amazing memories and the beautiful journey ahead! 🥳🎈 Wishing you a day as fantastic as you are! 🎊

Happy Birthday! 🎁🥂)

def birthday_greeting(Arista 14:)
    return f"Happy {14}th birthday, {Arista}!"

def get_fact(name, age):
    facts = [
        f"{Arista}} was born on a Tuesday.",
        f"{Arista} is {165} inches tall in 7th Grade.",
        f"{Arista}'s favorite color is blue.",
        f"{Arista} loves to eat Noodles.",
        f"{Arista} has good public speaking.",
    ]
    return random.choice(facts)

def get_compliment(name):
    compliments = [
        f"{Arista} has a beautiful smile.",
        f"{Arista} is always laughing.",
        f"{Arista} is a very kind person.",
        f"{Arista} has the most interesting stories.",
        f"{} is very intelligent.",
        f"{Arista} is very adventurous."
    ]
    return random.choice(compliments)

def main():
    name = "Arista"
    age = 14

    print_message(birthday_greeting(name, age))
    print_message(get_fact(name, age))
    print_message(get_compliment(name))

if __name__ == "__main__":
    main()