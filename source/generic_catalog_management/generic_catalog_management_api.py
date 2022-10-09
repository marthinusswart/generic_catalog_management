from flask_restful import Api
from generic_catalog_management.api_management import ApiManagement
from generic_catalog_management.catalog_management import CatalogItemCondition, Catalogs, CatalogGenres, CatalogItemAudienceRating
from generic_catalog_management.catalog_management import CatalogItemFormat, CatalogItemRegion, CatalogType


def create_api(app):
    api = Api(app)
    api.add_resource(ApiManagement, '/api/v1')
    api.add_resource(Catalogs, '/api/v1/<tenant_key>/catalogs')
    api.add_resource(CatalogGenres, '/api/v1/<tenant_key>/cataloggenres')
    api.add_resource(CatalogItemAudienceRating,
                     '/api/v1/<tenant_key>/catalogitemaudienceratings')
    api.add_resource(CatalogItemCondition,
                     '/api/v1/<tenant_key>/catalogitemconditions')
    api.add_resource(CatalogItemFormat,
                     '/api/v1/<tenant_key>/catalogitemformats')
    api.add_resource(CatalogItemRegion,
                     '/api/v1/<tenant_key>/catalogitemregions')
    api.add_resource(CatalogType,
                     '/api/v1/<tenant_key>/catalogtypes')
    return api
