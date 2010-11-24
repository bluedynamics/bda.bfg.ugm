from bda.bfg.ugm.model.ugm import Ugm
from bda.bfg.ugm.model.users import Users
from bda.bfg.ugm.model.user import User

root = Ugm()

def get_root(environ):
    return root