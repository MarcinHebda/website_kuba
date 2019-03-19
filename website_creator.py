from website_creator_helper import KubaWebsite


kw = KubaWebsite()

menu_list = kw.get_menu()

for ml in menu_list:
    if 'sub' not in ml:
        kw.create_site(ml['filename'])
    else:
        for sml in ml['sub']:
            kw.create_site(sml['filename'])

