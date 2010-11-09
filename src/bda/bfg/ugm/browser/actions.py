from repoze.bfg.view import bfg_view
from bda.bfg.ugm.model.interfaces import IUsers
from bda.bfg.ugm.model.interfaces import IUser
from bda.bfg.ugm.model.interfaces import IGroups
from bda.bfg.ugm.model.interfaces import IGroup

class Action(object):
    """Abstract action.
    
    A Subclass must implement ``__call__`` and is supposed to be registetred
    as JSON bfg view, like:
    
    @bfg_view(name='action_id', accept='application/json', renderer='json')
    """
    
    def __call__(self, model, request):
        """Perform this action and return JSON response.
        """
        raise NotImplementedError(u"Abstract action does not implement "
                                  u"``__call__``.")

###############################################################################
# Actions for IUsers application node
###############################################################################

@bfg_view(name='delete_item', accept='application/json',
          renderer='json', context=IUsers, permission="view")
class DeleteUserAction(Action):
    
    def __call__(self, model, request):
        """Delete user from database.
        """
        return {
            'success': True,
            'msg': 'Deleted user from database',
        }

###############################################################################
# Actions for IGroups application node
###############################################################################

@bfg_view(name='delete_item', accept='application/json',
          renderer='json', context=IGroups, permission="view")
class DeleteGroupAction(Action):
    
    def __call__(self, model, request):
        """Delete group from database.
        """
        return {
            'success': True,
            'msg': 'Deleted group from database',
        }

###############################################################################
# Actions for IUser application node
###############################################################################

@bfg_view(name='add_item', accept='application/json',
          renderer='json', context=IUser, permission="view")
class UserAddToGroupAction(Action):
    
    def __call__(self, model, request):
        """Add user to group.
        """
        return {
            'success': True,
            'msg': 'Added user to group',
        }

@bfg_view(name='remove_item', accept='application/json',
          renderer='json', context=IUser, permission="view")
class UserRemoveFromGroupAction(Action):
    
    def __call__(self, model, request):
        """Remove user from group.
        """
        return {
            'success': True,
            'msg': 'Removed User from Group',
        }

###############################################################################
# Actions for IGroup application node
###############################################################################

@bfg_view(name='add_item', accept='application/json',
          renderer='json', context=IGroup, permission="view")
class GroupAddUserAction(Action):
    
    def __call__(self, model, request):
        """Add user to group.
        """
        return {
            'success': True,
            'msg': 'Added user to group',
        }

@bfg_view(name='remove_item', accept='application/json',
          renderer='json', context=IGroup, permission="view")
class GroupRemoveUserAction(Action):
    
    def __call__(self, model, request):
        """Remove user from group.
        """
        return {
            'success': True,
            'msg': 'Removed user from group',
        }