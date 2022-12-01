import webview

class Api:
    
    def closePage(self):
        window.destroy()
     
    def minimizePage(self):
        window.minimize()

if __name__ == '__main__':
    api = Api()
    
    window = webview.create_window('Trader Calculator', 'index.html', frameless=True, easy_drag=True, resizable=False, width=470, height=550, js_api=api)
    webview.start(debug=False,http_server=False)
