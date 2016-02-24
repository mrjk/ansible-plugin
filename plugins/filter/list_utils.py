# From: https://github.com/timraasveld/ansible-string-split-filter

from ansible import errors
import re


def list_reverse(value):
    try:
		return value[::-1]
    except Exception, e:
        raise errors.AnsibleFilterError('list_reverse plugin error: %s, list=%s' % str(e),str(value) )

def list_index_of(value, item=''):
    try:
		return value.index(item)
    except Exception, e:
		return -1
        #raise errors.AnsibleFilterError('list_index_of plugin error: %s, list=%s' % str(e),str(value) )


class FilterModule(object):
    ''' A filter to play with lists. '''
    def filters(self):
        return {
            'list_reverse' : list_reverse,
            'list_index_of' : list_index_of,
        }
