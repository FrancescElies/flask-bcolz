# standard library imports
import six

# related third party imports
from flask import Flask, jsonify
from flask_apispec import FlaskApiSpec, ResourceMeta
from flask.views import MethodView, MethodViewType
import bcolz

# local application/library specific imports


app = Flask(__name__)
docs = FlaskApiSpec(app)


class MethodResourceMeta(ResourceMeta, MethodViewType):
    pass


class MethodResource(six.with_metaclass(MethodResourceMeta, MethodView)):
    methods = None


class DataResource(MethodResource):
    @doc(params={'folder': {'description': "subfolder's name inside data folder"}})
    def get(self, folder):
        data = bcolz.open('data/{}'.format(folder))
        return jsonify(list(data))


app.add_url_rule('/data/<folder>', view_func=DataResource.as_view('DataResource'))
docs.register(DataResource, endpoint='DataResource')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
