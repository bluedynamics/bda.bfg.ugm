from bda.bfg.tile import tile
from bda.bfg.ugm.model.ugm import Ugm
from.bda.bfg.ugm.browser.columns import Column

@tile('leftcolumn', interface=Ugm, permission='view')
class RootLeftColumn(Column):
    
    def render(self):
        return self._render(self.model['users'], 'leftcolumn')

@tile('rightcolumn', interface=Ugm, permission='view')
class RootRightColumn(Column):
    
    def render(self):
        return self._render(self.model['users'], 'rightcolumn')