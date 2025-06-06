import tkinter as tk
from lexer import tokenize
from styles import TOKEN_STYLES

# Gerçek zamanlı syntax vurgulayıcı uygulaması için Tkinter kullanarak basit bir GUI oluşturuyoruz.
class SyntaxVurgulayiciProjesi:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerçek Zamanlı Syntax Vurgulayıcı")
        self.text = tk.Text(root, wrap='word')
        self.text.pack(expand=1, fill='both')
        self.text.bind("<KeyRelease>", self.highlight)
        self.etiket_olustur()

    # Metin alanında her token türü için etiketleri ayarlıyoruz.
    def etiket_olustur(self):
        for token_type, style in TOKEN_STYLES.items():
            self.text.tag_configure(token_type, **style)

    # Kullanıcı her tuşa bastığında veya metin değiştiğinde bu fonksiyon çağrılıyor ve uygun vurgulamaları yapıyor.
    def highlight(self, event=None): 
        code = self.text.get("1.0", "end-1c")
        self.text.tag_remove("KEYWORD", "1.0", "end")
        self.text.tag_remove("IDENTIFIER", "1.0", "end")
        self.text.tag_remove("NUMBER", "1.0", "end")
        self.text.tag_remove("OPERATOR", "1.0", "end")
        self.text.tag_remove("SYMBOL", "1.0", "end")
        tokens = tokenize(code)
        for token in tokens: 
            start, end, token_type = token["start"], token["end"], token["type"]
            self.text.tag_add(token_type, start, end)

if __name__ == "__main__":
    root = tk.Tk()
    app = SyntaxVurgulayiciProjesi(root)
    root.mainloop()
