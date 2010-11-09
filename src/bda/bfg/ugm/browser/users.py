from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.app.browser.utils import make_url
from bda.bfg.ugm.model.interfaces import IUsers
from bda.bfg.ugm.browser.batch import ColumnBatch
from bda.bfg.ugm.browser.listing import ColumnListing

@tile('leftcolumn', 'templates/left_column.pt',
      interface=IUsers, permission='view')
class UsersLeftColumn(Tile):
    
    add_label = u"Add User"

@tile('rightcolumn', interface=IUsers, permission='view')
class UsersRightColumn(Tile):
    
    def render(self):
        return u'<div class="right_column">&nbsp;</div>'

@tile('columnbatch', interface=IUsers, permission='view')
class UsersColumnBatch(ColumnBatch):
    pass

@tile('columnlisting', 'templates/column_listing.pt',
      interface=IUsers, permission='view')
class UsersColumnListing(ColumnListing):
    
    @property
    def current_id(self):
        return self.request.get('_listing_current_id')
    
    @property
    def items(self):
        ret = list()
        for i in range(1000):
            target = make_url(self.request,
                              node=self.model,
                              resource=u'user%i' % i)
            ret.append({
                'target': target,
                'head': 'User - %i' % i,
                'current': self.current_id == u'user%i' % i and True or False,
                'actions': [
                    {
                        'id': 'delete_item',
                        'enabled': True,
                        'title': 'Delete User',
                        'target': target,
                    }
                ],
            })
        return ret