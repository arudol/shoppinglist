# shoppinglist
An editable web-browser shoppinglist, written in python using Flask and html templates. 
Important: The app expects a MongoDB database reachable under locally at port 27017. Easiest way of providing this is using Docker Desktop with whatever available MongoDB image. Make sure to configure the ports correctly, and activate before running the application with `python app.py`. The app will be available under 'http://127.0.0.1:8000/'.

If you want to delete all entries in the database, execute `python delete_all_entries_database.py`.

# requirements
To install required python packages, run `pip install -r requirements.txt` in the python environment, which will install flask and pymongo.
