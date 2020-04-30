import json
import sys

flag = int(input("Press 1 if you are a supplier of this VEnding Machine else press 0 if you want to buy something =>  "))

if flag ==1:
    password = int(input("Enter 4 digit password of vending machine =>  "))
    with open("pass.JSON","r") as password_json_file:
        temp = json.load(password_json_file)

    if password == temp["password"]:
        flag1 = int(input("Do you want to reset the vending Machine to groound level: press 1 if yes else press 0 =>  "))
        if flag1 == 1:
            reset_data = {"coin1": 0, "coin5": 0, "coin10": 0, "coin25": 0}
            with open("freq.JSON","w") as json_file:
                json.dump(reset_data,json_file)
    
    else:
        print("Incorrect Password")

    sys.exit()
        


with open("freq.JSON","r") as json_file:
    data = json.load(json_file)

initial_data = data


freq_coin_1 = data["coin1"]
freq_coin_5 = data["coin5"]
freq_coin_10 = data["coin10"]
freq_coin_25 = data["coin25"]


def check_for_money_return(money):
    global freq_coin_1, freq_coin_5, freq_coin_10, freq_coin_25 
   

    while money > 0:
              
        if money >= 25 and freq_coin_25 > 0:
            money = money - 25
            freq_coin_25 = freq_coin_25 - 1
       
        elif money >=10 and freq_coin_10 > 0:
            money = money - 10
            freq_coin_10 = freq_coin_10 -1
       
        elif money >=5 and freq_coin_5 > 0:
            money = money - 5
            freq_coin_5 = freq_coin_5 - 1
        
        elif money>=1 and freq_coin_1 > 0:
            money = money - 1
            freq_coin_1 = freq_coin_1 - 1
       
        else:
            return False

    
    return True  
   
count = 0
total_credit = 0
coin_num = int(input("How many coins would you like to enter:=>  "))
while count in range(coin_num):
    coin = int(input("Enter coin:  You can only enter coin from this set = {1,5,10,25}:=>   "))

    if coin == 1:
        freq_coin_1 = freq_coin_1 + 1
    elif coin == 5:
        freq_coin_5 = freq_coin_5 + 1
    elif coin == 10:
        freq_coin_10 = freq_coin_10 + 1
    elif coin == 25:
        freq_coin_25 = freq_coin_25 + 1
   
    total_credit = total_credit + coin
    count = count + 1


print("You have ",total_credit," in your bank" )
print("")
print("Choose your item:")
print("Press 1 for Coke (25 Bucks)")
print("Press 2 for Pepsi (35 Bucks)")
print("Press 3 for Soda (45 Bucks)")
item = int (input("Enter the number for your item:=>   "))

while item <1 or item >3:
    print("This item is not availabe")
    item = int(input("Enter the number for your item:=>   "))
final_credit = total_credit
if item ==1:
    if total_credit >= 25:
        money_to_return = total_credit - 25 
        if(check_for_money_return(money_to_return)):
            total_credit = total_credit - 25
            print("You have bought a Coke of 25 Bucks")
            print(" We have returned you ", total_credit , "Bucks" )
            data["coin1"] = freq_coin_1
            data["coin5"] = freq_coin_5
            data["coin10"] = freq_coin_10
            data["coin25"] = freq_coin_25
            print("")
            cancel = int(input("Do you want cancel the order: Press 1 if yes and 0 otherwise =>   "))
            if cancel == 0:
                with open("freq.JSON","w") as json_file:
                    json.dump(data,json_file)
       
        else:
            print("Vending Machine doesn't have enough coins to process your request")
            print("We have refunded your amount of ",final_credit," Bucks")     
    else:
        print("You don't have sufficient balance")
        print("We have refunded your amount of ",final_credit," Bucks")

elif item ==2:
    if total_credit >= 35:
        money_to_return = total_credit - 35
        if(check_for_money_return(money_to_return)):
            total_credit = total_credit - 35
            print("You have bought a Coke of 35 Bucks")
            print(" We have returned you ", total_credit , "Bucks" )
            data["coin1"] = freq_coin_1
            data["coin5"] = freq_coin_5
            data["coin10"] = freq_coin_10
            data["coin25"] = freq_coin_25
            print("")
            cancel = int(input("Do you want to cancel the order: Press 1 if yes and 0 otherwise:=>   "))
            if cancel == 0:
                with open("freq.JSON","w") as json_file:
                    json.dump(data,json_file)
       
        else:
            print("Vending Machine doesn't have enough coins to process your request")
            print("We have refunded your amount of ",final_credit," Bucks")
    else:
        print("You don't have sufficient balance")
        print("We have refunded your amount of ",final_credit," Bucks")

elif item == 3:
    if total_credit >= 45:
        money_to_return = total_credit - 45
        if(check_for_money_return(money_to_return)):
            total_credit = total_credit - 45
            print("You have bought a Coke of 45 Bucks")
            print(" We have returned you ", total_credit , "Bucks" )
            data["coin1"] = freq_coin_1
            data["coin5"] = freq_coin_5
            data["coin10"] = freq_coin_10
            data["coin25"] = freq_coin_25
            print("")
            cancel = int(input("Do you want to cancel the order: Press 1 if yes and 0 otherwise: =>  "))
            if cancel == 0:
                with open("freq.JSON","w") as json_file:
                    json.dump(data,json_file)
       
        else:
            print("Vending Machine doesn't have enough coins to process your request")
            print("We have refunded your amount of ",final_credit," Bucks")
    else:
        print("You don't have sufficient balance")  
        print("We have refunded your amount of ",final_credit," Bucks")