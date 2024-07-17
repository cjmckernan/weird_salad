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

I've used grams for the ingredients in the builder to make it easier to add them. Also added a recipe delete will look into adding recipe editor. Will also have to take a look at the making the recipes names unique based on the location & recipe name. Added the cost to the 


## Point of Sale 

Finally I will add the point of sale app. This will allow the user to choose a recipe from a recipe lists and choose a radio button if its cash or card. If cash it will automatically check out and update the ingredients for the amounts used. Then will log the sale to a sales table. The sale table will have total cost, user who logged it if it was cash or card. I wont focus on the audit log for what is sold as of now. Will try to get this done first 

- Added the functionality to in the process sale method to check all the ingredients 

# Final 

I prioritised getting a lot of the features completed to make it an actual useful application. Due to this the system isn't as fault tolerant as I would like. The data isn't 100% sanitised and there are few other views I would of liked to complete to make the system more robust and prevent user from entering in bad data. 

## Running the application 

I have included a db with everything setup so you dont need to carry out the migrations or configure the data. It is in the db folder on in main directory simple move to the directory above and install requirements and you should be able to just use run command 


-Setup Virtual environment 

python3 -m venv .venv 
source .venv/bin/activate

-Install dependencies 

pip install -r requirements.txt

- DB Migrations Commands (if not using configure db)

python manage.py migrate 

-Run Command

python manage.py runserver


### Usernames for configured DB

Admin User 
-username : nory
-password : 1234

Normal Users:

-username : harry_grill
-password : Green1959

-username : barry_burger
-password : Green1959
