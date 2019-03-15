from website_creator_helper import KubaWebsite


kw = KubaWebsite()

menu_list = kw.get_menu()

for ml in menu_list:
    kw.create_site(ml['filename'])
    if 'sub' in ml:
        for sml in ml['sub']:
            kw.create_site(sml['filename'])