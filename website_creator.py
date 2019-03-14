from website_creator_helper import KubaWebsite


kw = KubaWebsite()

kw.menu_list = [
    {
        'name': 'STRONA GŁÓWNA',
        'filename': 'index',
    },
    {
        'name': 'OPIS CHOROBY',
        'filename': 'opis-choroby',
    },
    {
        'name': 'LECZENIE',
        'filename': 'leczenie',
    },
    {
        'name': 'PO ZDROWIE',
        'filename': 'po-zdrowie',
        'sub': [
            {
                'name': 'OPERACJE',
                'filename': 'operacje',
            },
            {
                'name': 'REHABILITACJA',
                'filename': 'rehabilitacja',
            },
            {
                'name': 'CO DALEJ?',
                'filename': 'co-dalej',
            },
        ]
    },
    {
        'name': 'PODARUJ 1%',
        'filename': 'podaruj-1',
    },
    {
        'name': 'PODZIĘKOWANIA',
        'filename': 'podziekowania',
    },
    {
        'name': 'KONTAKT',
        'filename': 'kontakt',
    },
]

for kml in kw.menu_list:
    kw.create_site(kml['filename'])