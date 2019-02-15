#Compilador-Procesador---Digitales-III
Compilador para un procesador basado en set de instrucciones, y un archivo de codigo (solo una operacion por linea), la sintaxys parecida a C (debido a que todos los datos son entero no es necesario poner ->int<- para crear las las variables EJ1 linea1>> a=1; EJ2 linea2>> persona=12-a)

##Descargar:
    Para descargar el proyecto solo basta con usar el siguiente link
    - ```https://github.com/ANDRESHZ/Compilador-Procesador---Digitales-III/archive/master.zip```
    O
    - ```git clone https://github.com/ANDRESHZ/Compilador-Procesador---Digitales-III```

    Al desconprimir les quedar aun carpeta conteniendo todo el codigo y archivos
##USO:
    - Para realizar el correcto uso se desconprime y se accede a esa carpewta usando cd.
    - Deben editar ("set.txt") o en su defecto crear los archivo de set de instruccionesw qeu siga la norma EJEMPLO:
    ###Set de instrucciones:
        -Debe ser hecho en un archivo .txt
        -La primera instruccion 00000 debe ser "INICIO"
        -La segunda instruccion 00001 debe ser "="
        -La ultima instruccion 11111 debe ser "FIN"
        -Las instrucciones vacias (no usadas) poner la palabra "NAN"
        -Usar los simbolos de operaciones normales no palabras (+,-,*,/,&,|,^,%,...)
        -La instruccion de resta (si la va incluir en su set) debe ir antes que la se suma EJ  
        ```
            ...
            00110:-
            ...
            11011:+
            ...
        ```
        -Un ejemplo esta en el archivo "set.txt", pueden modificarlo o crear otro archivo con otro nombre:
        ```
            00000:INICIO
            00001:=
            00010:-
            00011:+
            00100:-
            00101:/
            00110:%
            00111:==
            01000:>
            01001:<
            01010:!=
            01011:&
            01100:|
            01101:!
            01110:^
            01111:jump
            10000:NAN
            10001:NAN
            10010:NAN
            10011:NAN
            10100:NAN
            10101:NAN
            10110:NAN
            10111:NAN
            11000:NAN
            11001:NAN
            11010:NAN
            11011:NAN
            11100:NAN
            11101:NAN
            11110:NAN
            11111:FIN
        ```
    ###Codigo a compilar:
        -Debe ser hecho en un archivo .txt
        -Debe comenzar con la plabra "INICIO:"
        -Debe finalizar con la palabra "FIN;"
        -Cada linea Finaliza con ";"
        -Para poner comentarios use "//" ejemplo:
        ``` 
            //esto es un comentario debe se puesto en un a linea solito
            t=29; // estos tambien se pueden usar
        ```    

        -Para inicializar variables NO debe usar la palabra reservada int, Solo poner el nombre de la variable que desea Ejemplo:
        ```
            num=1;
            paso=-5;
            perro=paso-num;
        ```
        -Maximo dos datos por operacion Ejemplo:
        ```
            xa=12;
            d=xa-4;
            dass=12%d;
            x=d/dass;
        ```
        -NO PONER ESPACIOS VACIOS ENTRE LINEAS.
            
    ###Ejecutar el archivo "Compilar.py":
        Para su unicamente deben entrar a la carpeta descompresa "compilar" dentro de donde se descargo
        - ```cd /Compilador-Procesador---Digita.../les-III-master/compilar/```
        para ejecutar usar : "python Compilar.py <nombre Codigo>.txt <nombre Set Instrucciones>.txt", para ejecutarlo reemplazar por los nombres que uds quieran en orden, por ejemplo los archivos que estan a l lado seria:       
        - ```python Compilar.py cod.txt set.txt```

 
