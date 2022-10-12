from generic_catalog_management import db


class Catalog(db.Model):
    __tablename__ = 'generic_catalog'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    catalog_type_id = db.Column(db.Integer)
    tenant_key = db.Column(db.String(100))

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'catalog_type_id': self.catalog_type_id,
            'tenant_key': self.tenant_key
        }


class CatalogGenre(db.Model):
    __tablename__ = 'generic_catalog_genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    tenant_key = db.Column(db.String(100))

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'tenant_key': self.tenant_key
        }


class CatalogItemAudienceRating(db.Model):
    __tablename__ = 'generic_catalog_item_audience_rating'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    tenant_key = db.Column(db.String(100))

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'tenant_key': self.tenant_key
        }


class CatalogItemCondition(db.Model):
    __tablename__ = 'generic_catalog_item_condition'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    tenant_key = db.Column(db.String(100))

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'tenant_key': self.tenant_key
        }


class CatalogItemFormat(db.Model):
    __tablename__ = 'generic_catalog_item_format'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    tenant_key = db.Column(db.String(100))

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'tenant_key': self.tenant_key
        }


class CatalogItemRegion(db.Model):
    __tablename__ = 'generic_catalog_item_region'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    tenant_key = db.Column(db.String(100))

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'tenant_key': self.tenant_key
        }


class CatalogType(db.Model):
    __tablename__ = 'generic_catalog_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    tenant_key = db.Column(db.String(100))

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'tenant_key': self.tenant_key
        }


class Developer(db.Model):
    __tablename__ = 'generic_developer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    tenant_key = db.Column(db.String(100))

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'tenant_key': self.tenant_key
        }


class GamePlatform(db.Model):
    __tablename__ = 'generic_game_platform'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    tenant_key = db.Column(db.String(100))
    catalog_id = db.Column(db.Integer)

    def as_json(self):
        return {
            'id': self.id,
            'catalog_id': self.catalog_id,
            'name': self.name,
            'description': self.description,
            'tenant_key': self.tenant_key
        }


class Publisher(db.Model):
    __tablename__ = 'generic_publisher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    tenant_key = db.Column(db.String(100))

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'tenant_key': self.tenant_key
        }


class CatalogItem(db.Model):
    __tablename__ = 'generic_catalog_item'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(150))
    tenant_key = db.Column(db.String(100))
    catalog_id = db.Column(db.Integer)
    purchase_price = db.Column(db.Float)
    image_file_id = db.Column(db.Integer)
    sort_title = db.Column(db.String(150))
    condition_id = db.Column(db.Integer)
    vendor_id = db.Column(db.Integer)

    def as_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'catalog_id': self.catalog_id,
            'purchase_price': self.purchase_price,
            'image_file_id': self.image_file_id,
            'sort_title': self.sort_title,
            'condition_id': self.condition_id,
            'vendor_id': self.vendor_id,
            'tenant_key': self.tenant_key
        }


class GameCatalogItem(db.Model):
    __tablename__ = 'generic_game_catalog_item'
    id = db.Column(db.Integer, primary_key=True)
    catalog_item_id = db.Column(db.Integer)
    tenant_key = db.Column(db.String(100))
    series = db.Column(db.String(150))
    developer_id = db.Column(db.Integer)
    publisher_id = db.Column(db.Integer)
    audience_rating_id = db.Column(db.Integer)
    region_id = db.Column(db.Integer)
    format_type_id = db.Column(db.Integer)
    game_platform_id = db.Column(db.Integer)
    release_date = db.Column(db.DateTime)
    igdb_id = db.Column(db.Integer)

    def as_json(self):
        return {
            'id': self.id,
            'catalog_item_id': self.catalog_item_id,
            'series': self.series,
            'developer_id': self.developer_id,
            'publisher_id': self.publisher_id,
            'audience_rating_id': self.audience_rating_id,
            'region_id': self.region_id,
            'format_type_id': self.format_type_id,
            'game_platform_id': self.game_platform_id,
            'release_date': self.release_date,
            'igdb_id': self.igdb_id,
            'tenant_key': self.tenant_key
        }
