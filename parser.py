# Yinelemeli Top-Down Parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        # Tüm tokenlar bitene kadar statement'ları analiz ediyoruz.
        while not self.is_at_end():
            self.statement()

    # Bir statement, ya bir değişken tanımlaması (örneğin: int x;) ya da bir ifade olabilir (örneğin: x + 5)
    # Bu fonksiyon, hangi tür statement olduğunu belirler ve gerekli işlemi yapan fonksiyondur.
    def statement(self):
        # Eğer 'int' anahtar kelimesi ile başlıyorsa bir değişken tanımıdır
        if self.eslestir("KEYWORD") and self.current_token()["value"] == "int":
            self.degisken_tanimlama()
        else:
            # Aksi halde bir ifade bekleniyor
            self.expression()

    # Değişken tanımı: int x; 
    # gibi bir yapıyı işleyen fonksiyon
    def degisken_tanimlama(self):
        # 'int' anahtar kelimesini tüket
        self.consume("KEYWORD")
        # Bir değişken ismi beklenir (identifier)
        self.consume("IDENTIFIER")
        # Tanımın sonunda noktalı virgül olmalı
        self.consume("SYMBOL", ";")

    # İfade (expression): toplama ve çıkarma işlemlerini destekleyen fonksiyon
    def expression(self):
        self.carpma_bolme()
        # '+' veya '-' geldiği sürece haliyle sonraki yeni terimler beklenir
        while self.eslestir("OPERATOR", "+", "-"):
            self.carpma_bolme()

    # Çarpma ve bölme işlemleri bu fonksiyonda işleniyor
    def carpma_bolme(self):
        self.factor()
        while self.eslestir("OPERATOR", "*", "/"):
            self.factor()

    # Sayı, değişken veya parantezli ifadeleri işleyen fonksiyon
    def factor(self):
        if self.eslestir("NUMBER") or self.eslestir("IDENTIFIER"):
            return
        elif self.eslestir("SYMBOL", "("):
            self.expression()
            self.consume("SYMBOL", ")")

    # Sıradaki token beklenen tipte ve (isteğe bağlı olarak) belirli bir değerdeyse alan (tüketen) fonksiyon
    def eslestir(self, type_, *values):
        if self.is_at_end():
            return False
        tok = self.current_token()
        # Tip uyuşmuyorsa yanlış
        if tok["type"] != type_:
            return False
        # Eğer değerler belirtilmişse, bunlardan biri olmalı
        if values and tok["value"] not in values:
            return False
        # Token uygunsa işaretçiyi bir sonraki token'a kaydırırız
        self.current += 1
        return True

    # Beklenen token varsa alan (tüketir), yoksa bir hata fırlatan fonksiyon
    def consume(self, type_, value=None):
        if self.eslestir(type_, value):
            return
        raise Exception(f"Expected {type_} {value}")

    # Şu anki token'ı döndüren fonksiyon
    def current_token(self):
        return self.tokens[self.current]

    # Token dizisinin sonuna gelip gelmediğimizi kontrol eden fonksiyon
    def is_at_end(self):
        return self.current >= len(self.tokens)
