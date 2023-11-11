d=int(input("Day:"))
m=input("Month:")
if d==1:
    if m=="January":print("New year's day")
    elif m=="July":print("Canada day")
    elif m!="July" and m!="January":print("Wrong month, but in this day have some holiday like:","\n New year's day in January","\n Canada day in July")  
elif d!=1:
    if m=="January":print("Wrong day, but in this month have a New year's day at the 1st day")
    elif m=="July":print("Wrong day, but in this month have a Canada day at the 1st day")
    elif d==25:
        if m=="December":print("Christmas day")
        elif m!="December":print("Wrong month, but in this day have a Christmas day")
    elif d!=25:
        if m=="December":print('Wrong day but in this month have a Chrismast day')
        else:print("Can't find any holiday")