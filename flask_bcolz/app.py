# standard library imports
import six
from pathlib import Path

# related third party imports
from flask import Flask, jsonify
from flask_apispec import FlaskApiSpec, ResourceMeta
from flask.views import MethodView, MethodViewType
import bcolz

# local application/library specific imports

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
docs = FlaskApiSpec(app)


class MethodResourceMeta(ResourceMeta, MethodViewType):
    pass


class MethodResource(six.with_metaclass(MethodResourceMeta, MethodView)):
    methods = None


class DataResource(MethodResource):
    def get(self, folder):
        data_path = Path('data')
        valid_folders = set(data_path.glob('*'))
        if data_path / folder not in valid_folders:
            return 'Invalid folder name', 422
        data = bcolz.open('data/{}'.format(folder))
        return jsonify(list(data))


app.add_url_rule('/data/<folder>', view_func=DataResource.as_view('DataResource'))
docs.register(DataResource, endpoint='DataResource')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
