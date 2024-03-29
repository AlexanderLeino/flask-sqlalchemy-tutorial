from flask import Flask
import os
from flask_cors import CORS
from api.route.flowerRoutes import flower


# Init App
app = Flask(__name__)
app.register_blueprint(flower)
cors = CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))

# fetched_URL = requests.get("https://beautiful-soup-4.readthedocs.io/en/latest/").content


# soup = BeautifulSoup(fetched_URL, features='html.parser')
# print(soup)

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Init db


# Init ma

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
