#Get individual octets and then put them in a list
#convert each octect(string) to a  integer

#Base condition if --> if want to exit enter exit(EXIT/exit/Exit) works
#else: continue to ipcheck

#Base2 condition if --> anything apart from exit or an ip return! ERROR!

#Condition
# Make sure only 4 octects

#conditions for all octects
#1. first octect has to be between 1-223
#2. rest of the octects have to be between 0-255
def count_check(ip):
    count = 0
    for octect in ip:
        count += 1
    return count == 4
        

def first_octet_check(octet):
    return int(octet) in range(1,223)


def octet_check(octetlist):
    return (lambda x: (int(octetlist[i]) in range(0-255)) for x in range(1,4))
                       

def cont_ip_check():
    repeat = input("\n Do you want to continue: ")
    return "y" in repeat.lower

def ip_check():
    repeat = True
    while repeat:
        ip = input("\nEnter the IP ADDRESS: ")
        octetlist= ip.split(".")
        if count_check(octetlist) and first_octet_check(octetlist[0]) and octet_check(octetlist):
            print ('VALID IP ADDRESS!')
            repeat = cont_ip_check()
        else:
            print ("ERROR!")
            repeat = cont_ip_check()

        
ip_check()