from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.app.browser.utils import make_url
from bda.bfg.ugm.model.users import Users
from bda.bfg.ugm.browser.batch import ColumnBatch
from bda.bfg.ugm.browser.listing import ColumnListing

@tile('leftcolumn', 'templates/left_column.pt',
      interface=Users, permission='view')
class UsersLeftColumn(Tile):
    
    add_label = u"Add User"

@tile('rightcolumn', interface=Users, permission='view')
class UsersRightColumn(Tile):
    
    def render(self):
        return u'<div class="right_column">&nbsp;</div>'

@tile('columnbatch', interface=Users, permission='view')
class UsersColumnBatch(ColumnBatch):
    pass

@tile('columnlisting', 'templates/column_listing.pt',
      interface=Users, permission='view')
class UsersColumnListing(ColumnListing):
    
    @property
    def items(self):
        ret = list()
        for i in range(10):
            ret.append({
                'target': make_url(self.request,
                                   node=self.model,
                                   resource=u'user%i' % i),
                'left': 'User',
                'right': '%i' % i,
            })
        return ret