from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.app.browser.utils import make_url
from bda.bfg.ugm.model.users import Users
from bda.bfg.ugm.model.groups import Groups

class ColumnListing(Tile):
    
    @property
    def items(self):
        # XXX: nothing senceful yet, dummy code for CSS
        ret = list()
        for i in range(1000):
            ret.append({
                'target': make_url(self.request,
                                   node=self.model,
                                   resource=u'foo'),
                'left': 'item %i' % i,
                'right': 'whatever %i' % i,
            })
        return ret