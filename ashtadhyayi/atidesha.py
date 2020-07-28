from ashtadhyayi.it_samjna_prakarana import णित्_वा, ञित्_वा


def गाङ्कुटादिभ्योऽञ्णिन्ङित्_१_२_१(पदम्):
    if पदम्.धातुः['आदेशः'] == 'गाङ्‌' or पदम्.धातुः['गणः'] == 'कुटादिः' or विज_इट्_१_२_२(पदम्):
        प्रत्ययः = पदम्.विकरणप्रत्ययः['प्रत्ययः']
        if not णित्_वा(प्रत्ययः) and not ञित्_वा(प्रत्ययः):
            पदम्.विकरणप्रत्ययः['अतिदेशः'] == 'ङित्'


def विज_इट्_१_२_२(पदम्):
    return पदम्.धातुः['धातुः'] == 'विज्' and पदम्.विकरणप्रत्ययः.get('इडागमः')