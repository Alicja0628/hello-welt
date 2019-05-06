while True:
    print("Aby wyświetlić informacje o autorze wciśnij 'a'")
    print("Aby wyświetlić liczby od 50 do 150, które są podzielne przez 3 i niepodzielne przez 5 wciśnij 'p'")
    print("Aby wyświetlić wiersz 7 tabliczki mnożenia wiśnij 'r'")
    print("Aby wyświetlić wiersz 5 tabliczki mnożenia wciśnij't")
    print("Aby zakończyć program wciśnij 'q'")
    znak = input()
    if znak == "a":
        print("Alicja Kowalczyk, 19 lat")
    elif znak == "p":
        x=50
        while x>=50 and x<=151:
            x=x+1
            if x%3==0 and x%5!=0:
                print(x)
    elif znak =="r":
        n=1
        for i in range (7,8):
            for n in range (1,11):
                print(n,"*",i,"=",n*i)
    elif znak == "t":
        i=0
        n=5
        while i>=0 and i<=9:
            i=i+1
            print(n,"*",i,"=",n*i)
    elif znak =="q":
        break
    else:
        print("Błąd!")
        
    print("Fajne repo, trzymaj tak dalej")
