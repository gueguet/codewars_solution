# https://www.codewars.com/kata/54b724efac3d5402db00065e

# MORSE_CODE is a dict implemented in the Codewars Kata

def decodeMorse(morse_code):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
