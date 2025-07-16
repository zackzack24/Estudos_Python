dia = int(input("Digite o número do dia da semana:"))

'''' 
 
if dia == 1 :
    print("Hoje é domingo")
elif dia == 2 :
    print("Hoje é segunda-feira")
elif dia == 3 :
    print("Hoje é terça-feira")
elif dia == 4 :
    print("Hoje é quarta-feira")
elif dia == 5 :
    print("Hoje é quinta-feira")
elif dia == 6 :
    print("Hoje é sexta-feira")   
elif dia == 7 :
    print("Hoje é sábado")
else:
    print("Esse dia não existe")

''' 

match dia :
    case 1:
        print("Domingo")
    case 2:
        print("segunda-feira")
    case 3:
        print("terça-feira")
    case 4:
        print("quarta-feira")
    case 5:
        print("quinta-feira")
    case 6:
        print("sexta-feira")
    case 7:
        print("sábado")
    case other:
        print("Esse dia não existe")
