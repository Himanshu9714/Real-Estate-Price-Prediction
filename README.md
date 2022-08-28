# Real Estate Price Prediction

#### Create virtual environment

<pre>python -m venv venv</pre>

#### Activate virtual environment

<pre>venv\Scripts\activate</pre>

#### Install requirements

<pre>pip install -r requirements.txt</pre>

#### Run Jupyter Notebook

<pre>jupyter notebook</pre>

#### Note

If jupyter notebook raises an module error then you can also install the module manually by running `%pip install module_name` in the notebook.

#### Flask Server Setup

Setup the App:

    Windows: set FLASK_APP=server/server.py
    MacOS:   export FLASK_APP=server/server.py

Run the Server:

    flask run
