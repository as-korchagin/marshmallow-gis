# marshmalow_gis

Библиотека для сериализации и десериализации GeoJson

## Установка

`pip install git+git@github.com:as-korchagin/marshmallow-gis.git`

## Использование

1. Создать класс, отнаследованнй от GeoFeatureModelSerializer
2. Определить поля в формате библиотеки marshmallow

## Пример

```python
from marshmallow_gis import GeoFeatureModelSerializer, GeoField
from marshmallow import fields


class LocationSerializer(GeoFeatureModelSerializer):
    address = fields.Str()
    city = fields.Str()
    state = fields.Str()
    point = GeoField()
    id = fields.Int()

ls = LocationSerializer(many=False)
ls.load(obj)
``` 

преобразует GeoJson:

```json
{
  "id": 1,
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [
      -123.0208,
      44.0464
    ]
  },
  "properties": {
    "address": "742 Evergreen Terrace",
    "city": "Springfield",
    "state": "Oregon"
  }
}
``` 
 в модель:
 ```json
{
    "id": 1,
    "address": "742 Evergreen Terrace",
    "city":  "Springfield",
    "state": "Oregon",
    "point": "POINT(-123.0208 44.0464)" // shapely object
}
```
