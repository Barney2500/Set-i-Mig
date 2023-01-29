import random
import mysql.connector
from dades import *

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="sevenhalf"
)

mycursor = db.cursor()

cadenainfo = "Name".ljust(10) + \
         "Human".ljust(10) + \
         "Bank".ljust(5) + \
         "InitialCard".ljust(14) + \
         "Priority".ljust(10) + \
         "Type".ljust(10) + \
         "Bet".ljust(10) + \
         "Points".ljust(10) + \
         "Cards".ljust(10) + \
         "RoundPoints".ljust(10) + \
         "\n" + "*" * 93 + "\n"

cartaesc = ''
mazo = []
def menu(c, t, i, o=None):
    if o is None:
        o = []
    next = False
    while not next:
        print(c)
        print(t)
        x = input(i)
        if not x.isdigit():
            print("Only numbers accepted")
            next = False
        else:
            x = int(x)
            if x not in o:
                next = False
                print('Value not accepted')
            else:
                return x


def ques(c, t, i, o=None):
    if o is None:
        o = []
    next = False
    while not next:
        print(c)
        print(t)
        x = input(i)
        if x not in o:
            print("Value not accepted")
            next = False
        else:
            return x


def getOpt(textOpts="", inputOptText="", rangeList=[], exceptions=[]):
    print(textOpts)
    q = -111
    while q not in rangeList and q not in exceptions:
        q = input(inputOptText)
        if not q.isdigit():
            print('Other values apart from integers are not available')
        else:
            q = int(q)
    return q


def adrem(c, t, i, r, o=[]):
    nifli = []
    mycursor.execute("SELECT player_id FROM player")
    for x in mycursor:
        for xe in x:
            nifli.append(xe)
    next = False
    while not next:
        print(c)
        showpla()
        print(t)
        g = input(i)
        if g not in o and g not in nifli:
            print('Value not accepted')
        if g in o:
            return g
        elif g in nifli:
            if r :
                gr = yn(f'Are you sure you want to remove player with id {g}?', 'Y/n')
                if gr:
                    delebas(g)
                else:
                    return
            if not r:
                gn = yn('Do you want to add this player?')
                if gn:
                    if g in playcont:
                        print('user alredy added')
                    else:
                        gi = getGameId()
                        dicplay(g)
                        fill_player_game(g, gi)
                        playcont.append(g)
                else:
                    return

def roundmax():
    next = False
    while not next:
        ma = input("Max Rounds")
        ma.strip()
        if not ma.isdigit() or not ma or ma.isspace():
            print('Please enter only int')
        else:
            ma = int(ma)
            if 0 < ma < 20:
                contextgame['rounds'] = ma
                return
            else:
                print('Only numbers between 5 and 20')
def delebas(p):
    mycursor.execute(f"DELETE FROM player WHERE player_id = '{p}'")
    db.commit()


def dicplay(i):
    mycursor.execute(f"SELECT player_name FROM player WHERE player_id = '{i}'")
    for x in mycursor:
        for xe in x:
            name = xe
    mycursor.execute(f"SELECT human FROM player WHERE player_id = '{i}'")
    for xa in mycursor:
        for xa in xa:
            hum = xa
    mycursor.execute(f"SELECT player_risk FROM player WHERE player_id = '{i}'")
    for xes in mycursor:
        for xo in xes:
            ty = xo
    if hum == 1:
        players[i]={'name':name, 'human':True, 'bank':False,"initialCard": "", "priority": 0, 'type':ty, 'bet': '', 'points': 0, 'cards': [], 'roundPoints' : 0}
    elif hum == 0:
        players[i] = {'name': name, 'human': False, 'bank': False, "initialCard": "", "priority": 0, 'type': ty,
                      'bet': '', 'points': 0, 'cards': [], 'roundPoints': 0}


def showpla():
    cadenah = ("*" * 35) + "Human" + ("*" * 39) + "\n" \
                                                  "ID".ljust(30) + \
              "Name".ljust(30) + \
              "Type".ljust(30) + \
              "\n" + "*" * 78 + "\n"

    cadenab = ("*" * 35) + "Bot" + ("*" * 39) + "\n" \
                                                "ID".ljust(30) + \
              "Name".ljust(30) + \
              "Type".ljust(30) + \
              "\n" + "*" * 78 + "\n"
    mycursor.execute("SELECT * FROM player")
    for x in mycursor:
        if x[3] == 1:
            for se in x:
                if se != 1:
                    k = se
                    cadenah = cadenah + str(k).ljust(30)
            cadenah = cadenah + "\n"
        else:
            for sa in x:
                if sa != 0:
                    kk = sa
                    cadenab = cadenab + str(kk).ljust(30)
            cadenab = cadenab + "\n"
    print(cadenah, cadenab)


def escogermazo():
    me = getOpt("1)Spanish Deck\n2)Poker Deck", 'Select:', [1, 2])
    if me == 1:
        cartaesc = cartasES.copy()
        contextgame['mazo'] = 'ESP'
        return cartaesc
    elif me == 2:
        cartaesc = cartasEN.copy()
        contextgame['mazo'] = 'POK'
        return cartaesc


def resetPoints():
    for i in players:
        players[i]['points'] = 20


def getGameId():
    next = False
    lid = []
    while not next:
        gameid = random.randint(1, 500)
        mycursor.execute("SELECT cardgame_id FROM player_game")
        for x in mycursor:
            for xe in x:
                lid.append(xe)
        if gameid not in lid:
            return gameid
        else:
            next = False


gameID = getGameId()


def newName():
    next = False
    while not next:
        nn = input('Name:')
        nn = nn.strip()
        if not nn or nn.isspace() or nn.isdigit():
            print('Incorrect name, please, enter a name not empty with only letters')
        else:
            return nn


def newDni(h):
    next = False
    dnlist = []
    mycursor.execute("SELECT player_id FROM player")
    for x in mycursor:
        for cf in x:
            dnlist.append(cf)
    while not next:
        if h:
            dni = input('Introduzca un DNI valido')
            if len(dni) != 9 or not dni[0:8].isdigit():
                print('El formato de DNI no es valido')
            elif letrasDNI[int(dni[0:8]) % 23].lower() != dni[8].lower():
                print(f'El DNI {dni} no es valido')

            else:
                dni = dni.upper()
                if dni in dnlist:
                    print('DNI alredy exists')
                else:
                    return dni
        elif not h:
            dnin = random.randint(11111111, 99999999)
            letra = palabra[dnin % 23]
            dni = (str(dnin) + letra)
            if dni in dnlist:
                next = False
            else:
                return dni


def newProfile():
    sel = getOpt('1)Cautious\n2)Moderated\n3)Bold', 'Option: ', [1, 2, 3])
    if sel == 1:
        return 20
    elif sel == 2:
        return 30
    elif sel == 3:
        return 40


def newPlayer(d, n, p, h):
    if h:
        return d, {'name': n, 'human': h, 'bank': False, 'initialCard': '', 'priority': '', 'type': p, 'bet': '',
                   'points': 0, 'cards': [], 'roundPoints': 0}
    elif not h:
        return d, {'name': n, 'human': h, 'bank': False, 'initialCard': '', 'priority': '', 'type': p, 'bet': '',
                   'points': 0, 'cards': [], 'roundPoints': 0}


def fill_player_game(pg, gid, *f):
    player_game[gid] = {pg: {'initial_card_id': '', 'starting_points': '', 'ending_points': ''}}


def fill_player_game_round(pgr, r, *f):
    player_game_round = {r + 1: {'': {'is_bank': '', 'bet_points': '', 'starting_round_points': '', 'cards_value': '',
                                      'endind_round_points': ''}}}


#


def lc(lcd):
    contador = 0
    for i in ordjug:
        players[i]['cards'] = lcd[contador]
        contador += 1


def yn(text='', textinp=''):
    print(text)
    x = 'e'
    while x != 'y' or x != 'n':
        x = input(textinp)
        x = x.lower()
        if x == 'y':
            s = True
            return s
        elif x == 'n':
            s = False
            return s
        else:
            print('Only y or n')


def setGamePriority(m):
    n = list(m.keys())
    listprueba = n.copy()
    prioridad = []
    for i in players:
        players[i]['initialCard'] = random.choice(listprueba)
        x = players[i]['initialCard']
        listprueba.remove(x)
    for a in players:
        for s in n:
            if s == players[a]['initialCard']:
                prioridad.append([s, m[s]['realValue'] * 10 + m[s]['priority'], a])
    tope = len(prioridad) - 1
    for pasada in range(len(prioridad) - 1):
        for i in range(tope):
            if prioridad[i][1] > prioridad[i + 1][1]:
                prioridad[i], prioridad[i + 1] = prioridad[i + 1], prioridad[i]
        tope -= 1
    for s in players:
        for c in range(len(prioridad)):
            if prioridad[c][0] == players[s]['initialCard']:
                players[s]['priority'] = c + 1
    for p in range(len(prioridad)):
        game.append(prioridad[p][2])


def orderAllPlayers():
    for i in range(len(game)):
        if i + 1 == len(game):
            orden.insert(0, game[i])
            players[game[i]]['bank'] = True
        else:
            orden.append(game[i])
    for o in orden:
        ordjug.append(o)
    ordjug.reverse()


# def setBets():
#     next = False
#     for s in range(len(ordjug)):
#         for i in players:
#             if ordjug[s] == i:
#                 while not next:
#                     apuesta = input('Set the Bet\nOnly integers allowed: ')
#                     apuesta = apuesta.strip()
#                     if apuesta.isalpha() or apuesta.isspace() or not apuesta or not apuesta.isdigit():
#                         print('Please, introduce only integers above 0')
#                     else:
#                         if players[i]['type'] == 30:
#                             mb = maxbetC(players[i]['points'])
#                             if apuesta > mb:
#                                 print('Due to the profile type this bet is not allowed, reduce the value')
#                             elif apuesta <= 0:
#                                 print('Bets under 0 are not allowed')
#                             else:
#                                 print(f'Bet with value {apuesta} has been accepted')
#                                 return apuesta
#                         elif players[i]['type'] == 40:
#                             mb = maxbetM(players[i]['points'])
#                             if apuesta > mb:
#                                 print('Due to the profile type this bet is not allowed, reduce the value')
#                             elif apuesta <= 0:
#                                 print('Bets under 0 are not allowed')
#                             else:
#                                 print(f'Bet with value {apuesta} has been accepted')
#                                 return apuesta
#                         elif players[i]['type'] == 50:
#                             mb = maxbetB(players[i]['points'])
#                             if apuesta > mb:
#                                 print('Due to the profile type this bet is not allowed, reduce the value')
#                             elif apuesta <= 0:
#                                 print('Bets under 0 are not allowed')
#                             else:
#                                 print(f'Bet with value {apuesta} has been accepted')
#                                 return apuesta


def setBets(id,ju):
    next = False
    while not next:
        if ju:
            apuesta = input('Set the Bet\nOnly integers allowed: ')
            apuesta = apuesta.strip()
            if apuesta.isalpha() or apuesta.isspace() or not apuesta or not apuesta.isdigit():
                print('Please, introduce only integers above 0')
            else:
                apuesta = int(apuesta)
                if players[id]['type'] == 30:
                    mb = maxbetC(players[id]['points'])
                    print(mb)
                    if apuesta > mb:
                        print('Due to the profile type this bet is not allowed, reduce the value')
                    elif apuesta <= 0:
                        print('Bets under 0 are not allowed')
                    else:
                        print(f'Bet with value {apuesta} has been accepted')
                        players[id]['bet'] = apuesta
                        return
                elif players[id]['type'] == 40:
                    mb = maxbetM(players[id]['points'])
                    if apuesta > mb:
                        print('Due to the profile type this bet is not allowed, reduce the value')
                    elif apuesta <= 0:
                        print('Bets under 0 are not allowed')
                    else:
                        print(f'Bet with value {apuesta} has been accepted')
                        players[id]['bet'] = apuesta

                        return
                elif players[id]['type'] == 50:
                    mb = maxbetB(players[id]['points'])
                    if apuesta > mb:
                        print('Due to the profile type this bet is not allowed, reduce the value')
                    elif apuesta <= 0:
                        print('Bets under 0 are not allowed')
                    else:
                        print(f'Bet with value {apuesta} has been accepted')
                        players[id]['bet'] = apuesta
                        return
        if not ju:
            bets = 0
            bets = players[id]['points'] * (players[id]['priority']/10)
            bets = str(bets)
            ass = quitardec(bets)
            players[id]['bet'] = ass
            return


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def maxbetC(d):
    apuestamax = (d * 0.3)
    apuestamax = str(apuestamax)
    a = quitardec(apuestamax)

    return a


def maxbetM(d):
    apuestamax = (d * 0.4)
    apuestamax = str(apuestamax)
    a = quitardec(apuestamax)

    return a


def maxbetB(d):
    apuestamax = (d * 0.5)

    a = quitardec(apuestamax)

    return a


def quitardec(x):
    j = x.split(".")
    r = j[0]
    r = int(r)
    return r



def standarRound(id, mazo, c, bc, k=False, p=False):
    suma = []
    sumarp = 0
    if not players[id]['cards']:
        c.append(random.choice(mazo))
        players[id]['cards'] = c
        print(f'You first card is {c}')
        for su in c:
            players[id]['roundPoints'] = bc[su]['value']
            mazo.remove(su)
    else:
        if players[id]['roundPoints'] > 7.5:
            lost = True
            return lost
        else:
            if not players[id]['human'] or k:
                pcpc = 1
                if p:
                    while sumarp < 7.5:
                        cd = random.choice(mazo)
                        c.append(cd)
                        print(f'You drawed {cd}')
                        for iss in range(len(c)):
                            sumarp += bc[c[iss]]['value']
                        players[id]['roundPoints'] = sumarp
                        for cc in c:
                            if cc in mazo:
                                mazo.remove(cc)
                while pcpc < players[id]['type']:
                    sumaval = 0
                    contador = 0
                    sumarp = 0
                    for isa in players[id]['cards']:
                        suma.append(bc[isa]['value'])
                    for su in suma:
                        sumaval += su
                    for r in bc:
                        if bc[r]['value'] + sumaval > 7.5:
                            contador += 1
                    pcpc = (contador / len(mazo)) * 100
                    pcpc = int(pcpc)
                    if pcpc > players[id]['type']:
                        pas = True
                        return pas
                    else:
                        cd = random.choice(mazo)
                        c.append(cd)
                        print(f'You drawed {cd}')
                        for iss in range(len(c)):
                            sumarp += bc[c[iss]]['value']
                        players[id]['roundPoints'] = sumarp
                        for cc in c:
                            if cc in mazo:
                                mazo.remove(cc)
            if players[id]['human'] and not k:
                sumaval = 0
                contador = 0
                for i in players[id]['cards']:
                    suma.append(bc[i]['value'])
                for su in suma:
                    sumaval += su
                for r in bc:
                    if bc[r]['value'] + sumaval > 7.5:
                        contador += 1
                    if sumaval > 7.5:
                        pas = True
                        return pas
                pcpc = (contador / len(mazo)) * 100
                pcpc = int(pcpc)
                if sumaval == 7.5:
                    res = yn(f'You alredy have 7.5', 'Do you really want to draw another card?')
                    if res:
                        cd = random.choice(mazo)
                        c.append(cd)
                        print(f'You drawed {cd}')
                        for i in range(len(c)):
                            sumarp += bc[c[i]]['value']
                        players[id]['roundPoints'] = sumarp
                        for su in c:
                            if su in mazo:
                                mazo.remove(su)
                        pas = False
                        return pas
                    elif not res:
                        pas = True
                        return pas
                if pcpc > players[id]['type'] and not p:
                    resp = yn(f'Chance of exceed 7.5 = {pcpc}%', 'Are you sure you want another card?')
                    if resp:
                        cd = random.choice(mazo)
                        c.append(cd)
                        print(f'You drawed {cd}')
                        for i in range(len(c)):
                            sumarp += bc[c[i]]['value']
                        players[id]['roundPoints'] = sumarp
                        for su in c:
                            if su in mazo:
                                mazo.remove(su)
                        pas = False
                        return pas
                    elif not resp:
                        pas = True
                        return pas
                else:
                    cd = random.choice(mazo)
                    c.append(cd)
                    print(f'You drawed {cd}')
                    for i in range(len(c)):
                        sumarp += bc[c[i]]['value']
                    players[id]['roundPoints'] = sumarp
                    for su in c:
                        if su in mazo:
                            mazo.remove(su)
                    pas = False
                    return pas


def newbank():
    lb = []
    po = []
    for h in players:
        if players[h]['roundPoints'] == 7.5:
            lb.append(h)
    for ha in lb:
        if players[ha]['bank']:
            return
        elif len(lb) >= 1:
            po.append(players[ha]['priority'])
        po.sort(reverse=True)
    for hi in players:
        players[hi]['bank'] = False
    for he in lb:
        if po[0] == players[he]['priority']:
            players[he]['bank'] = True
            players[he]['priority'] = 3
            for k in players:
                if players[k]['priority'] == 3:
                    players[k]['priority'] = po[0]
            print('Se ha cambiado de banca')


def distributionPointAndNewBankCandidates():
    contador = 0
    lpu = []
    licom = []
    wind = ''
    lipri = []
    sumw = 0
    for q in players:
        lpu.append(players[q]['roundPoints'])
    lpu.sort(reverse=True)
    for ple in players:
        if players[ple]['roundPoints'] == lpu[0]:
            licom.append('si')
            wind = ple
        else:
            licom.append('no')
    for ip in range(len(licom)):
        if 'si' in licom[ip]:
            contador += 1
    if contador > 1:
        for se in players:
            if players[se]['roundPoints'] == lpu[0]:
                lipri.append(players[se]['priority'])
            lipri.sort(reverse=True)
        print(lipri)
        for det in players:
            if players[det]['priority'] == lipri[0]:
                wind = det
                print(wind)
        for sa in players:
            if sa != wind:
                sumw += players[sa]['bet']
                players[sa]['points'] -= players[sa]['bet']
        players[wind]['points'] += sumw

    else:
        for sa in players:
            if sa != wind:
                sumw += players[sa]['bet']
                players[sa]['points'] -= players[sa]['bet']
        players[wind]['points'] += sumw

def check2Play():
    contador = 0
    for i in players:
        if players[i]['points'] > 0:
            contador+=1
        else:
            removepl(i)

def removepl(id):
    players.pop(id,None)


def printPlayerStats(id):
    for i in players[id]:
        print(i,players[id][i],'\n')
    input('Enter to return')
    return
def printStats(c,idPlayer=""):
    if idPlayer != "":
        print(f'Turn of {players[idPlayer]["name"]}')
    c = c + "\n"
    for i in players:
        for a in players[i]:
            c = c + str(players[i][a]).ljust(10)
        c = c + "\n"
    print(c)
    input('Enter to continue\n')
    return
def humanround(id,ma,mace):
    x = getOpt('1)View Stats\n2)View Game Stats\n3)Set Bet\n4)Order Card\n5)Automatic Play\n6)Stand','Option: ',[1,2,3,4,5,6])
    if x == 1:
        printPlayerStats(id)
    elif x == 2:
        printStats(cadenainfo,id)
    elif x == 3:
        setBets()
    elif x == 4:
        standarRound(id,ma,players[id]['cards'],mace)


