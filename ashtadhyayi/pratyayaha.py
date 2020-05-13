#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def प्रत्ययः_३_१_१(प्रत्ययः):
    परश्च_३_१_२(प्रत्ययः)


def परश्च_३_१_२(प्रत्ययः):
    if प्रत्ययः.संज्ञा in ['सुप्', 'पित्']:
        अनुदात्तौ_सुप्पितौ_३_१_४(प्रत्ययः)
    else:
        आद्युदात्तश्च_३_१_३(प्रत्ययः)


def आद्युदात्तश्च_३_१_३(प्रत्ययः):
    # TODO :
    return


def अनुदात्तौ_सुप्पितौ_३_१_४(प्रत्ययः):
    # TODO :
    return


def गुप्तिज्किद्भ्यः_सन्_३_१_५(पदम्):
    if पदम्.धातुः in ['गुप्', 'तिज्', 'कित्']:
        पदम्.प्रत्ययः.संज्ञा = 'सन्'


def मान्बधदान्शान्भ्यो_दीर्घश्चाभ्यासस्य_३_१_६(पदम्):
    if पदम्.धातुः in ['मान्', 'बध', 'दान्', 'शान्']:
        पदम्.प्रत्ययः.संज्ञा = 'सन्'
        # TODO पदम्.अभ्यासः deergha


def धातोः_कर्मणः_समानकर्तृकादिच्छायां_वा_३_१_७(पदम्):
    # TODO :
    pass


def सुप_आत्मनः_क्यच्_३_१_८():
    # TODO :
    pass


def काम्यच्च_३_१_९():
    # TODO :
    pass


def उपमानादाचारे_३_१_१०():
    # TODO :
    pass


def कर्तुः_क्यङ्_सलोपश्च_३_१_११():
    # TODO :
    pass


def भृशादिभ्यो_भुव्यच्वेर्लोपश्च_हलः_३_१_१२():
    # TODO :
    pass


def लोहितादिडाज्भ्यः_क्यष्_३_१_१३():
    # TODO
    pass


def कष्टाय_क्रमणे_३_१_१४():
    # TODO
    pass


def कर्मणः_रोमन्थतपोभ्यां_वर्तिचरोः_३_१_१५():
    # TODO
    pass


def बाष्पोष्मभ्यामुद्वमने_३_१_१६():
    # TODO
    pass


def शब्दवैरकलहाभ्रकण्वमेघेभ्यः_करणे_३_१_१७():
    # TODO
    pass


def सुखादिभ्यः_कर्तृवेदनायाम्_३_१_१८():
    # TODO
    pass


def नमोवरिवश्चित्रङः_क्यच्_३_१_१९():
    # TODO
    pass


def पुच्छभाण्डचीवराण्णिङ्_३_१_२०():
    # TODO
    pass


def मुण्डमिश्रश्लक्ष्णलवणव्रतवस्त्रहलकलकृततूस्तेभ्यो_णिच्_३_१_२१():
    # TODO
    pass


def धातोरेकाचो_हलादेः_क्रियासमभिहारे_यङ्_३_१_२२(पदम्):

    if पदम्.लकारः == 'लेट्':
        सिब्बहुलं_लेटि_३_१_३४(पदम्)

    if पदम्.धातुः == 'कमेर्':
        आयादयः = कमेर्णिङ्_३_१_३०()

    if पदम्.धातुः == 'ऋति':
        आयादयः = ऋतेरीयङ्_३_१_२९()

    if पदम्.धातुः in 'गुपू-धूप-विच्छि-पणि-पनि':
        आयादयः = गुपूधूपविच्छिपणिपनिभ्य_आयः_३_१_२८()

    if पदम्.आर्धधातुकम्:
        पदम्.प्रत्ययः = आयादय_आर्धधातुके_वा_३_१_३१(आयादयः)
    else:
        पदम्.प्रत्ययः = आयादयः

    # TODO
    pass


def नित्यं_कौटिल्ये_गतौ_३_१_२३():
    # TODO
    pass


def लुपसदचरजपजभदहदशगॄभ्यो_भावगर्हायाम्_३_१_२४():
    # TODO
    pass


def सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो_णिच्_३_१_२५():
    # TODO
    pass


def हेतुमति_च_३_१_२६():
    # TODO
    pass


def कण्ड्वादिभ्यो_यक्_३_१_२७():
    # TODO
    pass


def गुपूधूपविच्छिपणिपनिभ्य_आयः_३_१_२८():
    return 'आय'


def ऋतेरीयङ्_३_१_२९():
    return 'ईयङ्'


def कमेर्णिङ्_३_१_३०():
    return 'णिङ्'


def आयादय_आर्धधातुके_वा_३_१_३१(आयादयः):
    if आयादयः:
        return [None, आयादयः]


def सनाद्यन्ता_धातवः_३_१_३२():
    # TODO
    pass


def स्यतासी_लृलुटोः_३_१_३३(पदम्):
    if पदम्.लकारः in ['लृङ्', 'लृट्']:
        पदम्.प्रत्ययः = 'स्य'
    if पदम्.लकारः == 'लुट्':
        पदम्.प्रत्ययः = 'तास्'
    return


def सिब्बहुलं_लेटि_३_१_३४(पदम्):
    पदम्.प्रत्ययः = 'सिप्'
