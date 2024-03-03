from flask import Flask, request,session, render_template

from flask import  Response, jsonify, json, make_response
from flask_cors import CORS, cross_origin

from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = 'my_secret_key'
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BOOKS_PER_PAGE'] = 10  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    pubyear = db.Column(db.String(100), nullable=False)
    review = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(100), nullable=False)



@app.route("/",methods=['GET'])
def hello_world():

    page = request.args.get('page', 1, type=int)


    page = request.args.get('page', 1, type=int)
    books = Book.query.paginate(page, app.config['BOOKS_PER_PAGE'], False)
    return render_template('home.html', books=books)




@app.route("/search", methods=['GET'])
def search_books():
    page = request.args.get('page', 1, type=int)
    query = request.args.get('query', '')

    search_query = f"%{query}%"
    books = Book.query.filter(
        (Book.title.ilike(search_query)) | (Book.author.ilike(search_query))
    ).paginate(page, app.config['BOOKS_PER_PAGE'], False)

    return render_template('search.html', books=books, query=query)

@app.route("/",methods=['POST'])
def hello_world2():
    title = request.form["title"]
    pubyear = request.form["pubyear"]
    author = request.form["author"]
    shortreview = request.form["shortreview"]
    rating = request.form["rating"]
    # print(data)
    # print(data1)
    # print(data2)
    new_book = Book(title=title, author=author,pubyear = pubyear,review=shortreview,rating=rating)
    db.session.add(new_book)
    db.session.commit()
    print('Book added successfully!')

    page = request.args.get('page', 1, type=int)
    books = Book.query.paginate(page, app.config['BOOKS_PER_PAGE'], False)
 
    return render_template("home.html",books=books)




if __name__ == '__main__':
 
    app.run()
