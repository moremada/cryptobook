from flask_restplus import Namespace, Resource

api = Namespace('users', description='User related operations')


@api.route('/<int:user_id>')
@api.param('user_id', 'The user identifier')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get_user')
    def get(self, user_id):
        return 'get user {}'.format(user_id)
