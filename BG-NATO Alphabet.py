# NATO Phonetic Alphabet Guide
# Version: 1.0
# Date: 24-NOV-2020
# Developed by: Billy Gaskin
# Gasware Enterprises
#
# Reference: https://en.wikipedia.org/wiki/NATO_phonetic_alphabet

print("**\n** NATO Phonetic Alphabet Guide", "\n**\n")

# Load Dictionary containing the NATO Phonetic Alphabet

NATO_Alphabet = {}
NATO_Alphabet["A"]="Alfa"
NATO_Alphabet["B"]="Bravo"
NATO_Alphabet["C"]="Charlie"
NATO_Alphabet["D"]="Delta"
NATO_Alphabet["E"]="Echo"
NATO_Alphabet["F"]="Foxtrot"
NATO_Alphabet["G"]="Golf"
NATO_Alphabet["H"]="Hotel"
NATO_Alphabet["I"]="India"
NATO_Alphabet["Z"]="Zulu"
NATO_Alphabet["J"]="Juliett"
NATO_Alphabet["K"]="Kilo"
NATO_Alphabet["L"]="Lima"
NATO_Alphabet["M"]="Mike"
NATO_Alphabet["N"]="November"
NATO_Alphabet["O"]="Oscar"
NATO_Alphabet["P"]="Papa"
NATO_Alphabet["Q"]="Quebec"
NATO_Alphabet["R"]="Romeo"
NATO_Alphabet["S"]="Sierra"
NATO_Alphabet["T"]="Tango"
NATO_Alphabet["U"]="Uniform"
NATO_Alphabet["V"]="Victor"
NATO_Alphabet["W"]="Whiskey"
NATO_Alphabet["X"]="Xray"
NATO_Alphabet["Y"]="Yankee"
NATO_Alphabet["Z"]="Zulu"
NATO_Alphabet["0"]="Zero"
NATO_Alphabet["1"]="One"
NATO_Alphabet["2"]="Two"
NATO_Alphabet["3"]="Three"
NATO_Alphabet["4"]="Four"
NATO_Alphabet["5"]="Five"
NATO_Alphabet["6"]="Six"
NATO_Alphabet["7"]="Seven"
NATO_Alphabet["8"]="Eight"
NATO_Alphabet["9"]="Niner"

# Accept input and translate to NATO Alphabet

line_of_text=input("Enter text to translate:")
print("Translating: ",line_of_text.upper())
print()
i=1
allow_one_blank=False

for character in line_of_text:
    try:
        print(i,"(",character.upper(),")","...",NATO_Alphabet[character.upper()])
        i +=1
        allow_one_blank=True
    except(KeyError, ValueError):
        if character.upper()==" ":
            if allow_one_blank:
                print()
                allow_one_blank=False

input("\nCompleted! Press Enter to quit...")

# End of program...



