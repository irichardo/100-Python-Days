# Sell tickets
def sell_tickets():
    print("Welcome to the ticket office!")
    question = input("Quieres comprar un boleto?: ")
    amount = 0
    if question.lower() == "si":
        age = int(input("Introduce tu edad: "))
        if age < 18:
            amount += 3
            print(f"Tienes que pagar {amount}$")
        elif 18 < age < 50:
            amount += 5
            print(f"Es un boleto para adulto son {amount}$")
        elif age > 60:
            amount += 0
            # Return the Message because it's not necessary print the message about cost.
            return print("Eres un adulto mayor, tienes el beneficio de entrar gratis!")
        print(f"Por favor haz el siguiente pago {amount}")
    else:
        print("Gracias por usar nuestro servicio!")


sell_tickets()
