from bda.bfg.app.model import (
    AdapterNode,
    Properties,
    BaseMetadata,
)

class User(AdapterNode):
    
    @property
    def properties(self):
        props = Properties()
        props.editable = True
        return props
    
    @property
    def metadata(self):
        metadata = BaseMetadata()
        metadata.title = "User"
        metadata.description = "User"
        return metadata
    
    def __call__(self):
        self.model()