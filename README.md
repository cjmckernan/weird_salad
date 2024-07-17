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

## Recipe Builder

Next up is the recipe builder. This will need two models one for the recipe name and another for the recipe ingredients. I will likely use the stock app as they are closely related and will reference each other. I will use some js to build the recipe and make a request to the back end to store it. 

I've used grams for the ingredients in the builder to make it easier to add them. Also added a recipe delete will look into adding recipe editor. Will also have to take a look at the making the recipes names unique based on the location & recipe name



