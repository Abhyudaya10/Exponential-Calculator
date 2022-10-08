import math
intro = """                                                                                                                                            
 .____                                            .              .          ___          .         
 /      _  .- \,___,   __.  , __     ___  , __   _/_   `   ___   |        .'   \   ___   |     ___ 
 |__.    \,'  |    \ .'   \ |'  `. .'   ` |'  `.  |    |  /   `  |        |       /   `  |   .'   `
 |       /\   |    | |    | |    | |----' |    |  |    | |    |  |        |      |    |  |   |     
 /----/ /  \  |`---'  `._.' /    | `.___, /    |  \__/ / `.__/| /\__       `.__, `.__/| /\__  `._.'
              \                                                                                    
         
                                                                                                             
"""
print(intro)
q = input("Would you like to perform a operation?(ans in yes or no) ; ")
quit = False

satisfied = False
reps = 0
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
    while q == "yes":
        
        satisfied == False
        while satisfied == False:
            ready = input("Ready?(ans in yes or no) ")
            if ready == "yes":
                number = int(input("Number(type a int or a float, no strings!): "))
                operation = input("Operation (square, cube, square root, cube root,power): ")

                if operation == "square":
                    result = number**2
                    print(f"Your answer is || {result} ||.")
                    q = input("Would you like to perform a operation?(ans in yes or no) ; ")
                    reps +=1
                    historyOfGivenSquareRoots.append(number)
                    historyOfSquares.append(result)
                    
                elif operation == "cube":
                    result = number**3
                    print(f"Your answer is ||{result} ||.")
                    q = input("Would you like to perform a operation?(ans in yes or no) ; ")
                    reps +=1
                    historyOfGivenCubeRoots.append(number)
                    historyOfCubes.append(result)

                elif operation == "square root":
                    result = math.sqrt(number)
                    print(f"Your answer is ||{result} ||.")
                    q = input("Would you like to perform a operation?(ans in yes or no) ; ")
                    reps +=1
                    historyOfGivenSquares.append(number)
                    historyOfSquareRoots.append(result)

                elif operation == "cube root":
                    result = number** (1./3.)
                    print(f"Your answer is || {result} ||.")
                    q = input("Would you like to perform a operation?(ans in yes or no) ; ")
                    reps +=1
                    historyOfGivenCubes.append(number)
                    historyOfCubeRoots.append(result)

                elif operation == "power":
                    toThePower = int(input("To what number would you like to raise the power to?"))
                    result = number ** toThePower
                    print(f"The result is || {result} || .")
                    q = input("Would you like to perform a operation?(ans in yes or no) ; ")
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
            for key,value in zip(historyOfGivenSquareRoots, historyOfSquares) :
                print(f"""
                _____________________________________
                This is SquareRoot to Square history;
                Root - {key} , Square - {value}
                _____________________________________
                """)

            for key,value in zip(historyOfGivenCubeRoots, historyOfCubes) :
                print(f"""
                _________________________________
                This is CubeRoot to Cube history;
                Root - {key} , Cube - {value}
                _________________________________
                """)
            
            for key,value in zip(historyOfGivenSquares, historyOfSquareRoots) :
                print(f"""
                ____________________________________
                This is Square to SquareRoot history;
                Square - {key} , Root - {value}
                ____________________________________
                """)

            for key,value in zip(historyOfGivenCubes, historyOfCubeRoots) :
                print(f"""
                _________________________________
                This is Cube to CubeRoot history;
                Cube - {key} , Root - {value}
                _________________________________
                """)
            
            for key,value in zip (historyOfPowerBase, historyOfPower):
                print(f"""
                _______________________________
                This is the Exponent history;
                Base - {key} , Result - {value}
                _______________________________
               """)
        wantQuit = input("Would you like to quit")
        if wantQuit == "yes":
            quit = True
            break 
        else:
            continue
           


