# app.py
from flask_swagger_ui import get_swaggerui_blueprint
from routes.route import routes
from routes.route import app
from models.model import db
app.register_blueprint(routes)

SWAGGER_URL = '/api/docs'  # URL для Swagger UI
API_URL = '/swagger_json'  # URL для вашей OpenAPI-спецификации

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "web api project"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
if __name__ == '__main__':
    app.run(debug=True)