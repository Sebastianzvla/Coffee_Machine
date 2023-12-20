from Menu import MENU
from Menu import resources
from Menu import Art

V_Power = True
money = 0


def f_CompararRecursos(cafe):
    if cafe == "espresso":
        if resources["water"] - MENU[cafe]["ingredients"]["water"] >= 0 and resources["coffee"] - MENU[cafe]["ingredients"]["coffee"] >= 0:
            return "Suficiente"
        else:
            return "Insuficiente"
    else:
        if resources["water"] - MENU[cafe]["ingredients"]["water"] >= 0 and resources["milk"] - MENU[cafe]["ingredients"]["milk"] >= 0 and resources["coffee"] - MENU[cafe]["ingredients"]["coffee"] >= 0:
            return "Suficiente"
        else:
            return "Insuficiente"


# TODO 1. PREGUNTAR AL USUARIO QUE LE GUSTARIA TOMAR (espresso/latte/cappuccino) Y LOOP
while V_Power is True:
    print(Art)
    Orden = input("Que te gustaria tomar?, (espresso/latte/cappuccino) ☕: ").lower()
    # TODO 2. AGREGARLE UN BOTON DE OFF EN CASO DE QUERER APAGAR LA MAQUINA
    if Orden == "off":
        print("Apagando Equipo...\n")
        break
    # TODO 3. AGREGARLE LA VARIABLE DE REPORT PARA TENER EL REPORTE DE LA MAQUINA
    elif Orden == "reporte":
        print(f"Water: {resources["water"]}mL")
        print(f"Milk: {resources["milk"]}mL")
        print(f"Coffe: {resources["coffee"]}g")
        print(f"Money: ${money}")

# TODO 4. HAY SUFICIENTES RECURSOS PARA HACER LA BEBIDA ? SI NO VOLVER A PREGUNTAR
    elif f_CompararRecursos(Orden) == "Suficiente":
        print(f"El costo es de ${MENU[Orden]["cost"]}")
        print("Solo aceptamos 🪙 de 1, 2, 5, 10 Pesos y 💸 de 20, 50 y 100 Pesos")
        UnPeso = int(input("Cuantas 🪙 de 1 peso? "))
        DosPesos = int(input("Cuantas 🪙 de 2 peso? "))
        CincoPesos = int(input("Cuantas 🪙 de 5 peso? "))
        DiezPesos = int(input("Cuantas 🪙 de 10 peso? "))
        VeintePesos = int(input("Cuantas 💸 de 20 peso? "))
        CincuentaPesos = int(input("Cuantas 💸 de 50 peso? "))
        CienPesos = int(input("Cuantas 💸 de 100 peso? "))

        Dinero_Ingresado = UnPeso * 1 + DosPesos * 2 + CincoPesos * 5 + DiezPesos * 10 + VeintePesos * 20 + CincuentaPesos * 50 + CienPesos * 100
        # TODO 5. SE INGRESO SUFICIENTE DINERO ? SI NO REGRESAR EL DINERO, NO SERVIR Y VOLVER A PRGUNTAR
        # TODO 6. PROCESAR PAGO, REGRESAR CAMBIO Y REFLEJARLO EN EL REPORTE
        # TODO 7. PROCESAR PEDIDO Y REFLEJARLO EN LOS RECURSOS DANDO UN MENSAJE DE SERVIDO AL FINAL.
        if Dinero_Ingresado >= MENU[Orden]["cost"]:
            money += MENU[Orden]["cost"]
            Cambio = Dinero_Ingresado - MENU[Orden]["cost"]
            resources["water"] = resources["water"] - MENU[Orden]["ingredients"]["water"]
            if not Orden == "espresso":
                resources["milk"] = resources["milk"] - MENU[Orden]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU[Orden]["ingredients"]["coffee"]

            print(f"Aqui tienes tu {Orden}☕. Disfrutalo!!")
            print(f"Tu cambio es de ${Cambio}")

        elif Dinero_Ingresado < MENU[Orden]["cost"]:
            print("Dinero Insuficiente")

    else:
        print("Parece que no tenemos suficientes recursos para prepararlo, intenta con otra bebida")



