#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
    return lenght % 2 ==0


def get_num_char(string, char):
	for c in string:
        if c == char:
            num char+=1
    


def get_first_part_of_name(name):
	nom=list
    return "Bonjour",name,"!"


def get_random_sentence(animals, adjectives, fruits):
	return ""


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
