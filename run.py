import MySQLdb
from flask import Flask
from flask import jsonify
app = Flask(__name__)

def get_book_list():
	# Connect
	db = MySQLdb.connect(host="localhost",
			     user="root",
			     passwd="",
			     db="librarymanagement")

	cursor = db.cursor()

	# Execute SQL select statement
	cursor.execute("SELECT * FROM books")

	# Commit your changes if writing
	# In this case, we are only reading data
	# db.commit()

	# Get the number of rows in the resultset
	numrows = cursor.rowcount
	book_list = {}
	# Get and display one row at a time
	for x in range(0, numrows):
	    row = cursor.fetchone()
	    print (row[0], "-->", row[1])
	    book_list[row[0]] = row[1]

	# Close the connection
	db.close()
	return book_list

@app.route('/')
def hello():
    return "welcome to world of IT solutions!"
@app.route('/booklist')
def booklist():
    return jsonify(get_book_list()) 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
