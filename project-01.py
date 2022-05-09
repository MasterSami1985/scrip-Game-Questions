import sys
name = input("Enter Your Name: ")

def menu(): #Def Menu
    print(f"===||Welcome {[name]} To A Knowledge Game||===")
    print("=============================================")
    category =int(input("[1]-Sport\n[2]-Geography\n[#]Choose One: "))
    score = 0 # Counter 

    if category == 2 :#Back To menu or Exit
        print("Comming soon")
        rep=input("if you want back menu?type Yes or exist type no: ")
        if rep =="no":
            print("Thank you for use Game")
            sys.exit()
        return menu()
    
    if category == 1:#Questions List
        print("=============================================")
        questions=[["[A]-Where was the first World Cup soccer tournament held in 1930?:\n[1]-Paraguay\n[2]-Uruguay\n[3]-Brazil"],
                   ["[B]-What is the first team to win the World Cup twice in a row?:\n[1]-Argentina\n[2]-Brazil\n[3]-Italy"],
                   ["[C]-Where was the first FIFA Confederations Cup held in 1992?:\n[1]-Saudi Arabia\n[2]-England\n[3]-France"],
                   ["[D]-When was the first car race held in France?:\n[1]-1896AD\n[2]-1894AD\n[3]-1892AD"],
                   ["[E]-What is the color of the flag that if it is raised in a race car, it means that attention should be paid to the presence of a car behind it?:\n[1]-yellow\n[2]-red\n[3]-blue"],
                   ["[F]-In which city was the first Olympic Games held in Asia, which was in 1964?:\n[1]-Tokyo\n[2]-Beijing\n[3]-Sydney"]]
        #Question One
        print(' '.join(questions[0]))
        opt=int(input("Enter one: "))
        
        
        if opt == 2:
            score += 1
            print(f"Correct answer Uruguay : {score}")      
        else:
            print(f"wrong answer {score}")
            
        #Question Twoo
        print(' '.join(questions[1]))
        opt=int(input("Enter one: "))
        if opt == 2:
            score += 1
            print(f"Correct answer Brazil : {score}")   
        else:
            print(f"wrong answer {score}")
            
        #Question Three
        print(' '.join(questions[2]))
        opt=int(input("Enter one: "))
        if opt == 1:
            score += 1
            print(f"Correct answer Saudi Arabia : {score}")       
        else:
            print(f"wrong answer {score}")



        #Question Four
        print(' '.join(questions[3]))
        opt=int(input("Enter one: "))
        if opt == 2:
            score += 1
            print(f"Correct answer 1894AD : {score}")       
        else:
            print(f"wrong answer {score}")



        #Question Five
        print(' '.join(questions[4]))
        opt=int(input("Enter one: "))
        if opt == 3:
            score += 1
            print(f"Correct answer 1894AD : {score}")       
        else:
            print(f"wrong answer {score}")


        #Question six
        print(' '.join(questions[5]))
        opt=int(input("Enter one: "))
        if opt == 1:
            score += 1
            print(f"Correct answer 1894AD : {score}")       
        else:
            print(f"wrong answer {score}")

menu()
