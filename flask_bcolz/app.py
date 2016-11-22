# standard library imports
from pathlib import Path

# related third party imports
import bcolz
import six
from flask import Flask, jsonify
from flask.views import MethodView, MethodViewType
from flask_apispec import FlaskApiSpec, ResourceMeta

# local application/library specific imports

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
docs = FlaskApiSpec(app)


class MethodResourceMeta(ResourceMeta, MethodViewType):
    pass


class MethodResource(six.with_metaclass(MethodResourceMeta, MethodView)):
    methods = None


class DataResource(MethodResource):
    def get_valid_folders(self, data_path):
        def filter_folders(path):
            folder_ends_with = ['data', 'meta']
            return path.parts[-1] not in folder_ends_with

        valid_folders = filter(filter_folders, data_path.glob('**'))
        return set(valid_folders)

    def get(self, folder):
        data_path = Path('data')
        valid_folders = self.get_valid_folders(data_path)
        if data_path / folder not in valid_folders:
            return 'Invalid folder name', 422
        data = bcolz.open('data/{}'.format(folder))
        return jsonify(list(data))


app.add_url_rule('/data/<path:folder>/chunks', view_func=DataResource.as_view('DataResource'))
docs.register(DataResource, endpoint='DataResource')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
