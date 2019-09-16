from shapely.geometry import shape
from shapely.errors import WKTReadingError
from shapely.geometry import mapping
from marshmallow import fields


class GeoField(fields.Field):
    default_error_messages = {
        'invalid': 'Not a valid geometry.',
        'bad_wkt': "Invalid WKT data"
    }

    def _serialize(self, value, attr, obj, **kwargs):
        serialized = mapping(obj[attr])
        return serialized

    def _deserialize(self, value, attr, data, **kwargs):
        geom = self._validated(data[attr])
        return geom

    def _to_string(self, value):
        return str(value)

    def _validated(self, value):
        """Format the value or raise a :exc:`ValidationError` if an error occurs."""
        try:
            return shape(value)
        except (TypeError, ValueError, AttributeError):
            self.fail('invalid')
        except WKTReadingError:
            self.fail('bad_wkt')
