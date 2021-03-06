#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from ashtadhyayi.sajna import ऊकालोऽज्झ्रस्वदीर्घप्लुतः_१_२_२७, हलोऽनन्तराः_संयोगः_१_१_७
from ashtadhyayi.utils import स्वरात्_मात्रा, स्वरमात्राः, स्वराः
from ashtadhyayi.pratyahara import वर्णाः


def ह्रस्वं_लघु_१_४_१०(अक्षराणि):
    ह्रस्वं = ऊकालोऽज्झ्रस्वदीर्घप्लुतः_१_२_२७()['ह्रस्वः']
    ह्रस्वं = ''.join(ह्रस्वं) + स्वरात्_मात्रा(ह्रस्वं)
    हल् = वर्णाः('हल्')
    return re.search('([{ह्रस्वं}])|([{हल्}])(?!्)'.format(ह्रस्वं=ह्रस्वं, हल्=हल्), अक्षराणि)


def संयोगे_गुरु_१_४_११(अक्षराणि):
    ह्रस्वं = ह्रस्वं_लघु_१_४_१०(अक्षराणि)
    if ह्रस्वं:
        परः = अक्षराणि.split(ह्रस्वं.group())[1]
        return हलोऽनन्तराः_संयोगः_१_१_७(परः) is not None


def दीर्घं_च_१_४_१२(अक्षराणि):
    दीर्घं = ऊकालोऽज्झ्रस्वदीर्घप्लुतः_१_२_२७()['दीर्घः']
    दीर्घं = ''.join(दीर्घं) + स्वरात्_मात्रा(दीर्घं)
    # TODO find relevant sutras for anusvara and visarga
    return re.search('[{दीर्घं}ंः]'.format(दीर्घं=दीर्घं), अक्षराणि)


def लघु_वा(अक्षरम्):
    if दीर्घं_च_१_४_१२(अक्षरम्):
        return False
    elif संयोगे_गुरु_१_४_११(अक्षरम्):
        return False
    else:
        लघु = ह्रस्वं_लघु_१_४_१०(अक्षरम्)
        if not लघु:
            raise AssertionError
        return True


def लघु_गुरु(अक्षराणि):
    स्वर = स्वराः() + स्वरमात्राः()
    हल् = वर्णाः('हल्')
    स्वराक्षरप्रतिरूपम् = '([{स्वर}][ंः]?([{हल्}]्)*)|([{हल्}](?![्{स्वरमात्राः}])([{हल्}]्)*)'
    स्वराक्षरप्रतिरूपम् = स्वराक्षरप्रतिरूपम्.format(स्वर=स्वर, हल्=हल्, स्वरमात्राः=स्वरमात्राः())
    स्वराक्षराणि = re.findall(स्वराक्षरप्रतिरूपम्, अक्षराणि)
    if स्वराक्षराणि:
        return [लघु_वा(स्वराक्षरम्[0] if स्वराक्षरम्[0] else स्वराक्षरम्[2]) for स्वराक्षरम् in स्वराक्षराणि]

    return None


def गुरुमत्(अक्षराणि):
    परिणामः = लघु_गुरु(अक्षराणि)
    if परिणामः:
        return not all(परिणामः)
    return False


def लः_परस्मैपदम्_१_४_९९(तिङ्_प्रत्ययाः):
    return तिङ्_प्रत्ययाः[:9]


def तङानावात्मनेपदम्_१_४_१००(तिङ्_प्रत्ययाः):
    return तिङ्_प्रत्ययाः[9:]


def तिङस्त्रीणि_त्रीणि_प्रथममध्यमोत्तमाः_१_४_१०१(प्रत्ययाः, पुरुषः):
    return प्रत्ययाः[3 * पुरुषः: 3 * (पुरुषः + 1)]


def तान्येकवचनद्विवचनबहुवचनान्येकशः_१_४_१०२(प्रत्ययाः, वचनम्):
    return प्रत्ययाः[वचनम्]


def आनय_तिङ्_प्रत्ययम्(परस्मैपदम्, पुरुषः, वचनम्, तिङ्_प्रत्ययाः):
    पदम् = लः_परस्मैपदम्_१_४_९९(तिङ्_प्रत्ययाः) if परस्मैपदम् else तङानावात्मनेपदम्_१_४_१००(तिङ्_प्रत्ययाः)
    पुरुषः_प्रत्ययाः = तिङस्त्रीणि_त्रीणि_प्रथममध्यमोत्तमाः_१_४_१०१(पदम्, पुरुषः)
    return तान्येकवचनद्विवचनबहुवचनान्येकशः_१_४_१०२(पुरुषः_प्रत्ययाः, वचनम्)
