from flask import request
from flask_restx import Resource, Namespace, fields

from main.repositories.user import SqlUserRepository
from main.services.user import UserService

api = Namespace('user', description='user related operations')

user_model = api.model('user_model', {
    'username': fields.String(required=True, description='user username'),
    'password': fields.String(required=True, description='user password'),
})


@api.route('/')
@api.response(404, 'User not found.')
class User(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = UserService(SqlUserRepository())

    @api.doc('get a user by username')
    @api.marshal_with(user_model)
    def get(self, username: str):
        """get a user given its identifier"""
        user = self.user_service.get_by_username(username)
        if not user:
            api.abort(404)
        else:
            return user, 200

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(user_model, validate=True)
    def post(self):
        """Creates a new User """
        user = request.json
        if self.user_service.get_by_username(user["username"]):
            api.abort(400, 'User already existed')

        result = self.user_service.create_user(user["username"], user["password"])
        if result.inserted > 0:
            return None, 201
        return None, 500
