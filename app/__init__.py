import os
from flask import Flask, url_for, render_template, send_from_directory
app = Flask(__name__)

# ...

# Blueprints
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

# Setup favicon route
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# ...

if __name__ == "__main__":
    app.run()
