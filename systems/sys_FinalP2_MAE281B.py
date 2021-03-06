import numpy as np

from typing import Tuple,Union,Optional
from numpy import ndarray

from .sys_Parents import ControlAffineSys

class Sys_FinalP2_MAE281B(ControlAffineSys):
    def __init__(self) -> None:
        xDims = 2
        xBounds = np.array([[-3,3],[-3,3]])
        uDims = 1
        uBounds = np.array([[-10000,10000]])

        super().__init__(xDims=xDims,xBounds=xBounds,uDims=uDims,uBounds=uBounds)

    def f(self, x:ndarray, t:Optional[float]=None) -> ndarray:
        f = np.array([[-3/2*x[0,0]**2 - 1/2*x[0,0]**3 - x[1,0]],[0]])
        return f

    def g(self, x:ndarray, t:Optional[float]=None) -> ndarray:
        g = np.array([[0],[1]])
        return g

    def w(self, x:ndarray, t:Optional[float]=None) -> ndarray:
        w = np.zeros((self.xDims,1))
        return w

    def xdot(self,x:ndarray,t:Optional[float]=None,u:Optional[ndarray]=None,noise:bool=False) -> ndarray:
        f = self.f(x,t)
        g = self.g(x,t)
        w = self.w(x,t)
        if u == None: u = np.zeros((self.uDims,1))
        if noise == False: w = np.zeros(w.shape)
        return f + g@u + w
