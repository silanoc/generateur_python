#! /usr/bin/env python3
# coding: utf-8

"""
autair : Silanoc
date création : 27 juillet 2022
date mise à jour : 27 juillet 2022
version : 0.1.0
"""

import os

class Mon_generateur():
    def __init__(self, nom, chemin = '/home/gabriel-le/Dropbox/mes_depots_git'):
        self.nom = nom
        self.chemin = chemin
        
        self.entete = '''#! /usr/bin/env python3
# coding: utf-8

"""
autair : Silanoc
date création : 
date mise à jour : 
version : 0.0.1
"""'''
        
    def creerdossier(self, nom, chemin = '/home/gabriel-le/Dropbox/mes_depots_git'):
        try:
            os.makedirs(f'{chemin}/{nom}')
        except FileExistsError:
            pass
        
    def creation_fichier_code(self, nom, chemin = '/home/gabriel-le/Dropbox/mes_depots_git'):
        fichier = open(f'{chemin}/{nom}/{nom}.py', 'w', encoding="utf8")
        message = f'''{self.entete}

if __name__ == '__main__':
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
    
    def enchaine_dossier_code_test(self):
        self.creerdossier(self.nom, self.chemin)
        self.creation_fichier_code(self.nom, self.chemin)
        self.creation_fichier_test(self.nom, self.chemin)
        
def demande_valeurs_depart():
    nom = input('nom dossier')
    chemin = input('chemin du dossier')
    return nom, chemin

if __name__ == '__main__':
        
    nom, chemin = demande_valeurs_depart()
    projet = Mon_generateur(nom, chemin)
    projet.enchaine_dossier_code_test()        
 