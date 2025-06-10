h = int(input())
m = int(input())
s = int(input())
t = int(input()) 

def validar():
    return ( not(h > 23) and not(m >= 60) and not(s >= 60))


while True:
    restricao = validar()
    # a cada uma hora vou retirar do t e colocar no h
    if t >= 3600:
        t -= 3600
        h += 1
        
    # mesma coisa das horas so que pra minutos

    elif t >= 60:
        t -= 60
        m += 1

    # so somei o resto dos segundos
    else:
        s += t
        t = 0
        
    # verificacao de horas, minutos e segundos 
    if h > 23:
        h = 0
        m = 0
        s = 0
        restricao = validar()
    if m >= 60:
        h += 1
        m = 0
        restricao = validar()
    if s >= 60:
        m += 1
        s -= 60
        restricao = validar()

    print(restricao)
    print(h)
    print(m)
    print(s)


    if((restricao) and (t == 0)):
        break
    else:
        continue
  


