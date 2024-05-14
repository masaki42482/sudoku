#数独の正当性チェック  
def check(problem,i,j,number):
  #行チェック
    for column in range(9):
        if column != j:
            if problem[i][column] == number:
                return 1
  #列チェック
    for raw in range(9):
        if raw != i:    
            if problem[raw][j] == number:
                return 2
  #ブロックチェック
    if 0<= i <= 2:
        r_search = [0,1,2]
    elif 3 <= i <= 5:
        r_search = [3,4,5]
    else:
        r_search = [6,7,8]
        
    if 0<= j <= 2:
        c_search = [0,1,2]
    elif 3 <= j <= 5:
        c_search = [3,4,5]
    else:
        c_search = [6,7,8]
    # print(r_search,c_search)
    for raw in r_search:
        for column in c_search:
            if i != raw and j != column:
                if problem[raw][column] == number:
                    return 3
                if column == i and raw == j:
                    continue
    return 0

def possibility_check(problem,i,j):
    poss=[]
    for num in range (9):
        if check(problem,i,j,num+1) == 0:
            poss.append(num+1)
    return poss
    
def put_num_for_now(answer,i,j,poss):
    
    #終了条件
    if i == 8 and j == 8 and len(poss) == 1:
        answer[8][8] = poss[0]
        return "end"
    
    for num in poss:
        if check(answer,i,j,num) == 0:
            answer[i][j] = num
            #次の開きマスを探す
            flg = 0
            for raw in range(9):
                if i <= raw:
                    for column in range(9):
                        if answer[raw][column] == 0:
                            if j < column:
                                flg = 1
                                break
                            elif i < raw:
                                flg = 1
                                break
                    if flg == 1:
                        break
                    
            next_poss = possibility_check(answer,raw,column)
            if next_poss == []:
                if poss[-1] == num:
                        answer[i][j] = 0
                        return "error"
            
            else:
                result = put_num_for_now(answer,raw,column,next_poss)
                if result == "error":
                    if poss[-1] == num:
                        answer[i][j] = 0
                        return "error"
                if result == "end":
                    return "end"
        

def solve(answer):
    i = 0
    j = 0
    #次の開きマスを探す
    flg = 0
    for raw in range(9):
        if i <= raw:
            for column in range(9):
                if answer[raw][column] == 0:
                    if j <= column:
                        flg = 1
                        break
                    elif i < raw:
                        flg = 1
                        break
            if flg == 1:
                break
    poss = possibility_check(answer,raw,column)
    put_num_for_now(answer,raw,column,poss)
    answer_check(answer)
    return answer

def answer_check(answer):
    flag = 0
    for raw in range(9):
        for column in range(9):
            if check(answer,raw,column,answer[raw][column]) != 0:
                print(raw,column,answer[raw][column])
                print(check(answer,raw,column,answer[raw][column]))
                print("Contradiction is found")
                flag = 1
                break
        if flag == 1:
            return
    print("Succefully Solved")
    

def print_answer(answer):
    for line in answer:
        print(line) 
        
        
problem = [[0,0,0,0,7,0,6,0,5],[0,0,0,0,0,4,0,8,0],[2,0,0,0,0,6,0,7,0],[0,7,3,0,0,0,2,0,0],[5,0,0,0,0,0,0,0,4],[0,0,4,0,0,0,9,6,0],[0,8,0,4,0,0,0,0,3],[0,5,0,2,0,0,0,0,0],[7,0,6,0,8,0,0,0,0]]
answer = [[0,0,0,0,7,0,6,0,5],[0,0,0,0,0,4,0,8,0],[2,0,0,0,0,6,0,7,0],[0,7,3,0,0,0,2,0,0],[5,0,0,0,0,0,0,0,4],[0,0,4,0,0,0,9,6,0],[0,8,0,4,0,0,0,0,3],[0,5,0,2,0,0,0,0,0],[7,0,6,0,8,0,0,0,0]]
print_answer(solve(answer))