num = 5
cap = 3
refill = 2
fun = [4,1,-2,3,4]
len = len(fun)
tokens = cap
max_fun = 0
max_fun_list = []
current_list = []
current_fun = 0

def total_fun(index, current_fun, tokens):
    global max_fun, max_fun_list
    for current_index in range(index, len):
        prev_tokens = tokens
        if current_list:                    #don't want to refill if first game, check if list is empty
            try:
                if current_list.index(current_index) != -1:  #dont refill tokens unless you play a new game
                    if current_list[-1] != current_index:    #games must be played in order, any game that's not new and not same as previously played is ignored
                        break
            except:                               #is a new game
                tokens += refill
                if tokens > cap:
                    tokens = cap
        if tokens > 0:
            tokens -= 1
            current_list.append(current_index)
            current_fun += fun[current_index]
            if current_fun > max_fun:
                played_all_games = True;
                for games in range(0, len):                 #test all games have been played
                    try:
                        if current_list.index(games) != -1:
                            pass
                    except:
                        played_all_games = False
                        break
                if played_all_games:
                    max_fun = current_fun
                    max_fun_list = list(current_list)    #save a copy of the list instead of a reference

            total_fun(index, current_fun, tokens)
            current_list.pop()
            current_fun -= fun[current_index]
            tokens = prev_tokens


total_fun(0, current_fun, tokens)
print(max_fun_list)   #TODO, incorrect
print(max_fun)
