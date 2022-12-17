from django.template import loader
import random
# Create your views here.
from django.http import HttpResponse
import requests


def comy (game):

    emy = []
    lis = []
    fis = []

    x1 = 0
    for i in range (0,3):
        x =game[i].count("X")
        x1 += x

    if x1 != 1:

        for i in range(0,3):

            if len(lis) != 0:
                break

            k = game[i][1]

            if k == 'O':
                m = game[i][0]
                n = game[i][2]
                if m == 'O':
                    if game[i][2] == '':
                        lis.append([i , 2])
                        break
                elif n == 'O':
                    if game[i][0] == '':
                        lis.append([i , 0])
                        break
            elif k == '':
                m = game[i][0]
                n = game[i][2]
                if m == 'O' and n == 'O':
                    if game[i][1] == '':
                        lis.append([i , 1])
                        break



        for i in range(0,3):

            if len(lis) != 0:
                break

            k = game[1][i]
            if k == 'O':
                m = game[0][i]
                n = game[2][i]
                if m == 'O':
                    if game[2][i] == '':
                        lis.append([2 , i])
                        break
                elif n == 'O':
                    if game[0][i] == '':
                        lis.append([0 , i])
                        break
            elif k == '':
                m = game[0][i]
                n = game[2][i]
                if m == 'O' and n == 'O':
                    if game[1][i] == '':
                        lis.append([1 , i])
                        break
            

        if len(lis) == 0:
            v = game[1][1]
            if (v == "O"):

                if (game[0][2] == "O"):
                    if game[2][0] == '':
                        lis.append([2 , 0])
                elif game[2][0] == 'O':
                    if game[0][2] == '':
                        lis.append([0 , 2])

                if len(lis) == 0:   
                    
                    if (game[2][2] == "O"):
                        if game[0][0] == '':
                            lis.append([0 , 0])
                    elif game[0][0] == 'O':
                        if game[2][2] == '':
                            lis.append([2 , 2])


    if x1 != 1 and len(lis) == 0:

        for i in range(0,3):

            if len(lis) != 0:
                break

            k = game[i][1]

            if k == 'X':
                m = game[i][0]
                n = game[i][2]
                if m == 'X':
                    if game[i][2] == '':
                        lis.append([i , 2])
                        break
                elif n == 'X':
                    if game[i][0] == '':
                        lis.append([i , 0])
                        break
            elif k == '':
                m = game[i][0]
                n = game[i][2]
                if m == 'X' and n == 'X':
                    if game[i][1] == '':
                        lis.append([i , 1])
                        break



        for i in range(0,3):

            if len(lis) != 0:
                break

            k = game[1][i]
            if k == 'X':
                m = game[0][i]
                n = game[2][i]
                if m == 'X':
                    if game[2][i] == '':
                        lis.append([2 , i])
                        break
                elif n == 'X':
                    if game[0][i] == '':
                        lis.append([0 , i])
                        break
            elif k == '':
                m = game[0][i]
                n = game[2][i]
                if m == 'X' and n == 'X':
                    if game[1][i] == '':
                        lis.append([1 , i])
                        break



        if len(lis) == 0:
            v = game[1][1]
            if (v == "X"):

                if (game[0][2] == "X"):
                    if game[2][0] == '':
                        lis.append([2 , 0])
                elif game[2][0] == 'X':
                    if game[0][2] == '':
                        lis.append([0 , 2])

                if len(lis) == 0:   
                    
                    if (game[2][2] == "X"):
                        if game[0][0] == '':
                            lis.append([0 , 0])
                    elif game[0][0] == 'X':
                        if game[2][2] == '':
                            lis.append([2 , 2])

            elif game[1][1] == '':
        
                a = game[0][2]
                b = game[2][0]
                if (a == "X" and b == 'X'):
                    if game[1][1] == '':
                        lis.append([1 , 1])

                if len(lis) == 0:   
                    a = game[2][0]
                    b = game[0][2]
                    if (a == "X" and b == 'X'):
                        if game[1][1] == '':
                            lis.append([1 , 1])


    if len(lis) == 0:
        for i in range(0,3):

            if len(lis) != 0:
                break
            
            if game[i] == ['O' , '' , ''] or game[i] == ['' , 'O' , ''] or game[i] == ['' , '' , 'O']:
                if game[i][1] == '':
                    lis.append([i , 1])
                    break
                elif game[i][0] == '':
                    lis.append([i , 0])
                    break
                elif game[i][2] == '':
                    lis.append([i , 2])
                    break

    if len(lis) == 0:
        for i in range(0,3):

            fis.clear()

            for j in range(0,3):
                a = game[j][i]
                fis.append(a)
            
            if fis == ['O' , '' , ''] or game[i] == ['' , 'O' , ''] or game[i] == ['' , '' , 'O']:
                if fis[1] == '':
                    lis.append([1 , i])
                    break
                elif fis[0] == '':
                    lis.append([0 , i])
                    break
                elif fis[2] == '':
                    lis.append([2 , i])
                    break
        
    if len(lis) == 0:
        lif = [game[0][0] , game[1][1] , game[2][2]]
        jif = [game[0][2] , game[1][1] , game[2][0]]
        nn = [lif , jif]

        if lif == ['O' , '' , ''] or lif == ['' , 'O' , ''] or lif == ['' , '' , 'O']:
            if lif[0] == '':
                lis.append([0 , 0])
            elif lif[1] == '':
                lis.append([1 , 1])
            elif lif[2] == '':
                lis.append([2 , 2])
        elif jif == ['O' , '' , ''] or jif == ['' , 'O' , ''] or jif == ['' , '' , 'O']:
            if jif[0] == '':
                lis.append([0 , 2])
            elif jif[1] == '':
                lis.append([1 , 1])
            elif jif[2] == '':
                lis.append([2 , 0])



    if x1 == 1 or len(lis) == 0:
        if game[1][1] == '':
            lis.append([1,1])
        else:
            for i in range (0,3):
                for j in range (0,3):
                    if ((game[i][j])==''):
                        emy.append([i,j])
                        
            d = (len (emy))
            k = 0
            lis1 = []
            for i in range (d):
                k += 1 
                lis1.append(k)


            a = random.choice(lis1)
            a = a - 1
            x = emy[a][0]
            y = emy[a][1]
            lis.append([x , y])


    x = lis[0][0]
    y = lis[0][1]

    return x , y


def chekking_winner (game):
    won = []
    for i in range (0 , 3):
        for j in range (0 , 3):
            a = game[j][i]
            won. insert (1 , a)
            v = (len (won))
            if (v == 3):
                a = won [0]
                b = won [1]
                c = won [2]
                if ((a == "X")and(b=="X")and(c=="X")):
                    flag = 1
                    return flag
                if ((a == "O")and(b=="O")and(c=="O")):
                    flag = 2
                    return flag
        won.clear()
    for i in range (0 , 3):
        for j in range (0 , 3):
            a = game[i][j]
            won. insert (1 , a)
            v = (len (won))
            if (v == 3):
                a = won [0]
                b = won [1]
                c = won [2]
                if ((a == "X")and(b=="X")and(c=="X")):
                    return 1
                if ((a == "O")and(b=="O")and(c=="O")):
                    return 2
        won.clear()

    v = game[1][1]
    if (v == "X"):
        a = game[0][2]
        b = game[2][0]
        if ((a == "X") and (b == "X")):
            return 1
    elif (v == "O"):
        a = game[0][2]
        b = game[2][0]
        if ((a == "O") and (b == "O")):
            return 2

    if (v == "X"):
        a = game[0][0]
        b = game[2][2]
        if ((a == "X") and (b == "X")):
            return 1
    elif (v == "O"):
        a = game[0][0]
        b = game[2][2]
        if ((a == "O") and (b == "O")):
            return 2

    a = game [0].count("")    
    b = game [1].count("")
    c = game [2].count("")
    if ((a == 0) and (b == 0) and (c == 0)):
        return 3

    return 0


def index(request):
    ng = request.GET.get('new_game',"false")
    if (ng=='true'):
        del request.session["game"]
        del request.session["win"]
        del request.session["turn"]
    try:
        row = int(request.GET.get('row',"-1"))
        col = int(request.GET.get('col',"-1"))
    except:
        row = 10
        col = 10
    error = 'play!'
    game = request.session.get('game',[['','',''],['','',''],['','','']])
    turn = request.session.get('turn','X')
    win = request.session.get('win',False)
    template = loader.get_template('board.html')
    if not win:
        if (0<=row<=2 and 0<=col<=2):
            if game[row][col] == '':
                game[row][col] = turn
                if (turn=='X'): 
                    turn = 'O'
                else:
                    turn = 'X'

                winner = chekking_winner(game)

                if winner == 1:
                    error = 'X is winner!!!!'
                    win = True
                elif winner == 2:
                    error = 'O is winner!!!!'
                    win = True
                elif winner == 3:
                    error = 'Draw!!!!'
                    win = True

            elif game[row][col] != '':
                error = 'Cell is full!'
        elif (row==-1 and col==-1):
            error = 'play!'
        else:
            error = 'Invalid number!'
    elif win:
        error = 'The game is over. Click New Game to start a new game.'

    request.session['turn'] = turn
    request.session['game'] = game
    request.session['win'] = win

    context = {'game':game, 'turn':turn,'error':error}
    return HttpResponse(template.render(context, request))


def page1(request):
    # template = loader.get_template('board_1.html' )
    template = loader.get_template('board_1.html' )
    context = {}
    return HttpResponse(template.render(context, request))


def e404(request):
    # template = loader.get_template('board_1.html' )
    template = loader.get_template('e404.html' )
    context = {}
    return HttpResponse(template.render(context, request))


def index2(request):
    ng = request.GET.get('new_game',"false")
    if (ng=='true'):
        del request.session["game"]
        del request.session["win"]
        del request.session["turn"]
    try:
        row = int(request.GET.get('row',"-1"))
        col = int(request.GET.get('col',"-1"))
    except:
        row = 10
        col = 10
    error = 'play!'
    game = request.session.get('game',[['','',''],['','',''],['','','']])
    turn = request.session.get('turn','X')
    win = request.session.get('win',False)

    if not win:
        if (0<=row<=2 and 0<=col<=2):
            if game[row][col] == '':
                game[row][col] = turn
 
                winner = chekking_winner(game)

                if winner == 1:
                    error = 'X is winner!!!!'
                    win = True
                elif winner == 2:
                    error = 'O is winner!!!!'
                    win = True
                elif winner == 3:
                    error = 'Draw!!!!'
                    win = True

                if (turn=='X'): 
                    turn = 'O'
                else:
                    turn = 'X'

                            
                if turn == 'O':
                    if not win:
                        x , y = comy(game)
                        game[x][y] = turn
                        turn = 'X'

            
                winner = chekking_winner(game)

                if winner == 1:
                    error = 'X is winner!!!!'
                    win = True
                elif winner == 2:
                    error = 'O is winner!!!!'
                    win = True
                elif winner == 3:
                    error = 'Draw!!!!'
                    win = True


            elif game[row][col] != '':
                error = 'Cell is full!'
        elif (row==-1 and col==-1):
            error = 'play!'
        else:
            error = 'Invalid number!'
    elif win:
        error = 'The game is over. Click New Game to start a new game.'
        
    request.session['turn'] = turn
    request.session['game'] = game
    request.session['win'] = win


    template = loader.get_template('com_bord.html')
    context = {'game':game, 'turn':turn,'error':error}
    return HttpResponse(template.render(context, request))