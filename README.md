# Submission FLask API used here

Part 4 question 3
#Code walkthrough

The code consists of a app.py. Here the flask app runs and then there is a templates direactory where the html files are rendered from. 
Line 10-17 consists of all the configuration parameters and the successive lines consists of the db initialisation function to create all tables.
Then line 24-30 builds the model of the db. 

Then comes app route / in the helloworld function . This renders all the books in hello.html.

Lines 47-57 consists of the search get route . This route seraches for relevnt books based on the search query.
The next function is the post route in the / route to add a new book and its relevant featuress.

The html files in the templates directory are 2 in number. One for home and other for search. 


Part 4 question 1: The asynchronous nature of fast api allows the code to run in the background while simulataneously executing code rather than suspending functioning. 

