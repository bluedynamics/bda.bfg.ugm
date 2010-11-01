from bda.bfg.app.model import (
    AdapterNode,
    Properties,
    BaseMetadata,
)

class Group(AdapterNode):
    
    @property
    def properties(self):
        props = Properties()
        props.editable = True
        return props
    
    @property
    def metadata(self):
        metadata = BaseMetadata()
        metadata.title = "Group"
        metadata.description = "Group"
        return metadata
    
    def __call__(self):
        self.model()