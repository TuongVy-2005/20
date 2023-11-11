human_years=float(input())
if human_years<0:
    print('Invalid')
elif human_years<2:
    dog_years=human_years*10.5
else:
    dog_years=human_years*10.5+(human_years-2)*4
print(human_years, 'human years are equal to', dog_years,'dog years')