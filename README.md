# WebProject
Web App develop for Web Project made by Daniel, Agapito, Aaron, Benjami and Roger.

## Initial problem
Our idea is to implement a web application to manage the warehouse of a repair company that
specializes in electronics (mainly in Tvs, Pcs and Mobile phones) and also mechanical parts (such as
motor parts and robotic parts). 

In the warehouse, the technicians are assigned to the different tasks that
the company is involved, whether they are for general repairs or maintenance.
In the warehouse you will find a whole catalog of spare parts so that the technicians have enough tools
available to carry out the work as soon as possible. Therefore, they also have different companies that
supply material to the store depending on the orders that the accounting section performs.

The problem is that the technicians are complaining that there is no order or an organized way to know
what parts are in the store, and have to make a trip back to this one for nothing.
For this reason, the company has hired us to create a web application that facilitates the technicians to
perform a search of pieces in an optimal way.

## Key points of the functionality of the App

+ The web application will have to show a catalog of the pieces of the store with the important information to
facilitate the search.
+ The web application should have a search engine to incorporate filters to find models or specifications of
the pieces.
+ The web application will have to let modify the quantity of stock of each piece, both for technicians and for
supply companies.
+ The web application will get information from the Amazon API to get the names and descriptions for the
different pieces in the catalog.
+ The web application will have different user groups that will have different credentials over the software.

## Databases for the Job
    Models
      CatalogChange: For the changes in the warehouse
      Product: the list od products in the warehouse
      Category: the identifing categories of the products

    Product:
        product_id: id of a product
        category_id: a foreign key to Category that indicates which category is the product
        brand: the brand of said product
        model: the type of model corresponding to the product
        description: short description of the product
        product_type: specific type depending on the product (RAM DDR3 or DDR4, etc.)
        quantity: the quantity in the warehouse of said product
        
    Category:
        category: name of a category that's inside the type
        department_type: name of the type of departament
        department: name of a department
        
    CatalogChange:
        product_id_change: the id of the changed product
        category_id_change: the category of the changed product 
        quantity_modify: the quantity modified
        date: when it happened

## Checklist of implemented funcionalities:
### First Deliverable:
- [X] Models: created and revised for better functionality
- [x] Admin: activated and possible to midify the database
- [x] Login: login system with users and user administration with forms
- [x] Heroku deployment
- [x] Docker deployment
- [x] Multiserver planning

#### Admin access

For checking the admin and the functionality of the admin, please use the following information:

    Username: admin
    Password: 123456

#### Login implementation

In order to make a login that will work with our vision, we have used *crispy forms* for better coding, better view callings
and better HTML in general. Also, it works perfectly with Django User system.
#### Heroku deployment

There's already a deployment made with the app, you can find it in:

[Heroku website](http://web-project-warehouse.herokuapp.com/)

#### Docker deployment

For docker, we recommend to clone the repository and check de Dockerfile and docker-compose.yml, we are able to create
a container for this one using *sudo docker compose run* and executing the different commands, so we are certain that it is
possible.

#### Multiserver planning

One of the requirements for the first deliverable was to create a plan in which we proposed a multiserver deployment of our app, in which
we needed to specify number, functionality and dependences in said network.

For said planning, we will create 3 tiers: the Web tier, the App tier and the Database tier.

First, you have the **Web tier**. Said tier will be a server dedicated to reciving request from the users and sending the requested information. It will be the most Client based tier do to the direct connection with the possible users.

Secondly, you have the **Application tier**, said tier will process the Web tier sends it's ways, send request to the Database tier and send the response back to the Web tier. Here will have another server.

Finnaly, there's the **Database tier**, capable of holding all of the information for our Web App and recieving querrys to answer. Yet another container in a server or several containers in different servers(possibly one for every type of model that we have in the app) will be created for said tier.

Additionally, there can be another separated group of containers that have the scripts necessary for the functionality of our App.

![Server Diagram](/Captura_server_diagram.PNG)
