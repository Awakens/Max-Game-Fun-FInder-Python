num = 4
cap = 5
refill = 2
fun = [4,1,2,3]
max_fun = 0
max_fun_list = []
current_list = []
TOKEN_CAPACITY = 150
tokens = TOKEN_CAPACITY
current_games_played = []
current_fun = 0

def total_fun(current_fun, tokens):
    global max_fun, max_fun_list
    for x in fun:
        if tokens > 0:
            current_list.append(x)
            current_fun += x
            tokens -= 1
            if(current_list[-1] != x):  #refill tokens if you play a different game? or new one? TODO
                tokens += refill
                if tokens > TOKEN_CAPACITY:
                    tokens = TOKEN_CAPACITY
            if current_fun > max_fun:
                played_all_games = True;
                for games in fun:                 #test all games have been played
                    try:
                        if current_list.index(games) != -1:
                            pass
                    except:
                        played_all_games = False
                        break
                if played_all_games:
                    max_fun = current_fun
                    max_fun_list = list(current_list)    #save a copy of the list instead of a reference

            total_fun(current_fun, tokens)
            current_list.pop()
            current_fun -= x


total_fun(current_fun, tokens)
print(max_fun_list)   #TODO, incorrect
