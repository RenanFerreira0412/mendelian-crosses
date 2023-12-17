from flask import Flask


def create_app():
    app = Flask(__name__)

    # Registrando blueprints
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
