from math import *
units = {'0':'', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
tens = {'0':'', '00':'', '10':'ten', '11':'eleven', '12':'twelve','13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen', '20':'twenty', '30':'thirty', '40':'forty', '50':'fifty', '60':'sixty', '70':'seventy', '80':'eighty', '90':'ninety'}
placeVal ={'0':'', '1':' thousand', '2':' million', '3':' billion', '4':' trillion'}

def group(num):
    Rang = ceil(len(num)/3)
    num2 = num[::-1]
    new = []
    for item in range(Rang):
        new.append((num2[:3])[::-1])
        num2 = num2[3:]
    new = new[::-1]    
    return new

def hundreds(part):
    value = ''
    if (len(part)==1) or part.startswith('00'):
        value+=units[str(int(part))]
    elif (len(part)==2) or part.startswith('0'):
        value+= Tens(str(int(part)))
    elif len(part)==3:
        value += units[part[0]] + ' hundred'
        if part[1:] == '00':
            value = value
        elif part[1] == '0':
            value += ' and ' + units[part[2]]
        else:
            value += ' and ' + Tens(part[1:])
    return value
        
def Tens(num):
    value = ''
    if num.startswith('1'):
        value += tens[num]
    else:
        value += tens[num[0]+'0' ]
        if num[1] != '0':
            value += '-' + units[num[1]]
    return value

def toWords(digits):
 #   try:
        digits = str(digits)
        divided = group(digits)
        order = len(divided)-1
        word = ''
        for item in divided:
            if (len(divided)>1)and(order == 0)and(item.startswith('00')or item.startswith('0'))and(item !='000'):
                word += 'and '
            if item == '000':
                order -= 1
                continue
            word += hundreds(item) +  placeVal[str(order)]
            if (order != 0) and (divided[divided.index(item)+1]!='000') and (order-1 !=0):
                word+=', '
            elif (order != 0) and (divided[divided.index(item)+1]=='000') and ((order-1) !=0):
                word+=' '
            elif (order-1==0):
                if divided[divided.index(item)+1].startswith('0'):
                    word+=' '
                elif not divided[divided.index(item)+1].startswith('0'):
                    word +=', '
            order -= 1
        return word
                
#    except:
        return "The number you inputed is invalid or out of range"


number = int(input('Input a number: '))
print()
print(number, '=', toWords(number))

#def convert():
#    again = True
#    while again:
#        try:
#            number = int(input('Input a number: '))
#            print(toWords(number))
#        except:
#            print('Invalid number!')
#        valid = False
#        while not valid:
#            repeat = input('Do you want to convert another? (y/n): ')
#            if repeat =='y':
#                valid = True
#            elif repeat == 'n':
#                again = False
#                valid =True
#            else:
#                print('Invalid response!')
#                print()
#convert()            
#This commented out function would run better an another python console supports real time inputs, as sololearn supports inputs only at the beginning of running and not in real time
