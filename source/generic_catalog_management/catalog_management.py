from flask_restful import Resource
from flask import jsonify, request


class Catalogs(Resource):
    def get(self, tenant_key):
        from .models.generic_catalog_management_models import Catalog
        catalogs = Catalog.query.filter_by(tenant_key=tenant_key)
        result = [a.as_json() for a in catalogs]
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_catalog_management_models import Catalog

        new_catalog_json = request.get_json()

        new_catalog = Catalog()
        new_catalog.name = new_catalog_json['name']
        new_catalog.description = new_catalog_json['description']
        new_catalog.tenant_key = tenant_key
        new_catalog.catalog_type_id = new_catalog_json['catalog_type_id']
        db.session.add(new_catalog)
        db.session.commit()
        return {'result': 'Catalog created', 'JSON received': new_catalog_json}


class CatalogGenres(Resource):
    def get(self, tenant_key):
        from .models.generic_catalog_management_models import CatalogGenre
        catalog_genres = CatalogGenre.query.filter_by(tenant_key=tenant_key)
        result = [a.as_json() for a in catalog_genres]
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_catalog_management_models import CatalogGenre

        new_catalog_genre_json = request.get_json()

        new_catalog_genre = CatalogGenre()
        new_catalog_genre.name = new_catalog_genre_json['name']
        new_catalog_genre.description = new_catalog_genre_json['description']
        new_catalog_genre.tenant_key = tenant_key
        db.session.add(new_catalog_genre)
        db.session.commit()
        return {'result': 'Catalog Genre created', 'JSON received': new_catalog_genre_json}


class CatalogItemAudienceRating(Resource):
    def get(self, tenant_key):
        from .models.generic_catalog_management_models import CatalogItemAudienceRating
        catalog_audience_ratings = CatalogItemAudienceRating.query.filter_by(
            tenant_key=tenant_key)
        result = [a.as_json() for a in catalog_audience_ratings]
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_catalog_management_models import CatalogItemAudienceRating

        new_catalog_audience_rating_json = request.get_json()

        new_catalog_genre = CatalogItemAudienceRating()
        new_catalog_genre.name = new_catalog_audience_rating_json['name']
        new_catalog_genre.description = new_catalog_audience_rating_json['description']
        new_catalog_genre.tenant_key = tenant_key
        db.session.add(new_catalog_genre)
        db.session.commit()
        return {'result': 'Catalog Audience Rating created', 'JSON received': new_catalog_audience_rating_json}


class CatalogItemCondition(Resource):
    def get(self, tenant_key):
        from .models.generic_catalog_management_models import CatalogItemCondition
        catalog_item_condition = CatalogItemCondition.query.filter_by(
            tenant_key=tenant_key)
        result = [a.as_json() for a in catalog_item_condition]
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_catalog_management_models import CatalogItemCondition

        new_catalog_item_condition_json = request.get_json()

        new_catalog_genre = CatalogItemCondition()
        new_catalog_genre.name = new_catalog_item_condition_json['name']
        new_catalog_genre.description = new_catalog_item_condition_json['description']
        new_catalog_genre.tenant_key = tenant_key
        db.session.add(new_catalog_genre)
        db.session.commit()
        return {'result': 'Catalog Item Condition created', 'JSON received': new_catalog_item_condition_json}


class CatalogItemFormat(Resource):
    def get(self, tenant_key):
        from .models.generic_catalog_management_models import CatalogItemFormat
        catalog_item_format = CatalogItemFormat.query.filter_by(
            tenant_key=tenant_key)
        result = [a.as_json() for a in catalog_item_format]
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_catalog_management_models import CatalogItemFormat

        new_catalog_item_format_json = request.get_json()

        new_catalog_genre = CatalogItemFormat()
        new_catalog_genre.name = new_catalog_item_format_json['name']
        new_catalog_genre.description = new_catalog_item_format_json['description']
        new_catalog_genre.tenant_key = tenant_key
        db.session.add(new_catalog_genre)
        db.session.commit()
        return {'result': 'Catalog Item Format created', 'JSON received': new_catalog_item_format_json}


class CatalogItemRegion(Resource):
    def get(self, tenant_key):
        from .models.generic_catalog_management_models import CatalogItemRegion
        catalog_item_region = CatalogItemRegion.query.filter_by(
            tenant_key=tenant_key)
        result = [a.as_json() for a in catalog_item_region]
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_catalog_management_models import CatalogItemRegion

        new_catalog_item_region_json = request.get_json()

        new_catalog_genre = CatalogItemRegion()
        new_catalog_genre.name = new_catalog_item_region_json['name']
        new_catalog_genre.description = new_catalog_item_region_json['description']
        new_catalog_genre.tenant_key = tenant_key
        db.session.add(new_catalog_genre)
        db.session.commit()
        return {'result': 'Catalog Item Region created', 'JSON received': new_catalog_item_region_json}


class CatalogType(Resource):
    def get(self, tenant_key):
        from .models.generic_catalog_management_models import CatalogType
        catalog_type = CatalogType.query.filter_by(
            tenant_key=tenant_key)
        result = [a.as_json() for a in catalog_type]
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_catalog_management_models import CatalogType

        new_catalog_type_json = request.get_json()

        new_catalog_genre = CatalogType()
        new_catalog_genre.name = new_catalog_type_json['name']
        new_catalog_genre.description = new_catalog_type_json['description']
        new_catalog_genre.tenant_key = tenant_key
        db.session.add(new_catalog_genre)
        db.session.commit()
        return {'result': 'Catalog Type created', 'JSON received': new_catalog_type_json}
