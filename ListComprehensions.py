print [x*x for x in range(1,11) if x%2==0]
print [m+n for m in 'ABC' for n in 'XYZ']

import os
print [d for d in os.listdir('.')]
L=["Hello", "World", 20,'IBM', 'Apple']
#print [s.lower() for s in L if isinstance(s, str)]
print [s.upper() if isinstance(s, str) else s for s in L]


