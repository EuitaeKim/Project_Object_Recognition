from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate()

def create_app() :
    app = Flask(__name__, template_folder = 'Template')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///ulsan_info.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    Bootstrap(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from flask_app.routes import main_routes
    app.register_blueprint(main_routes.bp)

    return app

if __name__ == "__main__" :
    app = create_app()
    app.run(debug = True)