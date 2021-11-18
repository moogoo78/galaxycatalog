from flask import Flask

#from app.models import Specimen

def create_app():
    app = Flask(__name__)

    from app.main import main as main_bp
    app.register_blueprint(main_bp)
    @app.route('/')
    def index():
        #print (Specimen, 'ueueuuuee')
        return 'hello'
    return app
