note_input = input("Enter a note:")
note_letter = note_input[0]
octave_number = int(note_input[1])

if note_letter == "C":
    frequency = 261.63 * (2 ** (4 - octave_number))
elif note_letter == "D":
    frequency = 293.66 * (2 ** (4 - octave_number))
elif note_letter == "E":
    frequency = 329.63 * (2 ** (4 - octave_number))
elif note_letter == "F":
    frequency = 349.23 * (2 ** (4 - octave_number))
elif note_letter == "G":
    frequency = 392.00 * (2 **( 4 - octave_number))
elif note_letter == "A":
    frequency = 440.00 * (2 ** (4 - octave_number))
elif note_letter == "B":
    frequency = 493.88 * (2 ** (4 - octave_number))
else:
    print("Error")
    frequency = None

if frequency is not None:
    print(f"The frequency of {note_input} is {frequency} Hz")