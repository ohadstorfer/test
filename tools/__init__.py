# initiitit


from .numbers.simp import *
from .numbers.comp import *




simp_called = False



def check_simp_called():
    if not simp_called:
        raise Exception("Cannot call functions in comp module before calling at least one function in simp module")
