
import random 


def query_user():
    while  True:

        query = input("Enter a number that falls between 1 and 10 ")



                # Cast the type to integer to support numeric data type

        try:
            guesser = int(query)
            if guesser < 1 or guesser > 10:
                raise ValueError("Incorrect Range of value")
        except ValueError as err:


            print("Wrong Input of {} ".format(err))
        else:
            return guesser               


        #function to genrate a random number



        # guessing engine
def console_input(number):

    num = number
    attempts = 0

    while True:
        guesser = query_user()

        if guesser < num:
            print("The correct value is higher! ")
            attempts += 1

        elif guesser > num:
            print("The correct value is lower! ")
            attempts += 1

        elif guesser == num:
            print("guessed correct answer ")
            attempts += 1
            return attempts

def random_num():



    num =  random.randint(1,10)
    if num == 0:
        num += 1
    return num


def start_game():





    print("""----Welcome to The Guessing Game ------ Hints


                            When the program starts, we want to:
                            ------------------------------------
                            1. Display an intro/welcome message to the player.
                            2. Store a random number as the answer/solution.
                            3. Continuously prompt the player for a guess.
                            a. If the guess greater than the solution, display to the player "It's lower".
                            b. If the guess is less than the solution, display to the player "It's higher".

                            4. Once the guess is correct, stop looping, inform the user they "Got it"
                            and show how many attempts it took them to get the correct number.
                            5. Let the player know the game is ending, or something that indicates the game is over.

                            ( You can add more features/enhancements if you'd like to. )
                            """)


    max_score = 0
    present_score = 0
    num = random_num()

               
    while True:




        attempts = console_input(num)
        present_score = attempts
        print("You have {} total of attempts".format(attempts))

        if max_score == 0:

            max_score = present_score

        elif present_score < max_score:
            max_score = present_score

        while True:
            reset = input("Would you like to replay? , Y/N? ")
            if reset.lower() == 'y':
                print("Randomizing fresh number set ")
                num = random_num()
                print("your max score is {} ".format(max_score))
                break

            elif reset.lower() == 'n':
                print("Thanks,GoodBye ")
                break

            else:
                print("Try again! ")
                continue

        if reset == 'n':
            break

        

if __name__ == '__main__':
    start_game()



                
                                    


                                    


                                        

                                        
                                            
                                            
                                            
                                            

                                        
                                            
                                            

                                        
                                            
                                            


                                        
                                            
                                                

        

    



        
    


    


 




















                                                

       

        























































        


       
