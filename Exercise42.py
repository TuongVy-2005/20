frequency = float(input("Frequency:"))
if 260.63<=frequency<= 262.63:
    print ("Note of Frequency is C4")
elif 292.66<=frequency<=294.66:
    print ("Note of Frequency is D4")
elif 328.63<=frequency<=330.63:
    print ("Note of Frequency is E4")
elif 348.23<=frequency<=350.23:
    print ("Note of Frequency is F4")
elif 391.00<=frequency<=393.00:
    print ("Note of Frequency is G4")
elif 439.00<=frequency<=441.00:
    print ("Note of Frequency is A4")
elif 393.88<=frequency<=494.88:
    print ("Note of Frequency is B4")
else:
    print("Not correspond to a known note")