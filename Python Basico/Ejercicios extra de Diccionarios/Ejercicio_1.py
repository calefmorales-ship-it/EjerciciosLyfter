sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

sales_by_item= {}   

for sale in sales:  
    for item in sale['items']:  
        if item['upc'] not in sales_by_item: #not in se utiliza para verificar si la clave (en este caso, el upc del item) no existe en el diccionario sales_by_item, si no existe, se ejecuta el bloque de código dentro del if 
            sales_by_item[item['upc']] = 0 # sales_by_item[item['upc']] crea una key dinamicamente con el upc del item y le asigna un valor inicial de 0 
        sales_by_item[item['upc']] += item['unit_price'] # suma el precio del item a la key correspondiente en el diccionario sales_by_item
print(sales_by_item)