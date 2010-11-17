from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.app.browser.utils import make_url
from bda.bfg.ugm.model.interfaces import IGroups
from.bda.bfg.ugm.browser.columns import Column
from bda.bfg.ugm.browser.batch import ColumnBatch
from bda.bfg.ugm.browser.listing import ColumnListing

@tile('leftcolumn', 'templates/left_column.pt',
      interface=IGroups, permission='view')
class GroupsLeftColumn(Tile):
    
    add_label = u"Add Group"

@tile('rightcolumn', interface=IGroups, permission='view')
class GroupsRightColumn(Column):
    
    @property
    def current_id(self):
        return self.request.params.get('currid')
    
    def render(self):
        currid = self.current_id
        if not currid:
            return u'<div class="right_column">&nbsp;</div>'
        return self._render(self.model[currid], 'rightcolumn')

@tile('columnbatch', interface=IGroups, permission='view')
class GroupsColumnBatch(ColumnBatch):
    pass

@tile('columnlisting', 'templates/column_listing.pt',
      interface=IGroups, permission='view')
class GroupsColumnListing(ColumnListing):
    
    slot = 'leftlisting'
    
    @property
    def current_id(self):
        return self.request.params.get('currid')
    
    @property
    def items(self):
        ret = list()
        for i in range(1000):
            target = make_url(self.request,
                              node=self.model,
                              resource=u'group%i' % i)
            ret.append({
                'target': target,
                'head': 'Group %i' % i,
                'current': self.current_id == u'group%i' % i and True or False,
                'actions': [
                    {
                        'id': 'delete_item',
                        'enabled': True,
                        'title': 'Delete Group',
                        'target': target,
                    }
                ],
            })
        return ret