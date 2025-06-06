# Gerçek Zamanlı Syntax Vurgulayıcı

Bursa Teknik Üniversitesi, Programlama Dilleri dersi kapsamında geliştirilmiş;

C benzeri diller ve kodlar için Python tabanlı, gerçek zamanlı syntax vurgulayıcı. Bu uygulama, sözcüksel ve snytax analizi prensiplerini kullanarak GUI'de yazım yapıldığı anda kodu vurgular. Projenin geliştirilmesinde bu görevi gören hazır hiçbir kütüphane kullanılmamıştır. 

## Özellikler

- 5 token türünün gerçek zamanlı syntax vurgulaması
- Düzenli ifadeler kullanan custom olarak hazırlanmış sözcüksel analizci
- Sözdizimsel doğrulama için yinelemeli descent parser'ı
- `Tkinter` ile oluşturulmuş kullanıcı dostu GUI
- Kolay genişletme için modüler kod temeli

## Token Türleri

Vurgulayıcı şu anda aşağıdaki token türlerini destekliyor:
- **KEYWORD** (örneğin, `int`, `return`, `if`)
- **IDENTIFIER** (örneğin, değişken isimleri)
- **NUMBER** (örneğin, `42`, `3.14`)
- **OPERATOR** (örneğin, `+`, `-`, `*`, `/`)
- **SYMBOL** (örneğin, `;`, `{`, `}`)

## GUI (Görsel Arayüz)

GUI, kullanıcı input girerken syntax'ı vurgulanmış metni görüntüler. `Tkinter` kullanılarak oluşturulmuştur ve tamamen responsive'dir.

## Nasıl Çalışır?

1. **Sözcüksel Analiz:** Input'u düzenli ifadeler kullanarak token'lara ayırır.
2. **Ayrıştırma:** Input yapısını, yinelemeli bir descent parser kullanarak doğrular.
3. **Vurgulama:** Etiketler, toekn türüne göre `Text` bileşenine uygulanır.

## Nasıl Çalıştırılır?

Bu projeyi çalıştırmak için Python 3 gereklidir.

```bash
# Projenin olduğu dizine gidin
cd .../syntax-highlighter-projesi

# Ana uygulamayı çalıştırın
python main.py
