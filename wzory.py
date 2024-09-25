import math
while True:
    print("liczymy obwod i pole kwadratu, podaj bok a")
    a = float(input())
    if a>0:
        pole = a*a
        obwod = a*4
        print(f"obwod kwadratu wynosi: {obwod}, a pole wynosi: {pole}")
        break
    else:
        print("podales bledna wartosc boku")

while True:
    print("liczymy obwod i pole prostokat, podaj bok a"); 
    a = float(input())
    print("podaj bok b")
    b = float(input())
    if a>0 and b>0:
        pole = a*b
        obwod = 2*a + 2*b
        print(f"obwod prostokatu wynosi: {obwod}, a pole wynosi: {pole}")
        break
    else:
        print("podales bledna wartosc boku")

while True:
    print("liczymy obwod i pole rownolegloboku, podaj bok a"); 
    a = float(input())
    print("podaj bok b")
    b = float(input())
    print("podaj wysokosc h")
    h = float(input())
    if a>0 and b>0 and h>0:
        pole = a*h
        obwod = 2*a + 2*b
        print(f"obwod rownolegloboku wynosi: {obwod}, a pole wynosi: {pole}")
        break
    else:
        print("podales bledna wartosc boku")

while True:
    print("liczymy obwod i pole trapezu, podaj bok a"); 
    a = float(input())
    print("podaj bok b")
    b = float(input())
    print("podaj bok c")
    c = float(input())
    print("podaj blok d")
    d = float(input())
    print("podaj wysokosc h")
    h = float(input())
    if a>0 and b>0 and h>0 and c>0 and d>0:
        pole = ((a+b)*h)/2
        obwod = a+b+c+d
        print(f"obwod trapezu wynosi: {obwod}, a pole wynosi: {pole}")
        break
    else:
        print("podales bledna wartosc boku")

while True:
    print("liczymy obwod i pole trojkata, podaj bok a"); 
    a = float(input())
    print("podaj bok b")
    b = float(input())
    print("podaj bok c")
    c = float(input())
    print("podaj wysokosc h")
    if a>0 and b>0 and c>0 and h>0:
        pole = (a*h)/2
        obwod = a+b+c
        print(f"obwod trojkata wynosi: {obwod}, a pole wynosi: {pole}")
        break
    else:
        print("podales bledna wartosc boku")
    
while True:
    print("liczymy obwod i pole trojkata rb, podaj bok a"); 
    a = float(input())
    if a>0:
        pole = (a**2*(math.sqrt(3)))/4
        obwod = a*3
        print(f"obwod trojkata rb wynosi: {obwod}, a pole wynosi: {pole}")
        break
    else:
        print("podales bledna wartosc boku")

while True:
    print("liczymy obwod i pole kola, podaj promien r"); 
    r = float(input())
    if r>0:
        pole = (math.pi)*r**2
        obwod = 2*(math.pi)*r
        print(f"obwod kola wynosi: {obwod}, a pole wynosi: {pole}")
        break
    else:
        print("podales bledna wartosc promiena")

while True:
    print("liczymy obwod i pole rombu, podaj bok a"); 
    a = float(input())
    print("podaj przekanta e")
    e = float(input())
    print("podaj przekanta f")
    f = float(input())
    print("podaj wysykosc h")
    h = float(input())

    if a>0 and h>0 and e>0 and f>0:
        pole = a*h or (e*f)/2
        obwod = a*4
        print(f"obwod rombu wynosi: {obwod}, a pole wynosi: {pole}")
        break
    else:
        print("podales bledna wartosc boku")

while True:
    print("liczymy pole powierzchni i objetosc szescianu, podaj krawedz a"); 
    a = float(input())
    if a>0:
        Pp = 6*a**2
        objetosc = a**3
        print(f"objetosc wynosi: {objetosc}, pole powierzchni wynosi: {Pp}")
        break
    else:
        print("podales bledna wartosc krawedzi")


while True:
    print("liczymy pole powierzchni prostopadloscianu, podaj krawedz a"); 
    b = float(input())
    print("podaj krawedz b")
    b = float(input())
    print("podaj krawedz c")
    c = float(input())
    if a>0 and b>0 and c>0:
        Pp = (2*a*b)+(2*a*c)+(2*b*c)
        objetosc = a*b*c
        print(f"objetosc wynosi: {objetosc}, pole powierzchni wynosi: {Pp}")
        break
    else:
        print("podales bledna wartosc krawedzi")

while True:
    print("liczymy pole powierzchni graniastoslupu, podaj krawedz a"); 
    a = float(input())
    print("podaj wysokosc h")
    h = float(input())
    if a>0 and h>0:
        pp=a*a
        pb =(4*a)*h
        Pp =(2*pp)+pb
        objetosc=(pp*h)/3
        print(f"objetosc wynosi: {objetosc}, pole powierzchni wynosi: {Pp}")
        break
    else:
        print("podales bledna wartosc krawedzi")

while True:
    print("liczymy pole powierzchni i objetosc ostroslupa, podaj krawedz a"); 
    a = float(input())
    print("podaj wysokosc h")
    h = float(input())
    if a>0 and h>0:
        pp = a*a
        pb= (4*a)*h
        Pp = pp+pb
        objetosc = (pp*h)/3
        print(f"objetosc wynosi: {objetosc}, pole powierzchni wynosi: {Pp}")
        break
    else:
        print("podales bledna wartosc krawedzi")

while True:
    print("liczymy pole powierzchni i objetosc walca, podaj promien r"); 
    r = float(input())
    print("podaj wysokosc h")
    h = float(input())
    if r>0 and h>0:
        Pp = (2*(math.pi)*r**2)+(2*(math.pi)*r*h)
        objetosc = ((math.pi)*r**2)*h
        print(f"objetosc wynosi: {objetosc}, pole powierzchni wynosi: {Pp}")
        break
    else:
        print("podales bledna wartosc promienia")

while True:
    print("liczymy pole powierzchni i objetosc szescianu, podaj promien r"); 
    r = float(input())
    print("podaj wysokosc h")
    h = float(input())
    if r>0 and h>0:
        l = 2*(math.pi)*r
        Pp = ((math.pi)*r**2)+((math.pi)*r*l)
        objetosc = ((math.pi)*r**2*h)/3
        print(f"objetosc wynosi: {objetosc}, pole powierzchni wynosi: {Pp}")
        break
    else:
        print("podales bledna wartosc promienia")

while True:
    print("liczymy pole powierzchni i objetosc szescianu, podaj promien r"); 
    r = float(input())
    if r>0:
        Pp = 4*((math.pi)*r**2)
        objetosc = (4/3)*(math.pi)*r**3
        print(f"objetosc wynosi: {objetosc}, pole powierzchni wynosi: {Pp}")
        break
    else:
        print("podales bledna wartosc promienia")

while True:
    print("twierdzenie pitagorasa, podaj bok a"); 
    a = float(input())
    print("podaj bok b")
    b = float(input())
    if a>0 and b>0:
        tp = (math.sqrt(a**2+b**2))
        print(f"bok c wynosi: {tp}")
        break
    else:
        print("podales bledna wartosc boku")

while True:
    print("przekatna, podaj bok a"); 
    a = float(input())
    if a>0:
        pk = a*(math.sqrt(2))
        print(f"przekanta kwadratu wynosi: {pk}")
        break
    else:
        print("podales bledna wartosc boku")

while True:
    print("liczymy wysokosc troj rb, podaj bok a"); 
    a = float(input())
    if a>0:
        wtr = (a*(math.sqrt(3)))/2
        print(f"wysokosc troj rb wynosi: {wtr}")
        break
    else:
        print("podales bledna wartosc boku")