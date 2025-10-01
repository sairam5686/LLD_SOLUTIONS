import re

id = 1
MAILS =  []
ALL_TAGS = set()


class Mail:
    tag = set()
    def __init__(self , id , sender , receiver , tag  , subject , content ):
        self.id = id
        self.sender = sender
        self.receiver = receiver
        self.tag = tag
        self.subject = subject
        self.content = content


def create_mail( sender , receiver , tag  , subject , content ):
    global id
    tag =tag.split()
    ALL_TAGS.update(tag)
    tag = set(tag)
    new_mail = Mail(id , sender , receiver, tag, subject, content)
    MAILS.append(new_mail)
    id +=1
def delete_mail(local_id):
    founder = False
    for i in range(len(MAILS)):
        if(MAILS[i].id == local_id):
            ALL_TAGS.difference(MAILS[i].tag)
            MAILS.pop(i)
            return True
    return False


def mail_stats():
    print("Total No of mails : " ,len(MAILS))
    print("All the tags used :" ,  " ".join(ALL_TAGS))
    Recent_N  = int(input("Enter the number of mails : "))
    print("_________________________________________________________________________")
    for  i in range(-1, -Recent_N-1 , -1):
        print("Mail id : "  , MAILS[i].id)
        print("Sender Mail : "  , MAILS[i].sender)
        print("Receiver Mail : " , MAILS[i].receiver)
        print("Tags : " , " ".join(MAILS[i].tag))
        print("Mail Subject : " , MAILS[i].subject)
        print("Mail Content : ", MAILS[i].content)
        print("___________________________________________________________________________")


def add_tags(mail_id):
    local_tags = input("Enter the tags that you what to add with space : ")
    local_tags = local_tags.split()
    local_tags = set(local_tags)
    for i in range(len(MAILS)):
        if(MAILS[i].id == mail_id):
            MAILS[i].tag.update(local_tags)
            ALL_TAGS.update(local_tags)
            return True
    return False
def query_search(search_mail):
    checker = False
    for i in range(len(MAILS)):
       if(search_mail == MAILS[i].sender or search_mail == MAILS[i].receiver):
            print("Mail id : ", MAILS[i].id)
            print("Sender Mail : ", MAILS[i].sender)
            print("Receiver Mail : ", MAILS[i].receiver)
            print("Tags : ", " ".join(MAILS[i].tag))
            print("Mail Subject : ", MAILS[i].subject)
            print("Mail Content : ", MAILS[i].content)
            checker = True
    if(checker == False):
        print("The mail is not found ,so pls enter an valid one ")




def fuzzy_search(fuzzy_word):
    pattern = rf"(?i)\b{fuzzy_word}\b"
    for i in range(len(MAILS)):
        if(re.search( pattern,MAILS[i].content )
                or re.search(pattern , MAILS[i].subject)
                or re.search(pattern , MAILS[i].sender)
                or re.search(pattern , MAILS[i].receiver)
                or re.search(pattern , str(MAILS[i].tag)) ):
            print("Mail id : ", MAILS[i].id)
            print("Sender Mail : ", MAILS[i].sender)
            print("Receiver Mail : ", MAILS[i].receiver)
            print("Tags : ", " ".join(MAILS[i].tag))
            print("Mail Subject : ", MAILS[i].subject)
            print("Mail Content : ", MAILS[i].content)
            print("___________________________________________________________")






while(1):
    print("________________________ Mail Management system _______________________")
    print("1. Create Mail ")
    print("2. Delete Mail ")
    print("3. Mail Statics")
    print("4. Add Tags to Mail")
    print("5. Mail Search ")
    print("6. Fuzzy search")
    print("7. Exit ")
    choose = int(input("enter the choose ( 1- 7 ) : "))
    if(choose == 1):
        print("____________________________________________________________________")
        print("______________________ Create ______________________________________")
        sender  = input("Enter the mail of the Sender : ")
        receiver = input("Enter the mail of the receiver : ")
        tags = input("Enter the tags that you want to classify with space : ")
        subject = input("Enter the subject of the mail : ")
        content  =input("Enter the content of the mail : ")
        create_mail( sender , receiver , tags , subject , content )
        print("Mail Has been Successfully Created ")
        print("_______________________________________________________________________")

    elif(choose ==2):
        print("____________________________________________________________________")
        print("_________________________ Delete ___________________________________")

        delete_id = int(input("Enter the mail id for deletion : "))
        result =  delete_mail(delete_id)

        if(result == True):
            print("Mail has been Successfully Deleted")
        else:
            print("Enter an Valid mail id for Deletion ")
        print("_____________________________________________________________________")


    elif(choose == 3):

        print("_____________________________________________________________________________")
        print("________________________________ Mail Information __________________________________")

        mail_stats()

        print("_____________________________________________________________________________")

    elif(choose == 4):

        print("_____________________________________________________________________________")
        print("________________________________ Tag Adder __________________________________")
        local_id = int(input("enter the mails id : "))

        result =add_tags(local_id)

        if (result == True):
            print("Tag have been successfully added")
        else:
            print("enter an valid mail id")

        print("_____________________________________________________________________________")

    elif(choose == 5):
        print("_____________________________________________________________________________")
        print("________________________________ Structured Search ( Based on Sender and receiver mail ) __________________________________")
        mail_name = input("enter the sender or receiver mail : ")
        query_search(mail_name)

        print("_____________________________________________________________________________")

    elif(choose == 6):
        print("_____________________________________________________________________________")
        print("________________________________Fuzzy Search (Brute search -> No rules followed ) __________________________________")
        fuzzy_word = input("enter the search target : ")
        fuzzy_search(fuzzy_word)
        print("_____________________________________________________________________________")

    elif(choose == 7):
        break
    else:
        print("Invalid choose , pls enter an valid one !")
