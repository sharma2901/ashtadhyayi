#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
from ashtadhyayi.pratyahara import वर्णाः
from ashtadhyayi.it_samjna_prakarana import इत्, उपदेशसंज्ञकः, इत्संज्ञाप्रकरणम्
from ashtadhyayi.utils import स्वरात्_मात्रा, स्वरमात्राः, मात्रायाः_स्वरः
from enum import Enum


लकारः = Enum('लकारः', 'लट् लिट् लुट् लृट् लेट् लोट् लङ् लिङ् लुङ् लृङ्')


def लः_परस्मैपदम्_१_४_९९():
    return तिप्तस्झिसिप्थस्थमिब्वस्मस्_तातांझथासाथांध्वमिड्वहिमहिङ्_३_४_७८()[:9]


def तङानावात्मनेपदम्_१_४_१००():
    return तिप्तस्झिसिप्थस्थमिब्वस्मस्_तातांझथासाथांध्वमिड्वहिमहिङ्_३_४_७८()[9:]


def तिप्तस्झिसिप्थस्थमिब्वस्मस्_तातांझथासाथांध्वमिड्वहिमहिङ्_३_४_७८():
    return ['तिप्', 'तस्', 'झि', 'सिप्', 'थस्', 'थ', 'मिप्', 'वस्', 'मस्',
            'त', 'आताम्', 'झ', 'थास्', 'आथाम्', 'ध्वम्', 'इड्', 'वहि', 'महिङ्']


def तिङस्त्रीणि_त्रीणि_प्रथममध्यमोत्तमाः_१_४_१०१(प्रत्ययाः, पुरुषः):
    return प्रत्ययाः[3 * पुरुषः: 3 * (पुरुषः + 1)]


def तान्येकवचनद्विवचनबहुवचनान्येकशः_१_४_१०२(प्रत्ययाः, वचनम्):
    return प्रत्ययाः[वचनम्]


# TODO move this to an appropriate place
def टित्_वा(लकारः):
    return इत्(लकारः, उपदेशसंज्ञकः.आदेशः)[0] == 'ट्'


# TODO move this to an appropriate place
def ङित्_वा(लकारः):
    return इत्(लकारः, उपदेशसंज्ञकः.आदेशः)[0] == 'ङ्'


# TODO move this to an appropriate place
def आद्यन्तौ_टकितौ_१_१_४६(आगमः, स्थानी):
    if इत्(आगमः, उपदेशसंज्ञकः.आगमः) == 'ट्':
        आगमः = इत्संज्ञाप्रकरणम्(आगमः, उपदेशसंज्ञकः.आगमः)[:-1] + '्'
        return आगमः + स्थानी
    if इत्(लकारः, उपदेशसंज्ञकः.आगमः) == 'क्':
        आगमः = इत्संज्ञाप्रकरणम्(आगमः, उपदेशसंज्ञकः.आगमः)[:-1] + '्'
        return स्थानी + आगमः


def अचोऽन्त्यादि_टि_१_१_६४(शब्दः):
    टि_संज्ञा = आनय_टि_संज्ञाम्()
    हल् = वर्णाः('हल्')
    टि = re.search(टि_संज्ञा, शब्दः)
    if टि:
        टि = टि.group()
        if टि[0] in हल्:
            length = len(टि)
            if length > 1 and टि[1] not in हल्:
                return मात्रायाः_स्वरः(टि[1]) + (टि[2:] if length > 2 else '')
            else:
                return 'अ'
        return टि
    return None


def आनय_टि_संज्ञाम्():
    अल् = वर्णाः('अल्')
    हल् = वर्णाः('हल्')
    मात्राः = स्वरमात्राः()
    टि_संज्ञा = '[{अल्}][{मात्राः}]?(?!्)([{हल्}]्){{0,2}}$'.format(अल्=अल्, मात्राः=मात्राः, हल्=हल्)
    return टि_संज्ञा


def टित_आत्मनेपदानां_टेरे_३_४_७९(तिङ्):
    if तिङ् == 'थास्':
        return थासस्से_३_४_८०()
    else:
        टिसंज्ञा = आनय_टि_संज्ञाम्()
        हल् = वर्णाः('हल्')
        टि = re.search(टिसंज्ञा, तिङ्)
        if टि:
            टि = टि.group()
            आदेशः = स्वरात्_मात्रा('ए')
            if टि[0] in हल्:
                आदेशः = टि[0] + आदेशः
            return तिङ्.replace(टि, आदेशः)
        return तिङ्


def थासस्से_३_४_८०():
    return 'से'


def लिटस्तझयोरेशिरेच्_३_४_८१(तिङ्_प्रत्ययः):
    if तिङ्_प्रत्ययः == 'त':
        return 'एश्'
    elif तिङ्_प्रत्ययः == 'झ':
        return 'इरेच्'
    else:
        return तिङ्_प्रत्ययः


def परस्मैपदानां_णलतुसुस्थलथुसणल्वमाः_३_४_८२(पुरुषः, वचनम्):
    return ['णल्', 'अतुस्', 'उस्', 'थल्', 'अथुस्', 'अ', 'णल्', 'व', 'म'][पुरुषः * 3 + वचनम्]


def विदो_लटो_वा_३_४_८३(धातुः, लकारः):
    return धातुः == 'विदँ' and लकारः.लट् == लकारः


def ब्रुवः_पञ्चानामादित_आहो_ब्रुवः_३_४_८४(तिङन्तरूपम्):
    return तिङन्तरूपम्.धातुः == 'ब्रूञ्' and लकारः.लट् == तिङन्तरूपम्.लकारः and तिङन्तरूपम्.पुरुषः * 3 + तिङन्तरूपम्.वचनम् < 5


def लोटो_लङ्वत्_३_४_८५(तिङ्_प्रत्ययः, परस्मैपदम्, पुरुषः):
    # TODO : find the purpose  ( why like लङ्)
    if पुरुषः == 2 and स्वरात्_मात्रा('ए') in तिङ्_प्रत्ययः:
        return एत_ऐ_३_४_९३(तिङ्_प्रत्ययः)
    elif 'से' in तिङ्_प्रत्ययः or 'वे' in तिङ्_प्रत्ययः:
        return सवाभ्यां_वामौ_३_४_९१(तिङ्_प्रत्ययः)
    elif स्वरात्_मात्रा('ए') in तिङ्_प्रत्ययः:
        return आमेतः_३_४_९०(तिङ्_प्रत्ययः)
    elif तिङ्_प्रत्ययः == 'मिप्':
        return मेर्निः_३_४_८९(तिङ्_प्रत्ययः)
    elif तिङ्_प्रत्ययः == 'सिप्':
        return सेर्ह्यपिच्च_३_४_८७(तिङ्_प्रत्ययः)
    elif तिङ्_प्रत्ययः == 'अपित्':
        return वा_छन्दसि_३_४_८८(तिङ्_प्रत्ययः)
    else:
        return एरुः_३_४_८६(तिङ्_प्रत्ययः)


def एरुः_३_४_८६(तिङ्_प्रत्ययः):
    return तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('इ'), स्वरात्_मात्रा('उ'))


def सेर्ह्यपिच्च_३_४_८७(तिङ्_प्रत्ययः):
    return तिङ्_प्रत्ययः.replace('सिप्', 'हि')


def वा_छन्दसि_३_४_८८(तिङ्_प्रत्ययः):
    return तिङ्_प्रत्ययः.replace('अपित्', 'हि')


def मेर्निः_३_४_८९(तिङ्_प्रत्ययः):
    return तिङ्_प्रत्ययः.replace('मिप्', 'नि')


def आमेतः_३_४_९०(तिङ्_प्रत्ययः):
    return तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('ए'), 'आम्')


def सवाभ्यां_वामौ_३_४_९१(तिङ्_प्रत्ययः):
    तिङ्_प्रत्ययः = re.sub('से.*$', 'स्व', तिङ्_प्रत्ययः)
    return re.sub('वे.*$', 'वम्', तिङ्_प्रत्ययः)


def आडुत्तमस्य_पिच्च_३_४_९२(तिङ्_प्रत्ययः):
    return 'आट्'


def एत_ऐ_३_४_९३(तिङ्_प्रत्ययः):
    return तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('ए'), स्वरात्_मात्रा('ऐ')).replace('ए', 'ऐ')


def लेटोऽडाटौ_३_४_९४(तिङ्_प्रत्ययः, परस्मैपदम्, पुरुषः):
    # TODO - find the purpose
    if 'स' in तिङ्_प्रत्ययः and पुरुषः == 2:
        return स_उत्तमस्य_३_४_९८(तिङ्_प्रत्ययः)
    elif स्वरात्_मात्रा('इ') in तिङ्_प्रत्ययः and परस्मैपदम्:
        return इतश्च_लोपः_परस्मैपदेषु_३_४_९७(तिङ्_प्रत्ययः)
    elif स्वरात्_मात्रा('ए') in तिङ्_प्रत्ययः:
        return वैतोऽन्यत्र_३_४_९६(तिङ्_प्रत्ययः)
    elif स्वरात्_मात्रा('आ') in तिङ्_प्रत्ययः:
        return आत_ऐ_३_४_९५(तिङ्_प्रत्ययः)


def आत_ऐ_३_४_९५(तिङ्_प्रत्ययः):
    return तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('आ'), स्वरात्_मात्रा('ऐ'))


def वैतोऽन्यत्र_३_४_९६(तिङ्_प्रत्ययः):
    return तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('ए'), स्वरात्_मात्रा('ऐ')).replace('ए', 'ऐ')


def इतश्च_लोपः_परस्मैपदेषु_३_४_९७(तिङ्_प्रत्ययः):
    return तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('इ'), '')


def स_उत्तमस्य_३_४_९८(तिङ्_प्रत्ययः):
    return तिङ्_प्रत्ययः.replace('स्', '').replace('स', '')


def नित्यं_ङितः_३_४_९९(तिङ्_प्रत्ययः, परस्मैपदम्, पुरुषः):
    if पुरुषः == 2:
        return स_उत्तमस्य_३_४_९८(तिङ्_प्रत्ययः)

    if तिङ्_प्रत्ययः in ['तस्', 'थस्', 'थ', 'मिप्']:
        return तस्थस्थमिपां_तांतंतामः_३_४_१०१(तिङ्_प्रत्ययः)
    elif स्वरात्_मात्रा('इ') in तिङ्_प्रत्ययः:
        return इतश्च_३_४_१००(तिङ्_प्रत्ययः)


def इतश्च_३_४_१००(तिङ्_प्रत्ययः):
    return तिङ्_प्रत्ययः.replace(स्वरात्_मात्रा('इ'), '')


def तस्थस्थमिपां_तांतंतामः_३_४_१०१(तिङ्_प्रत्ययः):
    तस्थस्थमिपां = {
        'तस्': 'ताम्',
        'थस्': 'तम्',
        'थ': 'त',
        'मिप्': 'अमः'
    }
    return तस्थस्थमिपां.get(तिङ्_प्रत्ययः)


def लिङस्सीयुट्_३_४_१०२(तिङन्तरूपम्):
    प्रत्ययस्य_सूत्रम् = {
       'तिथोः': सुट्_तिथोः_३_४_१०७,
       'इट्': इटोऽत्_३_४_१०६,
       'झ': झस्य_रन्_३_४_१०५,
       'झि': झेर्जुस्_३_४_१०८
    }

    प्रत्ययः = 'तिथोः' if 'त' in तिङन्तरूपम्.तिङ्_प्रत्ययः or 'थ' in तिङन्तरूपम्.तिङ्_प्रत्ययः else तिङन्तरूपम्.तिङ्_प्रत्ययः
    सूत्रम् = प्रत्ययस्य_सूत्रम्.get(प्रत्ययः)

    if सूत्रम्:
        तिङन्तरूपम्.तिङ्_प्रत्ययः = सूत्रम्(तिङन्तरूपम्)

    if तिङन्तरूपम्.परस्मैपदम्:
        return यासुट्_परस्मैपदेषूदात्तो_ङिच्च_३_४_१०३(तिङन्तरूपम्.तिङ्_प्रत्ययः)
    else:
        return आद्यन्तौ_टकितौ_१_१_४६('सीयुट्', तिङन्तरूपम्.तिङ्_प्रत्ययः)


def यासुट्_परस्मैपदेषूदात्तो_ङिच्च_३_४_१०३(तिङ्_प्रत्ययः):
    return आद्यन्तौ_टकितौ_१_१_४६('यासुट्', तिङ्_प्रत्ययः)


# TODO : find the purpose of this
def किदाशिषि_३_४_१०४():
    return ''


def झस्य_रन्_३_४_१०५(तिङन्तरूपम्):
    return तिङन्तरूपम्.तिङ्_प्रत्ययः.replace('झ', 'रन्')


def इटोऽत्_३_४_१०६(तिङन्तरूपम्):
    return तिङन्तरूपम्.तिङ्_प्रत्ययः.replace('इट्', 'अत्')


def सुट्_तिथोः_३_४_१०७(तिङन्तरूपम्):
    तिथोः = 'त' if 'त' in तिङन्तरूपम्.तिङ्_प्रत्ययः else 'थ'
    return तिङन्तरूपम्.तिङ्_प्रत्ययः.replace(तिथोः, आद्यन्तौ_टकितौ_१_१_४६('सुट्', तिथोः))


def झेर्जुस्_३_४_१०८(तिङन्तरूपम्):
    if सिजभ्यस्तविदिभ्यः_च_३_४_१०९(तिङन्तरूपम्.तिङ्_प्रत्ययः):
        return तिङन्तरूपम्.तिङ्_प्रत्ययः.replace('झि', इत्संज्ञाप्रकरणम्('जुस्', उपदेशसंज्ञकः.प्रत्ययः))
    return तिङन्तरूपम्.तिङ्_प्रत्ययः


def सिजभ्यस्तविदिभ्यः_च_३_४_१०९(तिङन्तरूपम्):
    return (तिङन्तरूपम्.विकरणप्रत्ययः.प्रत्ययः == 'सिच्' or तिङन्तरूपम्.विकरणप्रत्ययः.संज्ञा in ['अभ्यस्तम्', 'द्वित्वम्']
            or तिङन्तरूपम्.धातुः == 'विद्')


def आतः_३_४_११०(तिङन्तरूपम्):
    विकरणप्रत्ययः = तिङन्तरूपम्.विकरणप्रत्ययः
    return (विकरणप्रत्ययः.प्रत्ययः == 'सिच्' and विकरणप्रत्ययः.परिणामः is None
            and विकरणप्रत्ययः.अङ्गम्[:-1] in ['आ', स्वरात्_मात्रा('आ')])


def लङः_शाकटायनस्यैव_३_४_१११(तिङन्तरूपम्):
    # TODO : purpose of this sutra?
    return तिङन्तरूपम्


def द्विषश्च_३_४_११२(तिङन्तरूपम्):
    # TODO : same as above
    return तिङन्तरूपम्


def लस्य_३_४_७७(तिङन्तरूपम्):
    तिङ्_प्रत्ययः = आनय_तिङ्_प्रत्ययम्(तिङन्तरूपम्.परस्मैपदम्, तिङन्तरूपम्.पुरुषः, तिङन्तरूपम्.वचनम्)

    if टित्_वा(तिङन्तरूपम्.लकारः.name) and not तिङन्तरूपम्.परस्मैपदम्:
        if तिङन्तरूपम्.लकारः == लकारः.लिट् and तिङ्_प्रत्ययः in ['त', 'झ']:
            तिङ्_प्रत्ययः = लिटस्तझयोरेशिरेच्_३_४_८१(तिङ्_प्रत्ययः)
        else:
            तिङ्_प्रत्ययः = टित_आत्मनेपदानां_टेरे_३_४_७९(तिङ्_प्रत्ययः)

    if तिङन्तरूपम्.परस्मैपदम्:
        if तिङन्तरूपम्.लकारः == लकारः.लिट्:
            तिङ्_प्रत्ययः = परस्मैपदानां_णलतुसुस्थलथुसणल्वमाः_३_४_८२(तिङन्तरूपम्.पुरुषः, तिङन्तरूपम्.वचनम्)

        ब्रुवः_पञ्चानामादि = ब्रुवः_पञ्चानामादित_आहो_ब्रुवः_३_४_८४(तिङन्तरूपम्)
        if विदो_लटो_वा_३_४_८३(तिङन्तरूपम्.धातुः, तिङन्तरूपम्.लकारः) or ब्रुवः_पञ्चानामादि:
            तिङ्_प्रत्ययः = [तिङ्_प्रत्ययः, परस्मैपदानां_णलतुसुस्थलथुसणल्वमाः_३_४_८२(तिङन्तरूपम्.पुरुषः, तिङन्तरूपम्.वचनम्)]
        if ब्रुवः_पञ्चानामादि:
            # TODO : return this as well
            तिङन्तरूपम्.धातुः = [तिङन्तरूपम्.धातुः, 'आह्']

    if ङित्_वा(तिङन्तरूपम्.लकारः.name):
        तिङ्_प्रत्ययः = नित्यं_ङितः_३_४_९९(तिङ्_प्रत्ययः, तिङन्तरूपम्.परस्मैपदम्, तिङन्तरूपम्.पुरुषः)

    लकार_सूत्राणि = {
        लकारः.लोट्: लोटो_लङ्वत्_३_४_८५,
        लकारः.लेट्: लेटोऽडाटौ_३_४_९४,
        लकारः.लिङ्: लिङस्सीयुट्_३_४_१०२
    }

    if लकार_सूत्राणि.get(तिङन्तरूपम्.लकारः) is not None:
        तिङ्_प्रत्ययः = लकार_सूत्राणि.get(तिङन्तरूपम्.लकारः)(तिङ्_प्रत्ययः, तिङन्तरूपम्.परस्मैपदम्, तिङन्तरूपम्.पुरुषः)

    तिङन्तरूपम्.तिङ्_प्रत्ययः = तिङ्_प्रत्ययः
    return तिङन्तरूपम्


def आनय_तिङ्_प्रत्ययम्(परस्मैपदम्, पुरुषः, वचनम्):
    पदम् = लः_परस्मैपदम्_१_४_९९() if परस्मैपदम् else तङानावात्मनेपदम्_१_४_१००()
    पुरुषः_प्रत्ययाः = तिङस्त्रीणि_त्रीणि_प्रथममध्यमोत्तमाः_१_४_१०१(पदम्, पुरुषः)
    return तान्येकवचनद्विवचनबहुवचनान्येकशः_१_४_१०२(पुरुषः_प्रत्ययाः, वचनम्)


if __name__ == '__main__':
    print(लस्य_३_४_७७(sys.argv[1], sys.argv[2], sys.argv[3] == 'परस्मैपदम्', int(sys.argv[4]), int(sys.argv[5])))
