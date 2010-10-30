from bda.bfg.app.model import (
    FactoryNode,
    Properties,
    BaseMetadata,
)

class Root(FactoryNode):
    """Root Node.
    """
    
    factories = {
    }
    
    @property
    def properties(self):
        props = Properties()
        props.in_navtree = True
        return props
    
    @property
    def metadata(self):
        metadata = BaseMetadata()
        metadata.title = "UGM"
        return metadata