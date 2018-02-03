import logging.config

from flask import Flask, Blueprint
from flask_restplus import Swagger
import settings
from api.restplus import api
from api.translation.endpoints.languages import ns as languages_namespace
from api.translation.endpoints.detection import ns as text_detection_namespace
from api.translation.endpoints.translation import ns as text_translation_namespace

app = Flask(__name__)
Swagger(app)
log = logging.getLogger(__name__)

# ----------------------------------------------------------------------------

blueprint = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprint)

# ADD ENDPOINTS
api.add_namespace(text_translation_namespace)
api.add_namespace(text_detection_namespace)
api.add_namespace(languages_namespace)
# END ENDPOINTS


app.register_blueprint(blueprint)

# ----------------------------------------------------------------------------

app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
app.config['SWAGGER_UI_ENABLED'] = settings.SWAGGER_UI_ENABLED

