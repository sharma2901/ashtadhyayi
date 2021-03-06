स्वरात्_स्वरमात्राः = {
                'अ': '',
                'आ': 'ा',
                'इ': 'ि',
                'ई': 'ी',
                'उ': 'ु',
                'ऊ': 'ू',
                'ऋ': 'ृ',
                'ॠ': 'ॄ',
                'ऌ': 'ॢ',
                'ए': 'े',
                'ऐ': 'ै',
                'ओ': 'ो',
                'औ': 'ौ',
                'अं': 'ं',
                'अः': 'ः'}

मात्राभ्यः_स्वराः = {
                '': 'अ',
                'ा': 'आ',
                'ि': 'इ',
                'ी': 'ई',
                'ु': 'उ',
                'ू': 'ऊ',
                'ृ': 'ऋ',
                'ॄ': 'ॠ',
                'ॢ': 'ऌ',
                'े': 'ए',
                'ै': 'ऐ',
                'ो': 'ओ',
                'ौ': 'औ',
                'ं': 'अं',
                'ः': 'अः'}


def स्वरात्_मात्रा(स्वराः):
    return ''.join(स्वरात्_स्वरमात्राः.get(स्वरः) for स्वरः in स्वराः)


def मात्रायाः_स्वरः(मात्राः):
    return ''.join(मात्राभ्यः_स्वराः.get(मात्रा) for मात्रा in मात्राः)


def स्वरमात्राः():
    return ''.join([स्वरमात्रा for स्वरमात्रा in स्वरात्_स्वरमात्राः.values()])


def स्वराः():
    return ''.join([स्वरमात्रा for स्वरमात्रा in स्वरात्_स्वरमात्राः.keys()])
