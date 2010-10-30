from bda.bfg.app.model import (
    BaseNode,
    Properties,
    BaseMetadata,
)

class Users(BaseNode):
    """Users Node.
    """
    
    @property
    def metadata(self):
        metadata = BaseMetadata()
        metadata.title = "Users"
        metadata.description = "Container for Users"
        return metadata