#Import the petfax folder as a package
from petfax import create_app

#The application factory function: an app instance
#Invoking the function an saving it to a variable called app
#app instance with all the custom logic already loaed into it.

app = create_app()
