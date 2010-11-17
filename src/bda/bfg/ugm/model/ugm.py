from odict import odict
from zope.interface import implements
from bda.bfg.app.model import (
    FactoryNode,
    Properties,
    BaseMetadata,
)
from bda.bfg.ugm.model.interfaces import IUgm
from bda.bfg.ugm.model.users import Users
from bda.bfg.ugm.model.groups import Groups
from bda.bfg.ugm.model.settings import Settings

class Ugm(FactoryNode):
    
    implements(IUgm)
    
    factories = odict((
        ('users', Users),
        #('groups', Groups), #XXX: later
        ('settings', Settings),
    ))
    
    @property
    def properties(self):
        props = Properties()
        props.in_navtree = False
        props.editable = False
        props.mainmenu_empty_title = True
        props.default_child = 'users'
        return props
    
    @property
    def metadata(self):
        metadata = BaseMetadata()
        metadata.title = "ugm"
        return metadata