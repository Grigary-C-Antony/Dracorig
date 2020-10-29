import random
coin_stat = [0,0,0,0,0]
coin_Playerone = 10
coin_Playertwo = 10
count=0
def sixCheck(player_coins,dice_value,coin_stat):
    if dice_value == 6:
        return player_coins-1 , coin_stat
    elif coin_stat[dice_value-1]==1:
        return sum(coin_stat) + player_coins , [0,0,0,0,0]
    else:
        coin_stat[dice_value-1]=1
        return player_coins-1 , coin_stat
def gameplay(coin,coin_stat):
    dice_list = [1,2,3,4,5,6]
    dice_value = random.choice(dice_list)
    coin,coin_stat =sixCheck(coin,dice_value,coin_stat)
    print(dice_value,coin,coin_stat)
    return coin,coin_stat
while True:
    count+=1
    coin_Playerone,coin_stat = gameplay(coin_Playerone,coin_stat)
    coin_Playertwo,coin_stat = gameplay(coin_Playerone,coin_stat)
    if coin_Playerone ==0:
        print(f"player one wins in {count} steps")
        break
    elif coin_Playertwo ==0:
        print(f"player two wins in {count} steps")
        break
    else:
        pass