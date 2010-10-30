from bda.bfg.app.model import (
    BaseNode,
    Properties,
    BaseMetadata,
)

class Groups(BaseNode):
    """Groups Node.
    """
    
    @property
    def metadata(self):
        metadata = BaseMetadata()
        metadata.title = "Groups"
        metadata.description = "Container for Groups"
        return metadata