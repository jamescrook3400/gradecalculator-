from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#def grade_calculator():
#Establishes acceptable grades
grades=('A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-')
responses = ('y','n')       

print("Welcome to the Hunter College High School semester GPA calculator! This GPA Calculator works exclusively with Hunter College High School, and is not guaranteed to reflect the system of any other school Hunter inputs each letter grade with the highest possible numerical grade it could be, and then averages it. If you failed a class, this GPA calculator will not work for you. This is because I don't know how Hunter factors in failed classes. I am working on an update to fix that. Follow all directions carefully. If you do not follow the directions, you will crash the program...code is finicky!")
answerinitial = input("Do you know your current semester gpa? [y/n] ")
if answerinitial not in responses:
    print("You did not enter an acceptable response")

if answerinitial == "y":
    avg = input("Enter it here, out of 100: ") 
else:
    #Calculates first grade
    firstclass = input("Which class should we start with? ")
    class1 = input("Enter your " + firstclass + " grade, use capital letters ONLY: " )

    #For special grades
    if class1 in grades:
        if class1 == 'A+':
            class1gradeint = 100.0
        elif class1 == 'D':
            class1gradeint = 67.0
        elif class1 == 'D-':
            class1gradeint = 65.0
        
        #For regular grades
        else:
        
            #For the ones place of the numerical grade
            if '+' in class1:
                class1last = 9.0
            elif '-' in class1:
                class1last = 2.0
            else:
                class1last = 6.0
        
            #For the tens place of the numerical grade
            if 'A' in class1:
                class1first = 90.0
            if 'B' in class1:
                class1first = 80.0
            if 'C' in class1:
                class1first = 70.0
            if 'D' in class1:
                class1first = 60.0
            
            #Calculates numerical grade
            class1gradeint = class1first + class1last
    
        #Presents numerical grade to the user
        class1grade = str(class1gradeint)
        print("Your " + firstclass + " grade is a " + class1grade + "/100.")
    
    #Deals with failed classes
    elif class1 == 'F':
        class1grade = "Fail"
        print("You failed " + firstclass + ". This program is not yet capable of calculating a GPA with an F in it.")
    
    
    #Deals with errors in the input
    else:
        print("You did not enter a proper grade. Please make sure you used capital letters. Restart and try again.")
    

    #Calculates second grade    
    secondclass = input("Which class should we do next? ")
    class2 = input("Enter your " + secondclass + " grade, use capital letters ONLY: " )

    #For special grades
    if class2 in grades:
        if class2 == 'A+':
            class2gradeint = 100.0
        elif class2 == 'D':
            class2gradeint = 67.0
        elif class2 == 'D-':
            class2gradeint = 65.0
        
        #For regular grades
        else:
        
            #For the ones place of the numerical grade        
            if '+' in class2:
                class2last = 9.0
            elif '-' in class2:
                class2last = 2.0
            else:
                class2last = 6.0
            
            #For the tens place of the numerical grade
            if 'A' in class2:
                class2first = 90.0
            if 'B' in class2:
                class2first = 80.0
            if 'C' in class2:
                class2first = 70.0
            if 'D' in class2:
                class2first = 60.0

            #Calculates numerical grade
            class2gradeint = class2first + class2last
        
        #Presents numerical grade to the user
        class2grade = str(class2gradeint)
        print("Your " + secondclass + " grade is a " + class2grade + "/100")
    
    #Deals with failed classes
    elif class2 == 'F':
        class2grade = "Fail"
        print("You failed " + firstclass + ". This program is not yet capable of calculating a GPA with an F in it.")
    
    
    #Deals with errors in the input
    else:
        print("You did not enter a proper grade. Please make sure you used capital letters. Restart and try again.")
    
    
    #Calculates third grade    
    thirdclass = input("Which class should we do next? ")
    class3 = input("Enter your " + thirdclass + " grade, use capital letters ONLY: " )

    #For special grades
    if class3 in grades:
        if class3 == 'A+':
            class3gradeint = 100.0
        elif class3 == 'D':
            class3gradeint = 67.0
        elif class3 == 'D-':
            class3gradeint = 65.0
        
        #For regular grades
        else:
        
            #For the ones place of the numerical grade        
            if '+' in class3:
                class3last = 9.0
            elif '-' in class3:
                class3last = 2.0
            else:
                class3last = 6.0
            
            #For the tens place of the numerical grade
            if 'A' in class3:
                class3first = 90.0
            if 'B' in class3:
                class3first = 80.0
            if 'C' in class3:
                class3first = 70.0
            if 'D' in class3:
                class3first = 60.0

            #Calculates numerical grade
            class3gradeint = class3first + class3last
        
        #Presents numerical grade to the user
        class3grade = str(class3gradeint)
        print("Your " + thirdclass + " grade is a " + class3grade + "/100")
    
    #Deals with failed classes
    elif class3 == 'F':
        class3grade = "Fail"
        print("You failed " + firstclass + ". This program is not yet capable of calculating a GPA with an F in it.")
    
    
    #Deals with errors in the input
    else:
        print("You did not enter a proper grade. Please make sure you used capital letters. Restart and try again.")  
    
            
    #Calculates fourth grade    
    fourthclass = input("Which class should we do next? ")
    class4 = input("Enter your " + fourthclass + " grade, use capital letters ONLY: " )

    #For special grades
    if class4 in grades:
        if class4 == 'A+':
            class4gradeint = 100.0
        elif class4 == 'D':
            class4gradeint = 67.0
        elif class4 == 'D-':
            class4gradeint = 65.0
        
        #For regular grades
        else:
        
            #For the ones place of the numerical grade        
            if '+' in class4:
                class4last = 9.0
            elif '-' in class4:
                class4last = 2.0
            else:
                class4last = 6.0
            
            #For the tens place of the numerical grade
            if 'A' in class4:
                class4first = 90.0
            if 'B' in class4:
                class4first = 80.0
            if 'C' in class4:
                class4first = 70.0
            if 'D' in class4:
                class4first = 60.0

            #Calculates numerical grade
            class4gradeint = class4first + class4last
        
        #Presents numerical grade to the user
        class4grade = str(class4gradeint)
        print("Your " + fourthclass + " grade is a " + class4grade + "/100")
    
    #Deals with failed classes
    elif class4 == 'F':
        class4grade = "Fail"
        print("You failed " + firstclass + ". This program is not yet capable of calculating a GPA with an F in it.")
    
    
    #Deals with errors in the input
    else:
        print("You did not enter a proper grade. Please make sure you used capital letters. Restart and try again.")
    
    
    #Calculates fifth grade    
    fifthclass = input("Which class should we do next? ")
    class5 = input("Enter your " + fifthclass + " grade, use capital letters ONLY: " )

    #For special grades
    if class5 in grades:
        if class5 == 'A+':
            class5gradeint = 100.0
        elif class5 == 'D':
            class5gradeint = 67.0
        elif class5 == 'D-':
            class5gradeint = 65.0
        
        #For regular grades
        else:
        
            #For the ones place of the numerical grade        
            if '+' in class5:
                class5last = 9.0
            elif '-' in class5:
                class5last = 2.0
            else:
                class5last = 6.0
            
            #For the tens place of the numerical grade
            if 'A' in class5:
                class5first = 90.0
            if 'B' in class5:
                class5first = 80.0
            if 'C' in class5:
                class5first = 70.0
            if 'D' in class5:
                class5first = 60.0

            #Calculates numerical grade
            class5gradeint = class5first + class5last
        
        #Presents numerical grade to the user
        class5grade = str(class5gradeint)
        print("Your " + fifthclass + " grade is a " + class5grade + "/100")
    
    #Deals with failed classes
    elif class5 == 'F':
        class5grade = "Fail"
        print("You failed " + firstclass + ". This program is not yet capable of calculating a GPA with an F in it.")
    
    
    #Deals with errors in the input
    else:
        print("You did not enter a proper grade. Please make sure you used capital letters. Restart and try again.")
    
    
    #Establishes if the user has a sixth class 
    response = input("Do you have a sixth class? [y/n] ")
    if response not in responses:
        print("You did not enter an acceptable response")
    
    if response == 'n':
        pass
    if response == 'y':
    
        #Calculates sixth grade    
        sixthclass = input("What is your sixth class? ")
        class6 = input("Enter your " + sixthclass + " grade, use capital letters ONLY: " )
    
        #For special grades
        if class6 in grades:
            if class6 == 'A+':
                class6gradeint = 100.0
            elif class6 == 'D':
                class6gradeint = 67.0
            elif class6 == 'D-':
                class6gradeint = 65.0
            
            #For regular grades
            else:
            
                #For the ones place of the numerical grade        
                if '+' in class6:
                    class6last = 9.0
                elif '-' in class6:
                    class6last = 2.0
                else:
                    class6last = 6.0
                
                #For the tens place of the numerical grade
                if 'A' in class6:
                    class6first = 90.0
                if 'B' in class6:
                    class6first = 80.0
                if 'C' in class6:
                    class6first = 70.0
                if 'D' in class6:
                    class6first = 60.0
    
                #Calculates numerical grade
                class6gradeint = class6first + class6last
            
            #Presents numerical grade to the user
            class6grade = str(class6gradeint)
            print("Your " + sixthclass + " grade is a " + class6grade + "/100")
        
        #Deals with failed classes
        elif class6 == 'F':
            class6grade = "Fail"
            print("You failed " + firstclass + ". This program is not yet capable of calculating a GPA with an F in it.")
            python = sys.executable
            os.execl(python, python, * sys.argv)
        
        #Deals with errors in the input
        else:
            print("You did not enter a proper grade. Please make sure you used capital letters. Restart and try again.")
            python = sys.executable
            os.execl(python, python, * sys.argv)

    #Calculates average and returns to the user
    if response == 'y':
        total = class1gradeint + class2gradeint + class3gradeint + class4gradeint + class5gradeint + class6gradeint
        avgint = total / 6
    else:
        total = class1gradeint + class2gradeint + class3gradeint + class4gradeint + class5gradeint 
        avgint = total / 5
    avg = str(avgint)
    print("Congratulations! Your average for this semester is: " + avg)

#Begins process of calculating a goal GPA
newresponse = input("Would you like to know what grades you need to get to change your average? [y/n] ")
if newresponse not in responses:
    print("You did not enter an acceptable response")


#Obtains necessary info    
if newresponse == 'y':
    goalgrade = input("Please enter your goal average, out of 100: ")
    naviance = input("Please enter your current GPA on Naviance: ")
    gradelevels = ('1', '2', '3', '4', '5')
    gradelevel = input("Please enter your current grade level. If you are in eighth grade, type '1', if you are in ninth grade,type '2', etc. ")
    if gradelevel == '0':
        print("Chill out, seven.")
    elif gradelevel not in gradelevels:
        print("This is not an acceptable grade level")
    
    
    #Does the math, presents it to the user
    else: 
        avgint = int(avg.split('.')[0])
        gradelevelint = int(gradelevel)
        navianceint = int(naviance.split('.')[0])
        goalgradeint = int(goalgrade.split('.')[0])
        almostavg = navianceint * (gradelevelint - 1)
        difference = (goalgradeint * gradelevelint) - almostavg
        differencestr = str(difference)
        if difference > 100:
            print("It is mathematically impossible for you to get a " + goalgrade + ". You would need a " + differencestr + " for the year to get that GPA.")
        else: 
            semester = input("Have you recieved second semester grades yet? [y/n] ")
            if semester not in responses:
                print("You did not enter an acceptable response")
            elif semester == 'n':
                sem2int = (difference * 2) - avgint 
                sem2 = str(sem2int)
                if sem2int > 100:
                    print("You need a " + sem2 + " for second semester in order to get a " + differencestr + " for the year, which would give you your goal gpa.",\
                    "But, of course, it is impossible to get a " + sem2 + " for the semester.") #Clarify what this is even saying my guy
                else:
                    print("You need a " + sem2 + " for second semester in order to get a " + differencestr + " for the year, which would give you your goal gpa.")
        
            #If the Naviance GPA includes this year's grades
            else:
                realalmostavg = navianceint * (gradelevelint)
                realdifference = (goalgradeint * (gradelevelint + 1)) - realalmostavg
                realdifferencestr = str(realdifference)
                if gradelevelint == 5:
                    print("You're a senior and Hunter has probably already updated your Naviance GPA. There is nothing you can do, I'm afraid.")
                if realdifference > 100:
                    print("It is likely that Hunter has already updated your Naviance GPA with this year's grades.",\
                    "That means it is mathematically impossible for you to get a " + goalgrade + ". You would need a " + realdifferencestr + " for next year to get that GPA.")
                else:
                    print("You need to get a " + realdifferencestr + " for next year in order to get a " + goalgrade + " for your final GPA.")
else:
    print("Thanks! Have a good day.")
        
        
#if __name__ == "__main__":
 #   app.run()