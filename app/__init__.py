from flask import Flask

from .api.v1 import blueprint as api_v1_bp

app = Flask(__name__)
app.register_blueprint(api_v1_bp)
