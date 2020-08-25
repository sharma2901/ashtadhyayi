from ashtadhyayi.dhaatoho import सार्वधातुकम्_आर्धधातुकम्, धातोरेकाचो_हलादेः_क्रियासमभिहारे_यङ्_३_१_२२
from ashtadhyayi.angasya import आर्धधातुकस्येड्_वलादेः_७_२_३५, मिदेर्गुणः_७_३_८२
from ashtadhyayi.lasya import लस्य_३_४_७७
from ashtadhyayi.aardhadhatuke import आर्धधातुके_२_४_३५, आदेच_उपदेशेऽशिति_६_१_४५


class तिङन्तरूपम्:

    def __init__(self, धातुः, लकारः, परस्मैपदम्, पुरुषः, वचनम्):
        self.धातुः = धातुः
        self.लकारः = लकारः
        self.परस्मैपदम् = परस्मैपदम्
        self.पुरुषः = पुरुषः
        self.वचनम् = वचनम्
        self.तिङ्_प्रत्ययः = {'प्रत्ययः': None, 'सार्वधातुकम्': False, 'आर्धधातुकम्': False}
        self.विकरणप्रत्ययः = {'प्रत्ययः': None, 'सार्वधातुकम्': False, 'आर्धधातुकम्': False}
        self.कृत्प्रत्ययः = {'प्रत्ययः': None, 'सार्वधातुकम्': False, 'आर्धधातुकम्': False}
        self.लकारार्थः = None


def तिङन्तम्(धातुः, लकारः, परस्मैपदम्, पुरुषः, वचनम्):
    पदम् = तिङन्तरूपम्(धातुः, लकारः, परस्मैपदम्, पुरुषः, वचनम्)
    # प्रक्रिया
    धातोरेकाचो_हलादेः_क्रियासमभिहारे_यङ्_३_१_२२(पदम्)
    लस्य_३_४_७७(पदम्)
    सार्वधातुकम्_आर्धधातुकम्(पदम्)
    इडागमविधिः(पदम्)
    धात्वादेशः(पदम्)
    अतिदेशः_अङ्गकार्यः(पदम्)
    सामान्यअङ्गकार्यः(पदम्)
    षत्वविधिः(पदम्)

    return पदम्


def इडागमविधिः(पदम्):
    आर्धधातुकस्येड्_वलादेः_७_२_३५(पदम्)


def धात्वादेशः(पदम्):
    आर्धधातुके_२_४_३५(पदम्)
    आदेशः = आदेच_उपदेशेऽशिति_६_१_४५(पदम्)
    if आदेशः:
        पदम्.धातुः['आदेशः'] = आदेशः


def अतिदेशः_अङ्गकार्यः(पदम्):
    return मिदेर्गुणः_७_३_८२(पदम्)


def सामान्यअङ्गकार्यः(पदम्):
    return None


def षत्वविधिः(पदम्):
    return None


def तिङ्_प्रत्ययाः(रूपम्):
    return [[तिङ्_प्रत्ययः(रूपम्, पुरुषः, वचनम्) for वचनम् in range(3)] for पुरुषः in range(3)]


def तिङ्_प्रत्ययः(रूपम्, पुरुषः, वचनम्):
    return लस्य_३_४_७७(तिङन्तरूपम्(*रूपम्, पुरुषः, वचनम्)).तिङ्_प्रत्ययः['प्रत्ययः']
