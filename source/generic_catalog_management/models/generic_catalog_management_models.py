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
