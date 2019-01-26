# ElectroExpress API

## Consulatar stock:

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

## Realizar devoluciones 

`http://127.0.0.1:5000/return`

Parámetros


Devuelve

