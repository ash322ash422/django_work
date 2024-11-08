MY_DEBUG = True

def dbg(*s, endline = '\n'):
   if MY_DEBUG:
      if isinstance(s, tuple):
         print( 'dbg:' + ''.join(map(str,s)) , end=endline)
#end def

