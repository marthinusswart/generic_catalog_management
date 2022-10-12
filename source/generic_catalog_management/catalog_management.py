from flask_restful import Resource
from flask import jsonify, request
from datetime import datetime


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
        new_catalog_genre.description = new_catalog_audience_rating_json.get(
            'description')
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
        new_catalog_genre.description = new_catalog_item_condition_json.get(
            'description')
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
        new_catalog_genre.description = new_catalog_item_format_json.get(
            'description')
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
        new_catalog_genre.description = new_catalog_item_region_json.get(
            'description')
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


class Developer(Resource):
    def get(self, tenant_key):
        from .models.generic_catalog_management_models import Developer
        developer = Developer.query.filter_by(
            tenant_key=tenant_key)
        result = [a.as_json() for a in developer]
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_catalog_management_models import Developer

        new_developer_json = request.get_json()

        new_developer = Developer()
        new_developer.name = new_developer_json['name']
        new_developer.description = new_developer_json.get('description')
        new_developer.tenant_key = tenant_key
        db.session.add(new_developer)
        db.session.commit()
        return {'result': 'Developer created', 'JSON received': new_developer_json}


class GamePlatform(Resource):
    def get(self, tenant_key):
        from .models.generic_catalog_management_models import GamePlatform
        game_platform = GamePlatform.query.filter_by(
            tenant_key=tenant_key)
        result = [a.as_json() for a in game_platform]
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_catalog_management_models import GamePlatform

        new_game_platform_json = request.get_json()

        new_game_platform = GamePlatform()
        new_game_platform.name = new_game_platform_json['name']
        new_game_platform.description = new_game_platform_json.get(
            'description')
        new_game_platform.tenant_key = tenant_key
        new_game_platform.catalog_id = new_game_platform_json.get('catalog_id')
        db.session.add(new_game_platform)
        db.session.commit()
        return {'result': 'Game Platform created', 'JSON received': new_game_platform_json}


class Publisher(Resource):
    def get(self, tenant_key):
        from .models.generic_catalog_management_models import Publisher
        publisher = Publisher.query.filter_by(
            tenant_key=tenant_key)
        result = [a.as_json() for a in publisher]
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_catalog_management_models import Publisher

        new_publisher_json = request.get_json()

        new_game_platform = Publisher()
        new_game_platform.name = new_publisher_json['name']
        new_game_platform.description = new_publisher_json.get('description')
        new_game_platform.tenant_key = tenant_key
        db.session.add(new_game_platform)
        db.session.commit()
        return {'result': 'Publisher created', 'JSON received': new_publisher_json}


class CatalogItem(Resource):
    def get(self, tenant_key):
        from .models.generic_catalog_management_models import CatalogItem
        catalog_item = CatalogItem.query.filter_by(
            tenant_key=tenant_key)
        result = [a.as_json() for a in catalog_item]
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_catalog_management_models import CatalogItem

        new_catalog_item_json = request.get_json()

        new_catalog_item = CatalogItem()
        new_catalog_item.title = new_catalog_item_json['title']
        new_catalog_item.description = new_catalog_item_json['description']
        new_catalog_item.catalog_id = new_catalog_item_json['catalog_id']
        new_catalog_item.image_file_id = new_catalog_item_json['image_file_id']
        new_catalog_item.purchase_price = new_catalog_item_json['purchase_price']
        new_catalog_item.sort_title = new_catalog_item_json['sort_title']
        new_catalog_item.condition_id = new_catalog_item_json['condition_id']
        new_catalog_item.vendor_id = new_catalog_item_json['vendor_id']
        new_catalog_item.tenant_key = tenant_key
        db.session.add(new_catalog_item)
        db.session.commit()
        return {'result': 'Catalog Item created', 'JSON received': new_catalog_item_json}


class GameCatalogItem(Resource):
    def get(self, tenant_key):
        from .models.generic_catalog_management_models import GameCatalogItem
        game_catalog_item = GameCatalogItem.query.filter_by(
            tenant_key=tenant_key)
        result = [a.as_json() for a in game_catalog_item]
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_catalog_management_models import GameCatalogItem

        new_game_catalog_item_json = request.get_json()

        cdate = datetime.strptime(
            new_game_catalog_item_json['release_date'], '%Y-%m-%d %H:%M:%S')

        new_game_catalog_item = GameCatalogItem()
        new_game_catalog_item.catalog_item_id = new_game_catalog_item_json.get(
            'catalog_item_id')
        new_game_catalog_item.game_platform_id = new_game_catalog_item_json.get(
            'game_platform_id')
        new_game_catalog_item.release_date = cdate
        new_game_catalog_item.format_type_id = new_game_catalog_item_json.get(
            'format_type_id')
        new_game_catalog_item.region_id = new_game_catalog_item_json.get(
            'region_id')
        new_game_catalog_item.series = new_game_catalog_item_json.get('series')
        new_game_catalog_item.audience_rating_id = new_game_catalog_item_json.get(
            'audience_rating_id')
        new_game_catalog_item.publisher_id = new_game_catalog_item_json.get(
            'publisher_id')
        new_game_catalog_item.developer_id = new_game_catalog_item_json.get(
            'developer_id')
        new_game_catalog_item.igdb_id = new_game_catalog_item_json.get(
            'igdb_id')
        new_game_catalog_item.tenant_key = tenant_key
        db.session.add(new_game_catalog_item)
        db.session.commit()
        return {'result': 'Game Catalog Item created', 'JSON received': new_game_catalog_item_json}
