# Weird Salads

From the look at the requirements main features it needs to make it a useful application are below I will approach them in that order. 


1. User authentication
2. Inventory Management 
3. Recipe Builder
4. Point of Sale 


## User authentication

I will use the django abstract user and add a location id and a couple more flags to use if needed. The location id will allow me to filter per locations. 

## Inventory Management 

I will add an ingredients model that has a location id to identify it to its location making it easily filterable. The model will have name(which will be unique), quantity and a cost. I wont allow the user to add the cost yet as I've got to think about how it will do these calculations. This will all be under a django app called "stock"

