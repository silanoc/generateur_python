#! /usr/bin/env python3
# coding: utf-8

import os

class Mon_generateur():
    def __init__(self, nom, chemin):
        self.nom = nom
        self.chemin = chemin
        
    def creerdossier(self, nom, chemin):
        try:
            os.makedirs(f'{chemin}/{nom}')
        except FileExistsError:
            pass
 