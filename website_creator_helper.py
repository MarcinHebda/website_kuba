import json

class KubaWebsite:


    def __init__(self):

        self.menu_list = []
        self.html_parts_dir = 'html_parts'
        self.content_dir = 'site_content'

    def get_menu(self):
        with open('menu.json', 'r') as data_file:
            return json.load(data_file)


    def create_submenu(self, submenu_list, menu_item_filename=''):

        submenu_content = '\t\t\t\t<ul class="dropdown-content">\n'
        for sml in submenu_list:
            current_class = 'class="current" ' if menu_item_filename == sml['filename'] else ''
            submenu_content += '\t\t\t\t\t<li><a ' + current_class + 'href="' + sml['filename'] + '.html">' + sml['name'] + '</a></li>\n'
        submenu_content += '\t\t\t\t</ul>\n'
        return submenu_content


    def create_menu(self, menu_item_filename=''):

        """ count of menu items have to be SEVEN! """

        self.menu_list = self.get_menu()

        menu_content = '\t<div class="header-menu">\n\t\t<ul class="dropdown">\n'
        for sml in self.menu_list:
            current_class = 'class="current" ' if menu_item_filename == sml['filename'] else ''
            menu_content += '\t\t\t<li><a ' + current_class + 'href="' + sml['filename'] + '.html">' + sml['name']
            if 'sub' in sml:
                menu_content += self.create_submenu(sml['sub'], menu_item_filename)
            menu_content += '</a></li>\n'
        menu_content += '\t\t</ul>\n\t</div><!-- .header-menu" -->\n'

        with open(self.html_parts_dir + '/' + 'header-menu.hp', 'w', encoding='UTF-8') as file_content:
            file_content.write(menu_content)


    def create_content_part(self, menu_item_filename):

        site_content = '\t<div class="content">\n\t\t<div class="content-inner">\n\t\t\t<div class="column-left">\n\t\t\t\t<img src="img/content_column_left_01.png" />\n\t\t\t\t<img src="img/content_column_left_02.png" />\n\t\t\t\t<img src="img/content_column_left_03.png" />\n\t\t\t</div><!-- .column-left -->\n\t\t\t<div class="column-center">\n\n'
        with open(self.content_dir + '/' + menu_item_filename + '.sc', 'r', encoding="UTF-8") as file_content:
            site_content += file_content.read()
        site_content += '\n\t\t\t</div><!-- .column-center -->\n\t\t\t<div class="column-right">\n\t\t\t\t<img class="photo" src="img/content_column_right_01.jpg" />\n\t\t\t\t<img class="photo" src="img/content_column_right_01.jpg" />\n\t\t\t</div><!-- column-right -->\n\t\t</div><!-- .content-inner -->\n\t</div><!-- .content -->\n'

        with open(self.html_parts_dir + '/' + 'content.hp', 'w', encoding="UTF-8") as file_content:
            file_content.write(site_content)


    def get_site_part(self, filename):

        with open(self.html_parts_dir + '/' + filename, 'r', encoding="UTF-8") as file_content:
            return file_content.read()


    def create_site(self, menu_item_filename):

        self.create_menu(menu_item_filename)
        self.create_content_part(menu_item_filename)

        site_content = ''
        site_content += self.get_site_part('begin.hp')
        site_content += '\n\n'
        site_content += self.get_site_part('header.hp')
        site_content += '\n\n'
        site_content += self.get_site_part('header-menu.hp')
        site_content += '\n\n'
        site_content += self.get_site_part('content.hp')
        site_content += '\n\n'
        site_content += self.get_site_part('footer.hp')
        site_content += '\n\n'
        site_content += self.get_site_part('end.hp')

        with open(menu_item_filename + '.html', 'w', encoding='UTF-8') as file_content:
            file_content.write(site_content)