import time,random,male,female
print("============================")
print("|  #####  #######  #    #  |")
print("|  #      #  #  #  ##   #  |")
print("|  #      #  #  #  # #  #  |")
print("|  #      #  #  #  #  # #  |")
print("|  #      #  #  #  #   ##  |")
print("|  #####  #  #  #  #    #  |")
print("============================")
print()
print("欢迎使用<取名>")
gender=input("性别[ 男/女 ]: ")
f_name=input("姓: ")
while True:
    if gender=="男":
        x=random.randint(1,100)
        if x<=13:
            s_name=str(random.choice(male.one))
        elif x<=29:
            s_name=str(random.choice(male.two))
        elif x<=72:
            s_name=str(random.choice(male.one)+random.choice(male.two))
        else:
            s_name=str(random.choice(male.two)+random.choice(male.one))
        print("姓名: "+f_name+s_name)
        input("要不要重新选一个？")
    if gender=="女":
        x=random.randint(1,100)
        if x<=18:
            s_name=str(random.choice(female.one))
        elif x<=27:
            s_name=str(random.choice(female.two))
        elif x<=32:
            s_name=str(random.choice(female.three))
        elif x<=54:
            s_name=str(random.choice(female.one)+random.choice(female.two))
        elif x<=69:
            s_name=str(random.choice(female.two)+random.choice(female.three))
        else:
            s_name=str(random.choice(female.two)+random.choice(female.one))
        print("姓名: "+f_name+s_name)
        input("要不要重新选一个？")
        