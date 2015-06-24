import sublime, sublime_plugin
import webbrowser
 
class OpenBrowserCommand(sublime_plugin.TextCommand):
    def run(self,edit):

        # read config
        url_map = sublime.load_settings("OpenBrowser.sublime-settings").get('path')

        window = sublime.active_window()

        # save file
        window.run_command('save')

        url = self.view.file_name()

        flag = False
        for path, domain in url_map.items():
            # path has last is '/'
            if path[-1:] == '/':
                path = path[:-1];

            if url.startswith(path):
                if domain[-1:] == '/':
                    domain = domain[:-1];

                url = url.replace(path, domain)#.replace('\\', '/')
                flag = True
                break


        if not flag:
            url = 'file://' + url
        webbrowser.open_new(url)