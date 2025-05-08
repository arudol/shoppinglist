from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient  
import os
from forms import InputForm, RemoveForm
import ast
import argparse

app = Flask(__name__)

#Set up MongoDB client. 
# The MongoDB URI is fetched from the environment variable 'MONGODB_URI'
# If not found, it defaults to 'mongodb://localhost:27017/'
client = MongoClient(os.environ.get("MONGODB_URI", "mongodb://localhost:27017/"))

# connect to database "athome" from the client
athome = client.athome
# from athome database, access shopping collection
shoppinglist = athome.shopping

@app.route("/")
def index():
    # Convert the documents to a list, excluding the '_id' field
    data = list(shoppinglist.find({}, {"_id": 0}))
    # Return the data as a JSON response with status code 200 (OK)
    return render_template('table_clickable.html', data=data), 200


# first possibility: get and post in a single method
@app.route("/add", methods=('GET', 'POST'))
def add_entry():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        # Insert the data into the 'data' collection in MongoDB
        shoppinglist.insert_one({"item":form.item.data, 
                                 "shop":form.shop.data, 
                                 "comment":form.comment.data})
        # redirect to the main page with the updated list
        return redirect(url_for('index'))
    return render_template('add.html', form=form) 


@app.route('/remove_single_item/', methods=['GET', 'POST'])
def remove_single_item():
    # return is a string, convert to dict firsts
    data = ast.literal_eval(request.form['entry'])
    shoppinglist.delete_many(data)
	# add the rest of your code here.
    return redirect(url_for('index'))

@app.route('/remove_all_from_shop/', methods=['GET', 'POST'])
def remove_all_from_shop():
    shop = request.form['shop']
    data = {'shop':shop}
    shoppinglist.delete_many(data)
	# add the rest of your code here.
    return redirect(url_for('index'))


## If remove is on single page. Not in use currently
# second possibility: get and post separately 
@app.post("/remove")
def remove_post():
    # If the request method is POST, get the JSON data from the request
    form = RemoveForm(request.form)
    if form.validate():
        data = {}
        if form.item.data:
            data['item'] = form.item.data
        if form.shop.data:
            data['shop'] = form.shop.data
        
        if data:
            shoppinglist.delete_many(data)
    # redirect to the main page with the updated list
    return redirect(url_for('index'))

@app.get("/remove")
def remove_get():
    form = RemoveForm(request.form)
    return render_template('remove.html', form=form)   





if __name__ == "__main__": 
    parser = argparse.ArgumentParser(
                        prog='ProgramName',
                        description='What the program does',
                        epilog='Text at the bottom of help')
    parser.add_argument('--host')      # option that takes a value
    args, leftovers = parser.parse_known_args()

    if args.host is not None:
        app.run(host=str(args.host), port=8000)
    app.run(port=8000)