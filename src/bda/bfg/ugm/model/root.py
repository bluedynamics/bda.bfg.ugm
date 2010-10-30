from odict import odict
from bda.bfg.app.model import (
    FactoryNode,
    Properties,
    BaseMetadata,
)
from bda.bfg.ugm.model.users import Users
from bda.bfg.ugm.model.groups import Groups

class Root(FactoryNode):
    """Root Node.
    """
    
    factories = odict((
        ('users', Users),
        ('groups', Groups),
    ))
    
    @property
    def properties(self):
        props = Properties()
        props.mainmenu_empty_title = True
        return props
    
    @property
    def metadata(self):
        metadata = BaseMetadata()
        metadata.title = "ugm"
        return metadata