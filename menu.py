import os


def mostrarmenu(opciones):
        while(True):
            os.system("clear")
            for item in opciones:
                print(item)


    
            opcion = input("digite opcion")
   


            if opcion == "1":
                os.system("clear")
                print("esta es la opcion 1")



            elif opcion == "2":
                os.system("clear")
                print("esta es la opc 2")
                input("digite una tecla para continuar")


            elif opcion == "3":
                os.system("clear")
                print("esta es la opc 3")
                input("digite una tecla para continuar")

            
            
            elif opcion == "s":
                os.system("clear")
                input("digite una tecla para salir")


                








def menu():
    opciones ={
    "menu principal",
    "1 agregar empleado",
    "2 listar empleado",
    "3 eliminar empleado",
    "s. SALIR"
    }


    mostrarmenu(opciones)


def main():
    menu()






if __name__ == "__main__":
    main()










