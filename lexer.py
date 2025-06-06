# Sözcüksel Analizci (Lexer) için düzenli ifadeler kullanarak oluşturulmuş kodumuz. 
import re

# Token türlerini ve düzenli ifadelerini tanımlıyoruz.
TOKEN_REGEX = [
    ("KEYWORD", r"\b(int|float|return|if|else|while|for)\b"),
    ("IDENTIFIER", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    ("NUMBER", r"\b\d+(\.\d+)?\b"),
    ("OPERATOR", r"[+\-*/=]"),
    ("SYMBOL", r"[{}()\[\];,]"),
]

# Tokenize fonksiyonu, verilen kodu satır satır okuyarak token'lara ayırıyor.
def tokenize(code):
    lines = code.split('\n')
    tokens = []
    for lineno, line in enumerate(lines, start=1): # Satır numarasını 1'den başlatıyoruz
        index = 0
        while index < len(line):
            match = None
            for token_type, pattern in TOKEN_REGEX: 
                regex = re.compile(pattern) # Token türüne göre düzenli ifade oluşturuyoruz
                match = regex.match(line, index) # Token'ı bulmaya çalışıyoruz
                if match:
                    start_col = match.start() # Token başlangıç sütunu
                    end_col = match.end() # Token bitiş sütunu
                    start_index = f"{lineno}.{start_col}"
                    end_index = f"{lineno}.{end_col}"
                    tokens.append({
                        "type": token_type, # Token türü
                        "start": start_index, # Token başlangıç indeksi
                        "end": end_index # Token bitiş indeksi
                    })
                    index = end_col
                    break
            if not match:
                index += 1
    return tokens
