# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:34:28 2018

@author: SpawN
"""

from googletrans import Translator

translator = Translator()

text = unicode("안녕하세요", "utf-8")
translated = translator.translate(text)
print(" Source Language:" + translated.src)