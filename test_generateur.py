#! /usr/bin/env python3
# coding: utf-8

import generateur
import os
import sys

def test_class_generateur():
    mon_generateur = generateur.Mon_generateur('nom_A', 'chemin_A')
    
def test_creation_dossier():
    mon_generateur = generateur.Mon_generateur('nom_A', sys.path[0])
    #nom = f'{sys.path[0]}/nom_A'
    mon_generateur.creerdossier('nom_A', sys.path[0])
    assert os.path.exists(f'{sys.path[0]}/nom_A') == True