# Создайте программу для игры в ""Крестики-нолики"".

list_cross = [['1' , '2' , '3'] , ['4' , '5' , '6'] , ['7' , '8' , '9']]
# for i in range(3):
#     for j in range(3):
#         list_cross.append('_')

def win_game(list_cross):
    if (list_cross[0,0] == list_cross[1,1] == list_cross[2,2]) or \
        (list_cross[0, 0] == list_cross[0, 1] == list_cross[0, 2]) or \
        (list_cross[1, 0] == list_cross[1, 1] == list_cross[1,2]) or \
            ()

print(list_cross, end='\n')
