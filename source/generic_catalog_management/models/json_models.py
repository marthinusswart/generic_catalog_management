from datetime import datetime

class GameItem():
    def as_json(self, view_row):
        return {
            'id': view_row.id,            
            'series': view_row.series,
            'developer': view_row.developer,
            'publisher': view_row.publisher,
            'audience_rating': view_row.rating,
            'region': view_row.region,
            'format': view_row.format,
            'platform': view_row.platform,
            'release_date': datetime.strptime(view_row.release_date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'),
            'igdb_id': view_row.igdb_id,
            'tenant_key': view_row.tenant_key,            
            'title': view_row.title,
            'description': view_row.description,            
            'purchase_price': view_row.purchase_price,            
            'sort_title': view_row.sort_title,
            'condition': view_row.condition            
        }