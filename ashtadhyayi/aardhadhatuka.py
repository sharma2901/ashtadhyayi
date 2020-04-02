#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def आर्धधातुकस्येड्_वलादेः_७_२_३५(सेट्धातु, आर्धधातुक_विकरण_सेट्_प्रत्यय):
    if वल्(आर्धधातुक_विकरण_सेट्_प्रत्यय[0]):
        return सेट्धातु[:-1] + 'ि' + आर्धधातुक_विकरण_सेट्_प्रत्यय
    else:
        return सेट्धातु[:-1] + आर्धधातुक_विकरण_सेट्_प्रत्यय

def वल्(वर्ण):
    #करणीयम् : प्रत्याहारसूत्रात् वल् वा इति ज्ञातव्यम् 
    return वर्ण in list('कखगघङचछजझञटठडढणतथदधनपफबभमरलवशषसह')

def अस्तेर्भूः_२_४_५२():
    return 'भू'

def ब्रुवो_वचिः_२_४_५३():
    return 'वच्'

def चक्षिङः_ख्याञ्_२_४_५४():
    return 'ख्या'

def अजेर्व्यघञपोः_२_४_५६():
    return 'वी'

def धात्वादेश(धातु, प्रत्यय):   
    धात्वादेश = {
        'अस्' : अस्तेर्भूः_२_४_५२,
        'ब्रू' : ब्रुवो_वचिः_२_४_५३,
        'चक्ष्' : चक्षिङः_ख्याञ्_२_४_५४,
        'अज्' : अजेर्व्यघञपोः_२_४_५६
    }
    if धातु in धात्वादेश:
        return धात्वादेश[धातु]()
    else :
        return आदेच_उपदेशेऽशिति_६_१_४५(धातु, प्रत्यय)

#करणीयम् - सम्पूर्णम् 
आर्धधातुक_विकरण_प्रत्यय = ['सिप्']

def आदेच_उपदेशेऽशिति_६_१_४५(धातु, प्रत्यय):
    #' ेैोौ' = ' े'+'ेै'+'ो'+'ौ' - एजन्त
    if धातु[-1] in ' ेैोौ' and प्रत्यय in आर्धधातुक_विकरण_प्रत्यय:
        return  धातु[:-1] + 'ा'
    else :
        return धातु
