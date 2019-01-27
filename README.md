# ElectroExpress API

## Consultar stock:

`http://127.0.0.1:5000/stock`

Parámetros:

- `device`: filtrar por dispositivo (`http://127.0.0.1:5000/stock?device=mobile`)
- `brand`: filtrar por marca (`http://127.0.0.1:5000/stock?brand=apple`)
- `price_lowereq`: filtrar por precio menor o igual (`http://127.0.0.1:5000/stock?price_lowereq=200`)


## Realizar compras

`http://127.0.0.1:5000/buy`


Parámetros:

- `id`: indicar la id del producto que se quiere comprar (`http://127.0.0.1:5000/buy?id=1`)
- Si se quieren comprar más de un artículo, separar las ids por `:` 
(`http://127.0.0.1:5000/buy?id=1:2:3`)

Devuelve:

Genera un ticket de compra (diccionario de lista), con un número de ticket 
compuesto por fecha y hora de la compra y una de las ids de los artículos comprados:
`{
  "20190126131626": [
    "2", 
    "5"
  ]
}`

En caso se introducir una id de un producto no existente en el stock, devuelve 
un diccionario vacío como motivo de no poder realizar la compra: `{}`

## Consultar compras

`http://127.0.0.1:5000/purchases`

Devuelve:

Diccionario de diccionarios de los distintos tickets generados al hacer compras.

## Realizar devoluciones 

`http://127.0.0.1:5000/remove`

Parámetros:

- `bill_number`: indicando el número de ticket de la compra, se elimina dicha
compra de lista de compras. (`http://127.0.0.1:5000/remove?bill_number=20190126131626`)
- `id`: indicando, además del número de ticket, el id del producto a devolver, 
se retira de la lista de productos comprados el indicado.
(`http://127.0.0.1:5000/remove?bill_number=20190126131626&id:2`)

Devuelve:

Devuelve la lista de las compras (dicionario de listas) una vez eliminado lo 
indicado (ticket entero o artículo concreto)
