# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_container.ipynb.

# %% auto 0
__all__ = ['Container']

# %% ../00_container.ipynb 3
import pandas as pd
from fastcore.test import *
from fastcore.utils import *

# %% ../00_container.ipynb 8
class Container():
    """Un container de dataset qui s'initialise en passant une `clé` et un `dataset`
    """
    def __init__(self, 
                 cle : str, # la clé du container
                 dataset : pd.DataFrame = None, # le dataset
                 colonnes_a_masquer : list = [], # les colonnes à masquer
                 colonnes_a_conserver : list = [] # les colonnes qui ne seront pas transformées
                ):
        self.cle = cle
        self.dataset = dataset
    def __str__(self):
        return f'Container for "{self.cle}" of shape {self.dataset.shape}' 
    __repr__ = __str__

# %% ../00_container.ipynb 13
@patch
def __eq__(self:Container, cont_b:Container): return (self.cle, self.dataset.shape) == (cont_b.cle, cont_b.dataset.shape)

# %% ../00_container.ipynb 19
@patch
def longueur(self:Container):
    '''retourne le nombre de lignes du dataset'''
    return self.dataset.shape[0]
