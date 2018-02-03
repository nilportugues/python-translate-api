import logging

from flask import request
from flask_restplus import Resource

from ..services.translate import TranslationService
from ...restplus import api
from ...translation.serializers import *

log = logging.getLogger(__name__)
ns = api.namespace('text')


@ns.route('/translate')
class TranslationResource(Resource):

    @api.expect(translated_text_request)
    @api.response(200, 'Success', translated_text_response)
    @api.response(400, 'Bad Request', vnd_error_schema)
    @api.response(500, 'Internal Server Error', vnd_error_schema)
    def post(self):
        """
        Translates a text from an input language to an output language.
        """
        if not request.json:
            return self._build_bad_json_response()

        service = TranslationService()
        success, response = service.execute(request.json)

        if not success:
            return self._build_bad_request_response(response)

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


    @staticmethod
    def _build_bad_request_response(response):

        # loop errors
        errors = []
        for key, value in response.items():
            error = {'message': value, 'path': '/' + key}
            errors.append(error)

        # build response
        response = {
            "_embedded": {
                "errors": errors
            },
            "total": len(errors)
        }
        return response, 400
