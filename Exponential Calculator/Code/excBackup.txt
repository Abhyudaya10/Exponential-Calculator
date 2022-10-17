import smtplib
from smtplib import SMTP
import os

def squares(number):
    number = number**2
    return number
def cube(number):
    number = number**3
    return number
def squares_root(number):
    number = number**(1/2)
    return number
def cube_root(number):
    number = number**(1/3)
    return number
def power(number,power):
    number = number**power
    return number

intro = """                                                                                                                                            
 .____                                            .              .          ___          .         
 /      _  .- \,___,   __.  , __     ___  , __   _/_   `   ___   |        .'   \   ___   |     ___ 
 |__.    \,'  |    \ .'   \ |'  `. .'   ` |'  `.  |    |  /   `  |        |       /   `  |   .'   `
 |       /\   |    | |    | |    | |----' |    |  |    | |    |  |        |      |    |  |   |     
 /----/ /  \  |`---'  `._.' /    | `.___, /    |  \__/ / `.__/| /\__       `.__, `.__/| /\__  `._.'
              \                                                                                    
         
                
                                                                                                             
"""
print(intro)
reps = 0
quit = False
q = input("Would you like to perform a operation?(ans in y or n) ; ")
satisfied = False
historyOfGivenSquareRoots = []
historyOfGivenCubeRoots = []
historyOfSquares = []
historyOfCubes = []
historyOfGivenSquares = []
historyOfSquareRoots = []
historyOfGivenCubes = []
historyOfCubeRoots = []
historyOfPower = []
historyOfPowerBase = []
while quit == False:
    while q == "y":
        
        satisfied == False
        while satisfied == False:
            ready = input("Ready?(ans in y or n) ")
            if ready == "y":
                numinput = int(input("Number : "))
                operation = input("Operation : ")

                if operation == "square":
                    result = squares(numinput)
                    print(f"Your answer is || {result} ||.")
                    q = input("Would you like to perform a operation?(ans in y or n) ; ")
                    reps +=1
                    historyOfGivenSquareRoots.append(numinput)
                    historyOfSquares.append(result)
                    
                elif operation == "cube":
                    result = cube(numinput)
                    print(f"Your answer is ||{result} ||.")
                    q = input("Would you like to perform a operation?(ans in y or n) ; ")
                    reps +=1
                    historyOfGivenCubeRoots.append(numinput)
                    historyOfCubes.append(result)

                elif operation == "square root":
                    result = squares_root(numinput)
                    print(f"Your answer is ||{result} ||.")
                    q = input("Would you like to perform a operation?(ans in y or n) ; ")
                    reps +=1
                    historyOfGivenSquares.append(numinput)
                    historyOfSquareRoots.append(result)

                elif operation == "cube root":
                    result = cube_root(numinput)
                    print(f"Your answer is || {result} ||.")
                    q = input("Would you like to perform a operation?(ans in y or n) ; ")
                    reps +=1
                    historyOfGivenCubes.append(numinput)
                    historyOfCubeRoots.append(result)

                elif operation == "power":
                    toThePower = int(input("To what number would you like to raise the power to?"))
                    result = power(numinput, toThePower)
                    print(f"The result is || {result} || .")
                    q = input("Would you like to perform a operation?(ans in y or n) ; ")
                    reps +=1
                    historyOfPowerBase.append(toThePower)
                    historyOfPower.append(result)

                    
                else:
                    print("Not valid operation sorry sorry")
                    break
            else:
                print("Ok:(")
                break
    else:
        userWantHistory = input("Would you like to access your operation history?(ans in yes or no) ;")
        if userWantHistory == "yes":
            square_history = ""
            cube_history = ""
            square_root_history = ""
            cube_root_history = ""
            exponent_history = ""
            to_address = input("Please enter your email address(Format - name.name@gmail.com): ")
            for key,value in zip(historyOfGivenSquareRoots, historyOfSquares) :
                square_history = f"""
                _____________________________________
                This is SquareRoot to Square history;
                Root - {key} , Square - {value}
                _____________________________________
                """
                print(square_history)
                
                

            for key,value in zip(historyOfGivenCubeRoots, historyOfCubes) :
                cube_history = f"""
                _________________________________
                This is CubeRoot to Cube history;
                Root - {key} , Cube - {value}
                _________________________________
                """
                print(cube_history)
                
                
            
            for key,value in zip(historyOfGivenSquares, historyOfSquareRoots) :
                square_root_history = f"""
                ____________________________________
                This is Square to SquareRoot history;
                Square - {key} , Root - {value}
                ____________________________________
                """
                print(square_root_history)
                
               

            for key,value in zip(historyOfGivenCubes, historyOfCubeRoots) :
                cube_root_history = f"""
                _________________________________
                This is Cube to CubeRoot history;
                Cube - {key} , Root - {value}
                _________________________________
                """
                print(cube_root_history)
                
            for key,value in zip (historyOfPowerBase, historyOfPower):
                exponent_history = f"""
                _______________________________
                This is the Exponent history;
                Base - {key} , Result - {value}
                _______________________________
               """
                print(exponent_history)

        from_address = os.environ.get("emial_addr")
        subject = "Operation history"
        body = f"""
        {square_history}
        {cube_history}
        {square_root_history}
        {cube_root_history}
        {exponent_history}
        """
        
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        # start TLS for security
        s.starttls()
        
        # Authentication
        s.login("expo.calc@gmail.com", "taqweudbwimffggc")
        
        # message to be sent
        msg = f"Subject: {subject}\n\n{body}"
      
        
        # sending the mail
        s.sendmail("expo.calc@gmail.com", to_address, msg)
        
        # terminating the session
        s.quit()       
        wantQuit = input("Would you like to quit")
        if wantQuit == "yes":
            quit = True
            break 
        else:
            continue

