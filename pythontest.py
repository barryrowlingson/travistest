
print "This must be python 2"
from inform import display, warn, error
display(
    'Display is like print'
    'except that it supports logging and can be disabled.'
    ,sep=', ')

# Display is like print, except that it supports logging and can be disabled.

warn('warnings get a header that is printed in yellow.')
# warning: warnings get a header that is printed in yellow.

error('errors get a header that is printed in red.')
# error: errors get a header that is printed in red.
