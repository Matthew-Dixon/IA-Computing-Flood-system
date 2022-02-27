from floodsystem.analysis import polyfit
import numpy

def test_polyfit():
    x=polyfit([0.0,1.0,2.0,3.0],[0.0,1.0,2.0,3.0],2)
    assert x[1] ==0.0
