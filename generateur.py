#! /usr/bin/env python3
# coding: utf-8

import os

class Mon_generateur():
    def __init__(self, nom, chemin = '/home/gabriel-le/Dropbox/mes_depots_git'):
        self.nom = nom
        self.chemin = chemin
        
    def creerdossier(self, nom, chemin = '/home/gabriel-le/Dropbox/mes_depots_git'):
        try:
            os.makedirs(f'{chemin}/{nom}')
        except FileExistsError:
            pass
 