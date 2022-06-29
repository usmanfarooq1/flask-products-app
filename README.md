
# CRUD Api in Flask + RabbitMQ for persisting logs

This project is a simple Flask application showing the idea of basic CRUD. The project also uses
RabbitMQ for persisting the operation logs of the basic CRUD application. If any of the routes are 
hit or consumed, some of the information regarding the made request is saved in an sqlite database.
To demonstrate basic CRUD operations, sqlite database is used aswell.


## How To Start the project.

For starting the project, A basic assumption is made that on the machine to run the project a local rabbitMQ instant is running
on ```localhost``` with the default 'guest' username and password and default settings.

But the host of RabbitMQ could be changed by making a change in the .env file for variable
```RABBIT_MQ_HOST_NAME```. It defaults to 'localhost'. This ```.env``` file also contains the URI for the logs database ```LOGS_DATABASE_URI```.


Now for running the project just clone the repo first 

and

```cd  flask-products-app```

and run 

```./install.sh```

this will create a venv environment for the project and installs all the dependencies for the project and after that will firstly create the data base with the file name ```products.sqlite```
and start the server at ```localhost:5000```

After that start the rabbitMQ consumer in another terminal tab for saving the operations happening at the api.

From the project directory

```cd rabbitmq_consumer```

```source venv/bin/activate```

```python3 main.py```

and the consumer will start running waiting for the messages to consume.

### Routes

There are four routes 

[1]```GET /product```

it returns an array of product from the datbase

```
[
    {
        name:<product_name>,
        description:<product_description>,
        price:<product_price>,
        quantity:<product_quantity>
    }
    .
    .
    .
    .
]
```
[2] ```GET /product/<id>```

It returns a single product found by Id from the database. Takes a parameter [ Int ] in the url path.

```
    {
        id:<product_id>
        name:<product_name>,
        description:<product_description>,
        price:<product_price>,
        quantity:<product_quantity>
    }
```

[3] ```PUT /product/<id>```

JSON  Request Body for the updation of a single product by Id.  Takes a parameter [ Int ] in the url path.
```
{
        id:<product_id>,
        name:<product_name>,
        description:<product_description>,
        price:<product_price>,
        quantity:<product_quantity>
}
```

It returns the updated product in the result.

{
        id:<updated_product_id>,
        name:<updated_product_name>,
        description:<updated_product_description>,
        price:<updated_product_price>,
        quantity:<updated_product_quantity>
}


[4] ```DELETE /product/<id>```

It deletes a product from the database by Id. Takes a parameter [ Int ] in the url path.

and returns the name of the deleted product in the result.

{
        name:<updated_product_name>
}


[4] ```POST /product```
JSON Request Body for the creation of a product.
```
{
        name:<product_name>,
        description:<product_description>,
        price:<product_price>,
        quantity:<product_quantity>
}
```

It returns the newly created product in the result.

```
{       
        id:<new_product_id>,
        name:<new_product_name>,
        description:<new_product_description>,
        price:<new_product_price>,
        quantity:<new_product_quantity>
}
```

# RabbitMQ Consumer 

When the consumer is ran it will wait for the messages in the rabbitMQ queue as soon as some message is there to be consumed.
I used the default settings and credentials for rabbitMQ because there are alot to do for these settings.

The consumer will show the count of how many requests have been made yet for different HTTP METHODS to the API.



This covers everything, If there is still some this that I have not covered please feel free to contact me :)