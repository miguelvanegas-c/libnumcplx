# EL NOMBRE DE LA LIBRERIA ES 'libnumcplx'

El proyecto es una libreria con las operaciones basicas de los numeros complejos.
Es necesario tener claro que los numeros complejos seran representados por tuplas, en
el primer valor de la tupla se encontrara el numero real y el segundo el numero imaginario.
1. La suma nombrada como sumaC, la cual recibe dos tuplas y devuelve el resultado de dicha suma en una sola tupla.
2. La multiplicacion nombrada como multiC, la cual recibe dos tuplas y devuelve el resultado de dicha multiplicacion en una sola tupla.
3. La resta funcion nombrada como restaC, la cual recibe dos tuplas y devuelve el resultado de dicha resta en una sola tupla.
4. La división nombrada como divisionC, la cual recibe dos tuplas y devuelve el resultado de dicha división en una sola tupla.
5. El modulo de un numero complejo, esta operacion recibe solo una tupla y devuelve un numero real.
6. El conjugado de un numero complejo, esta operacion recibe una tupla y devuelve otra tupla.
7. La fase de un numero complejo, esta operacion recibe una tupla y devuelve un numero real.
8. La conversion de complejo a polar, esta operacion recibe una tupla y devuelve otra tupla.
9. La conversion de polar a complejo, esta operacion recibe una tupla y devuelve otra tupla.

## COMO INSTALAR

## COMO USAR LA LIBRERIA

Se realiza la descarga del archivo 'libnumcplx.py', se guarda en un folder junto con el archivo que se este trabajando,
se hara su importacion de la siguiente forma.

import libnumcplx

De esta forma se tendra acceso a todas las funciones de la libreria, a las cuales se accederan de la siguiente forma

import libnumcplx as lc
print(lc.sumaC((1,2),(1,2)))

(2,4)

(PARA CADA FUNCION TENER EN CUENTA EL TIPO QUE EXIGE LA FUNCION)

## COMO PROBAR LA BIBLIOTECA

Junto con el archivo de la libreria se descargara el archivo 'test_complejos', que incluira un conjunto de pruebas 
automaticas, donde se prueban cada una de las funciones de la libreria.
Se puede correr el archivo completo, lo cual dara la siguiente salida.

Ran 9 tests in 0.002s

OK

De otra forma sera posible correr funcion por funcion el codigo, asi se comprobara cada una de ellas.
Cada funcion tuvo dos pruebas, donde primero se hacia la prueba con numeros enteros y despues con numeros que no fueran enteros,
con la intencion de que no se encontrar algun fallo por el tipo de los datos.

## NOTAS EXTRAS

- El codigo esta fundamentado en las formulas ya existentes para operar numeros complejos, al tener cada una de las 
formulas al alcance de la mano, solo fue necesario traducirlas a codigo.
- Con la libreria se busca facilitar el manejo de numeros complejos en python, manejandolos en tuplas.

## VERSION
version 1.0.0

## AUTOR
Miguel Angel Vanegas Cardenas





