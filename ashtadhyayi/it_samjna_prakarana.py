#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum
import re
from ashtadhyayi.pratyahara import वर्णाः
from ashtadhyayi.utils import स्वरात्_मात्रा

उपदेशसंज्ञकः = Enum('उपदेशसंज्ञकः', 'प्रत्याहारः प्रत्ययः आदेशः आगमः धातुः')

def उपदेशेऽजनुनासिक_इत्_१_३_२():
    अच् = वर्णाः('अच्')
    अजनुनासिक = '[{अच्}]ँ'.format(अच्= अच् + स्वरात्_मात्रा(वर्णाः('अच्')))
    return अजनुनासिक

def हलन्त्यम्_१_३_३():
    return हलन्त्यम्()

def हलन्त्यम्(विभक्तौ=''):
    हल् = वर्णाः('हल्')
    हल् = "".join([वर्णः for वर्णः in हल् if वर्णः not in विभक्तौ])
    return '[{हल्}]्$'.format(हल्=हल्)

def न_विभक्तौ_तुस्माः_१_३_४():
    return हलन्त्यम्('तथदधनसम')

def आदिर्ञिटुडवः_१_३_५():
    आदिर्ञिटुडवः = '^ञि|टु|डु'
    return आदिर्ञिटुडवः

def षः_प्रत्ययस्य_१_३_६():
    षः = '^ष्'
    return षः

def चुटू_१_३_७():
    चुटू = '^[चछजझ्ञटठडढण]्?'
    return चुटू

def लशक्वतद्धिते_१_३_८():
    लशकु = '^[लशकखगघङ]्?'
    return लशकु

def तस्य_लोपः_१_३_९(pattern, उपदेशः):
    # '' = लोपः
    return re.sub(pattern, '', उपदेशः)

def इत्संज्ञाप्रकरणम्(उपदेशः, उपदेशसंज्ञकः=उपदेशसंज्ञकः.प्रत्ययः, विभक्तिः=False):
    # अजनुनासिक
    उपदेशः = तस्य_लोपः_१_३_९(उपदेशेऽजनुनासिक_इत्_१_३_२(), उपदेशः)
    
    # हलन्त्यम्
    if not विभक्तिः :
        उपदेशः = तस्य_लोपः_१_३_९(हलन्त्यम्_१_३_३(), उपदेशः)
    else :
        उपदेशः = तस्य_लोपः_१_३_९(न_विभक्तौ_तुस्माः_१_३_४(), उपदेशः)

    #आदिर्ञिटुडवः
    उपदेशः = तस्य_लोपः_१_३_९(आदिर्ञिटुडवः_१_३_५(), उपदेशः)

    if उपदेशसंज्ञकः == उपदेशसंज्ञकः.प्रत्ययः :
        #षः_प्रत्ययस्य_१_३_६
        उपदेशः = तस्य_लोपः_१_३_९(षः_प्रत्ययस्य_१_३_६(), उपदेशः)

        #चुटू
        उपदेशः = तस्य_लोपः_१_३_९(चुटू_१_३_७(), उपदेशः)

        #लशक्वतद्धिते    
        उपदेशः = तस्य_लोपः_१_३_९(लशक्वतद्धिते_१_३_८(), उपदेशः)

    return उपदेशः
