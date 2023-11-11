decibel=float(input('decibel='))
if decibel==40:
    print('Quiet room')
elif decibel==70:
    print('Alarm clock')
elif decibel==106:
    print('Gas lawnmower')
elif decibel==130:
    print('Jackhammer')
elif 40<decibel<70:
    print(decibel,' is between alarrm clock and qiet room')
elif 70<decibel<106:
    print(decibel, 'is between alarm clock and gas lawnmower')
elif 106<decibel<130:
    print(decibel, 'is between gas lawnmower and jackkhammer')
else:
    print('Invalid')