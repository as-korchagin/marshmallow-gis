from marshmallow import schema, post_dump, pre_load
from .geo_field import GeoField


class GeoFeatureModelSerializer(schema.Schema):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._geo_field = None

    @property
    def geo_field(self):
        if not self._geo_field:
            for field_name, field_type in self.fields.items():
                if isinstance(field_type, GeoField):
                    self._geo_field = field_name
                    break
        return self._geo_field

    @pre_load(pass_many=True)
    def _convert(self, data, many):
        if many:
            obj = [{**feature['properties'], self.geo_field: feature['geometry']} for feature in data['features']]
        else:
            obj = {**data['properties'], self.geo_field: data['geometry']}
        return obj

    @post_dump(pass_many=True)
    def _serialize(self, data, many):
        return self.__to_collection(data) if many else self.__to_one(data)

    def __to_one(self, data):
        geo_field = data.pop(self.geo_field)
        return {
            'type': 'Feature',
            'geometry': geo_field,
            'properties': data,
        }

    def __to_collection(self, data):
        return {
            'type': "FeatureCollection",
            'features': [self.__to_one(elem) for elem in data]
        }
