from common.library import ChoiceAdapter


class StatusTypes(ChoiceAdapter):
    """ class to to status of orders"""
    
    Pending = 101
    Completed = 102
    Cancelled = 103