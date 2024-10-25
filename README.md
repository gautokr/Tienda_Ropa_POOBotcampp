# Tienda_Ropa_POOBotcampp
POO Practice by making a clothing store system

Este sistema de compras aplica los 4 pilares de la programación orientada a objetos con el objetivo de generar un programa en el cual los usuarios puedan ver prendas disponibles en una tienda, elegir entre ellas para almacenarlas en su carrito según la cantidad deseada, y luego procesar su compra, visualizando un resumen de los productos y costo total de las elecciones al final. Igualmente, lo pueden visualizar a medida que van agregando sus productos para verificar que el total esté dentro de su presupuesto estimado.

Al iniciar, el programa muestra el inventario con un mensaje de bienvenida. Posteriormente, pregunta al usuario qué prenda desea adquirir. También se presentan opciones en caso de que desee ver el carrito o salir del programa.
- En caso de colocar el nombre de una prenda, se pide también la cantidad. Después se vuelve al menú.
- Si se introduce "carrito", se pueden ver detalles de los productos y costos.
- En caso de "salir", se muestra el proceso anterior. Luego el programa cierra.

Se utilizan las siguientes clases: Producto, Ropa (hereda de Producto), Camisa, Pantalón y Zapato (heredan de Ropa), Tienda y Carrito.
1. Producto representa cada producto de la tienda, conteniendo información de nombre, precio y cantidad, con métodos que accionan con los atributos.
2. Ropa contiene los atributos y métodos de Producto, pero se añade "Talla".
3. Las clases de prendas específicas añaden un nuevo atributo, "Tipo de Tela".
4. La clase Tienda sirve para el menú principal, es el inventario que se muestra a la bienvenida, donde se almacenan los productos. Además, permite añadir nuevas prendas.
5. Carrito es una clase donde se pueden agregar productos del inventario, de Tienda, dependiendo de lo que se desee comprar. Adicionalmente, aquí se calculan los totales para cada usuario, retornando un resumen con detalles en caso de ingresar al carrito o antes de finalizar la compra.
   
Para que el programa funcione de modo deseado y se cierre cuando el usuario lo dicte, se utiliza un bucle While con condicionales if, mientras que para manejo de errores se utiliza dentro un bucle try.
