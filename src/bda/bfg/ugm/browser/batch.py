from bda.bfg.tile import tile
from bda.bfg.app.browser.batch import Batch
from bda.bfg.ugm.model.users import Users
from bda.bfg.ugm.model.groups import Groups

class ColumnBatch(Batch):
    
    @property
    def display(self):
        return True
    
    @property
    def vocab(self):
        ret = list()
        for char in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                     'Y', 'X', 'Y', 'Z']:
            ret.append({
                'page': char,
                'current': False,
                'visible': True,
                'url': '',
            })
        return ret

@tile('columnbatch', interface=Users, permission='login')
class UsersColumnBatch(ColumnBatch): pass

@tile('columnbatch', interface=Groups, permission='login')
class GroupsColumnBatch(ColumnBatch): pass