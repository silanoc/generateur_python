#! /usr/bin/env python3
# coding: utf-8

import os

class Mon_generateur():
    def __init__(self, nom, chemin = '/home/gabriel-le/Dropbox/mes_depots_git'):
        self.nom = nom
        self.chemin = chemin
        
        self.entete = '''#! /usr/bin/env python3
# coding: utf-8

# autair : Silanoc
# date : 

    """_summary_
    """'''
        
    def creerdossier(self, nom, chemin = '/home/gabriel-le/Dropbox/mes_depots_git'):
        try:
            os.makedirs(f'{chemin}/{nom}')
        except FileExistsError:
            pass
        
    def creation_fichier_code(self, nom, chemin = '/home/gabriel-le/Dropbox/mes_depots_git'):
        fichier = open(f'{chemin}/{nom}/{nom}.py', 'w', encoding="utf8")
        message = f'''{self.entete}

if __name__ == __main__:
    pass
'''
        fichier.write(message)
        
    def creation_fichier_test(self, nom, chemin = '/home/gabriel-le/Dropbox/mes_depots_git'):
        fichier = open(f'{chemin}/{nom}/test_{nom}.py', 'w', encoding="utf8")
        message = f'''{self.entete}

import pytest
import {nom}
'''
        fichier.write(message)
        
    
        
 