import logging

from flask import request
from flask_restplus import Resource

from ..services.detect import execute
from ...restplus import api
from ..serializers import *

log = logging.getLogger(__name__)
ns = api.namespace('text')


@ns.route('/detect')
class LanguageDetectionResource(Resource):
    @api.expect(detect_text_request)
    @api.response(200, 'Success', detect_text_response)
    @api.response(500, 'Internal Server Error', vnd_error_schema)
    def post(self):
        """
        Detects from a given text the language it has been written in.
        """
        if not request.json:
            return self._build_bad_json_response()

        success, response = execute(request.json)

        return response, 200

    @staticmethod
    def _build_bad_json_response():
        response = {
            "_embedded": {
                "errors": [
                    {
                        "message": "Provided input is not valid JSON.",
                        "path": "/"
                    }
                ]
            },
            "total": 1
        }
        return response, 400
