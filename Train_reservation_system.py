# for berth globals
LOWER_BERTH = 1
LOWER_BERTH_ARR = []
UPPER_BERTH = 1
UPPER_BERTH_ARR = []
MIDDLE_BERTH = 1
MIDDLE_BERTH_ARR = []

# for rac globals
RAC_TICKET = 1
RAC_TICKET_ARR = []

# for waiting globals
WAITING_TICKETS = 1
WAITING_TICKETS_ARR = []

# id maker Global
id = 1

# tickets details object
class Ticket:
    def __init__(self , id,  name , age , status ):
        self.id = id
        self.name = name
        self.age = age
        self.status = status


def book_tickets():
    global UPPER_BERTH , LOWER_BERTH , MIDDLE_BERTH ,RAC_TICKET ,WAITING_TICKETS , id
    name = input("enter your name")
    age = int(input("enter your age"))
    berth_preference = input("enter your berth U - upper  / L - lower / M - middle  ** "
                             "Note: if the request berth is not available then other options will be booker")

    # for berth of upper
    if(berth_preference =='U'):
        if( UPPER_BERTH != 0 ):
            print("Booked upper Berth ticket")
            new_ticket = Ticket(id, name, age , 'U')
            UPPER_BERTH_ARR.append(new_ticket)
            UPPER_BERTH -=1
        elif(LOWER_BERTH !=0 ):
            print("Due to unavailablity Booked Lower Berth ticket ")
            new_ticket = Ticket(id, name, age ,'L')
            LOWER_BERTH_ARR.append(new_ticket)
            LOWER_BERTH -=1
        elif(MIDDLE_BERTH != 0 ):
            print("Due to unavailablity Booked Middle Berth ticket ")
            new_ticket = Ticket(id, name, age , 'M')
            MIDDLE_BERTH_ARR.append(new_ticket)
            MIDDLE_BERTH -=1
        elif(RAC_TICKET != 0 ):
            print("Due to unavailablity Booked Rac Berth ticket ")
            new_ticket = Ticket(id, name, age , 'R')
            RAC_TICKET_ARR.append(new_ticket)
            RAC_TICKET -=1
        elif(WAITING_TICKETS != 0):
            print("Due to unavailablity Booked waiting Berth ticket ")
            new_ticket = Ticket(id, name, age , 'W')
            WAITING_TICKETS_ARR.append(new_ticket)
            WAITING_TICKETS -=1
        else:
            print("Sorry all the ticket have been booked")

    # for Middle Berth
    if (berth_preference == 'M'):

        if (MIDDLE_BERTH != 0):
            print("Booked lower Berth ticket")
            new_ticket = Ticket(id, name, age, "M")
            MIDDLE_BERTH_ARR.append(new_ticket)
            MIDDLE_BERTH -= 1
        elif (LOWER_BERTH != 0):
            print("Due to unavailablity Booked lower Berth ticket")
            new_ticket = Ticket(id, name, age , "L")
            LOWER_BERTH_ARR.append(new_ticket)
            LOWER_BERTH -= 1
        elif (UPPER_BERTH != 0):
            print("Due to unavailablity Booked upper Berth ticket")

            new_ticket = Ticket(id, name, age , 'U')

            UPPER_BERTH_ARR.append(new_ticket)
            UPPER_BERTH -= 1
        elif (RAC_TICKET != 0):
            print("Due to unavailablity Booked RAC Berth ticket")
            new_ticket = Ticket(id, name, age , 'R')
            RAC_TICKET_ARR.append(new_ticket)
            RAC_TICKET -= 1
        elif (WAITING_TICKETS != 0):
            print("Due to unavailablity Booked Waiting Berth ticket")
            new_ticket = Ticket(id, name, age , 'W')
            WAITING_TICKETS_ARR.append(new_ticket)
            WAITING_TICKETS -= 1
        else:
            print("Sorry all the ticket have been booked")

    # for Lower Berth
    if (berth_preference == 'L'):
        if (LOWER_BERTH != 0):
            print("Booked lower Berth ticket ")
            new_ticket = Ticket(id, name, age , 'L')
            LOWER_BERTH_ARR.append(new_ticket)
            LOWER_BERTH -= 1
        elif (MIDDLE_BERTH != 0):
            print("Due to unavailablity Booked Middle Berth ticket ")
            new_ticket = Ticket(id, name, age , 'M')
            MIDDLE_BERTH_ARR.append(new_ticket)
            MIDDLE_BERTH -= 1
        elif (UPPER_BERTH != 0):
            print("Due to unavailablity Booked upper Berth ticket ")
            new_ticket = Ticket(id, name, age , 'U')
            UPPER_BERTH_ARR.append(new_ticket)
            UPPER_BERTH -= 1
        elif (RAC_TICKET != 0):
            print("Due to unavailablity Booked Rac Berth ticket ")
            new_ticket = Ticket(id, name, age , 'R')
            RAC_TICKET_ARR.append(new_ticket)
            RAC_TICKET -= 1
        elif (WAITING_TICKETS != 0):
            print("Due to unavailablity Booked waiting Berth ticket ")
            new_ticket = Ticket(id, name, age , 'W')
            WAITING_TICKETS_ARR.append(new_ticket)
            WAITING_TICKETS -= 1
        else:
            print("Sorry all the ticket have been booked")

    id +=1



def cancel_ticket():
    global UPPER_BERTH , LOWER_BERTH , MIDDLE_BERTH ,RAC_TICKET , WAITING_TICKETS
    founder = False
    cancel_id = int(input("enter the cancel id"))
    cancel_status = input("enter the cancel status U - upper / L - lower / M - Middle / R - RAC / W - waiting ")
    if(cancel_status == 'U'):
        for i in range(len(UPPER_BERTH_ARR)):
            if(UPPER_BERTH_ARR[i].id == cancel_id):
                UPPER_BERTH_ARR.pop(i)
                founder = True
                UPPER_BERTH -=1

                if(len(RAC_TICKET_ARR) != 0):
                    rac_ticket = RAC_TICKET_ARR.pop(0)
                    UPPER_BERTH_ARR.append(rac_ticket)
                    UPPER_BERTH +=1
                    RAC_TICKET -=1
                    if(len(WAITING_TICKETS_ARR) !=0 ):
                        waiting_ticket = WAITING_TICKETS_ARR.pop(0)
                        RAC_TICKET_ARR.append(waiting_ticket)
                        RAC_TICKET +=1
                        WAITING_TICKETS -=1




    elif(cancel_status == "M"):
        for i in range(len(MIDDLE_BERTH_ARR)):
            if(MIDDLE_BERTH_ARR[i].id == cancel_id):
                MIDDLE_BERTH_ARR.pop(i)
                founder = True
                MIDDLE_BERTH -=1
                if (len(RAC_TICKET_ARR) != 0):
                    rac_ticket = RAC_TICKET_ARR.pop(0)
                    MIDDLE_BERTH_ARR.append(rac_ticket)
                    MIDDLE_BERTH += 1
                    RAC_TICKET -= 1
                    if (len(WAITING_TICKETS_ARR) != 0):
                        waiting_ticket = WAITING_TICKETS_ARR.pop(0)
                        RAC_TICKET_ARR.append(waiting_ticket)
                        RAC_TICKET += 1
                        WAITING_TICKETS -= 1

    elif (cancel_status == "L"):
        for i in range(len(LOWER_BERTH_ARR)):
            if(LOWER_BERTH_ARR[i].id == cancel_id):
                LOWER_BERTH_ARR.pop(i)
                founder = True
                LOWER_BERTH -=1
                if (len(RAC_TICKET_ARR) != 0):
                    rac_ticket = RAC_TICKET_ARR.pop(0)
                    LOWER_BERTH_ARR.append(rac_ticket)
                    LOWER_BERTH += 1
                    RAC_TICKET -= 1
                    if (len(WAITING_TICKETS_ARR) != 0):
                        waiting_ticket = WAITING_TICKETS_ARR.pop(0)
                        RAC_TICKET_ARR.append(waiting_ticket)
                        RAC_TICKET += 1
                        WAITING_TICKETS -= 1

    elif (cancel_status == "R"):
        for i in range(len(RAC_TICKET_ARR)):
            if(RAC_TICKET_ARR[i].id == cancel_id):
                RAC_TICKET_ARR.pop(i)
                founder = True
                RAC_TICKET -=1
                if (len(WAITING_TICKETS_ARR) != 0):
                    waiting_ticket = WAITING_TICKETS_ARR.pop(0)
                    RAC_TICKET_ARR.append(waiting_ticket)
                    RAC_TICKET += 1
                    WAITING_TICKETS -= 1

    elif(cancel_status == "W"):
        for i in range(len(WAITING_TICKETS_ARR)):
            if(WAITING_TICKETS_ARR[i].id == cancel_id):
                WAITING_TICKETS_ARR.pop(i)
                founder = True

    if(founder == False):
        print("enter an valid id and status for cancellation")



def available_tickets():
    print("Upper Berth : " , UPPER_BERTH)
    print("Middle Berth : " , MIDDLE_BERTH)
    print("Lower Berth : " , LOWER_BERTH)
    print("RAC : " , RAC_TICKET)
    print("Waiting List : " , WAITING_TICKETS)

def booked_tickets():
    print("**** Upper berth List ****")
    for i in range(len(UPPER_BERTH_ARR)):
        print("____________________")
        print("user id :" , UPPER_BERTH_ARR[i].id)
        print("user Name :" , UPPER_BERTH_ARR[i].name)
        print("User age :", UPPER_BERTH_ARR[i].age)
        print("user status :", UPPER_BERTH_ARR[i].status)

    print("--------------------------")

    print("**** Middle berth List ****")
    for i in range(len(MIDDLE_BERTH_ARR)):
        print("____________________")
        print("user id :",MIDDLE_BERTH_ARR[i].id)
        print("user name :",MIDDLE_BERTH_ARR[i].name)
        print("user age :", MIDDLE_BERTH_ARR[i].age)
        print("user status :", MIDDLE_BERTH_ARR[i].status)

    print("--------------------------")

    print("**** Lower berth List ****")
    for i in range(len(LOWER_BERTH_ARR)):
        print("____________________")
        print("User id :" , LOWER_BERTH_ARR[i].id)
        print("User Name : " , LOWER_BERTH_ARR[i].name)
        print("User Age :" , LOWER_BERTH_ARR[i].age)
        print("user status :", LOWER_BERTH_ARR[i].status)
    print("-----------------------")


    print("**** RAC List ****")
    for i in range(len(RAC_TICKET_ARR)):
        print("____________________")
        print(RAC_TICKET_ARR[i].id)
        print(RAC_TICKET_ARR[i].name)
        print(RAC_TICKET_ARR[i].age)
        print("user status :", RAC_TICKET_ARR[i].status)

    print("-----------------------")

    print("**** Waiting List ****")
    for i in range(len(WAITING_TICKETS_ARR)):
        print("____________________")
        print(WAITING_TICKETS_ARR[i].id)
        print(WAITING_TICKETS_ARR[i].name)
        print(WAITING_TICKETS_ARR[i].age)
        print("user status :", WAITING_TICKETS_ARR[i].status)

    print("-----------------------")



while(1):
    print("-------- Choose any one option --------")
    print("1. Booking ")
    print("2. Cancel  ")
    print("3. Available Tickets")
    print("4. Booked Tickets ")
    print("5. Exit the reservation ")
    print("----------------------------------------")

    choose = int(input("enter the functionality"))
    if(choose == 1):
        print("--------------------------------------------------------")
        print("-----------------------Booking Option--------------------")
        book_tickets()
    elif(choose ==2):
        print("--------------------------------------------------------")
        print("----------------------Cancel Option---------------------")
        cancel_ticket()
    elif(choose == 3):
        print("-------------------------------------------------------")
        print("--------------------Available Tickets-------------------")
        available_tickets()
    elif(choose == 4):
        print("--------------------------------------------------------")
        print("----------------------Booked tickets -------------------")
        booked_tickets()
    elif(choose == 5):
        break
    else:
        print("!!!! Select any valid choice !!!!")
