from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.app.browser.utils import make_url
from bda.bfg.ugm.model.groups import Groups
from bda.bfg.ugm.browser.batch import ColumnBatch
from bda.bfg.ugm.browser.listing import ColumnListing

@tile('leftcolumn', 'templates/left_column.pt',
      interface=Groups, permission='view')
class GroupsLeftColumn(Tile):
    
    add_label = u"Add Group"

@tile('rightcolumn', interface=Groups, permission='view')
class GroupsRightColumn(Tile):
    
    def render(self):
        return u'<div class="right_column">&nbsp;</div>'

@tile('columnbatch', interface=Groups, permission='view')
class GroupsColumnBatch(ColumnBatch):
    pass

@tile('columnlisting', 'templates/column_listing.pt',
      interface=Groups, permission='view')
class GroupsColumnListing(ColumnListing):
    
    @property
    def items(self):
        ret = list()
        for i in range(10):
            ret.append({
                'target': make_url(self.request,
                                   node=self.model,
                                   resource=u'group%i' % i),
                'left': 'Group',
                'right': '%i' % i,
            })
        return ret