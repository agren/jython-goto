# Usage example:
#    from jygoto import goto
#    from jygoto import label
#
#    goto .my_label
#    print "Goodbye"
#    label .my_label
#    print "Hello"
#    print "World!"
#

class Dummy(object):
	def __getattr__(self, key):
		return None

goto = Dummy()
label = Dummy()
