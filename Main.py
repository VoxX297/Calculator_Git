from Division import *
from Suma import *
from SumaAvanzada import *
from Resta import *
from Multiplicacion import *


class Main():

    def calcMenu(self) -> int:
        
        print ("*****************************")
        print ("Suma ------------ 1")
        print ("Resta ----------- 2")      
        print ("Multiplicacion -- 3")   
        print ("Division -------- 4")
        print ("Suma avanzada --- 5")   
        
        

        try:
            a = int(input("Ingrese su opción (1-5): "))
            if 1 <= a <= 5:
                return a
            else:
                print("Opción no válida. Intente de nuevo.")
                return self.calcMenu()  
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")
            return self.calcMenu()  
    



        
    def run(self ):

        a = self.calcMenu()
        if a == 5:
            nums = input("ingresa los numeros separados por coma")
            lista_numeros = [int(num.strip()) for num in nums.split(",")]
            
        else:
            x = int(input("ingresa el primer numero: "))
            y = int(input("ingresa el segundo numero: "))
        if a == 1:
            suma = Suma().sumar(x, y)
            print(f"El resultado de la suma es {suma}")
        elif a == 2:
            resta = Resta().restar(x, y)  
            print(f"El resultado de la resta es {resta}")
        elif a == 3:
            producto = Multiplicacion().muliplicar(x, y)  
            print(f"El resultado de la multiplicación es {producto}")
        elif a == 4:
            division = Division().dividir(x, y)  
            print(f"El resultado de la división es {division}")
        elif a == 5:
            suma_avanzada = SumaAvanzada().sumarA(lista_numeros)
            print(f"El resultado de la suma avanzada es {suma_avanzada}")

        
if __name__ == "__main__":
    main = Main()
    main.run()