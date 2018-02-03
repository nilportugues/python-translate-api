import logging

from flask_restplus import Resource
from googletrans.constants import LANGUAGES
from ...restplus import api
from ...translation.serializers import *

log = logging.getLogger(__name__)
ns = api.namespace('text')


language_list = api.model('language_list', {
    'languages': fields.Raw(LANGUAGES, required=True)
})


@ns.route('/languages')
class LanguagesResource(Resource):
    @api.response(200, 'Success', language_list)
    def get(self):
        """
        Returns a key-value list with all the supported languages.
        """
        return {'languages': LANGUAGES}, 200

