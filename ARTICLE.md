# Gerçek Zamanlı Syntax Vurgulayıcı

## Dil ve Gramer Seçimi 

Bu proje, okunabilirliği, hızlı geliştirmelere uygun olması, Tkinter gibi güçlü GUI geliştirme araçlarına sağladığı destekten dolayı **Python** dilinde geliştirilmiştir. Ayrıca projenin gerekliliklerinden birisi olan harici kütüphane kullanmama engelinden dolayı ihtiyacımız olan esnekliği sağlayabiliyor.

Kullanılan gramer oluşturulurken, anahtar kelimeleri, tanımlayıcıları (identifiers), sabit değerleri, operatörleri ve noktalama işaretlerini vurgulamak için uygun basitleştirilmiş yapılara sahip **C benzeri dillerden** esinlenildi. Dil bilgisisi bağlamdan bağımsızdır ve prosedürler (procs) bir programlama dilinin temsili bir alt kümesini desteklemek (kabul etmek) üzere tanımlanmıştır. 

## Syntax Analiz Süreci

Bu projedeki syntax analizi iki aşamalı bir süreçtir:
1. **Sözcüksel (Lexical) Analiz** – Düzenli ifadeler kullanarak kullanıcı girdisini gerçek zamanlı olarak belirteçleştirir (tokenizes).
2. **Ayrıştırma** – Belirteç (token) akışının sözdizimsel doğruluğunu doğrulamak için dilbilgisi kurallarını uygular.

İkisi beraber, doğru ve bağlama uygun vurgulamanın temelini oluşturan girdi kodunun yapısal olarak anlamamıza yardımcı olur.

## Sözcüksel (Lexical) Analiz

Sözcüksel analiz, **"Durum Diyagramı ve Program İmplementasyonu"** yöntemi kullanılarak uygulanıyor. Her belirteç (token), düzenli ifade düzenine göre tanımlanıyor. Anahtar token türleri şunları içerir:
- **Keywords (Anahtar Kelimeler)** (örneğin, `int`, `if`, `return`)
- **Identifiers (Tanımlayıcılar)** (değişken/fonksiyon adları)
- **Literals (Sabit Değerler)** (sayılar)
- **Operators (Operatörler)** (`+`, `-`, `=`, gibi)
- **Punctuation (Noktalama İşaretleri)** (`;`, `()`, `{}`, gibi)

Kullanıcı GUI üzerinden yazarken, sözcük çözücü (lexer) gerçek zamanlı olarak tetiklenir ve sonucunda anında geri bildirim ve dinamik token sınıflandırması sağlanır. 

## Ayrıştırma Uygulaması

Bu proje için basitliği ve yönetilebilirliği nedeniyle seçilen **Top-Down Parser** yaklaşımı kullanılır. Input'u, dilbilgisi kurallarını yinelemeli olarak uygulayarak başlangıç sembolünden türetmeye çalışır ve **preorder gezme** bir ayrıştırma ağacı (parse tree) üretir.

Bu ayrıştırıcı, token dizisinin basitleştirilmiş dilbilgisine uygun olup olmadığını doğrular. Tam parse tree üretimi görselleştirilmese de ayrıştırma, vurgulama (highlighting) için geçerli kod bölgelerinin belirlenmesine yardımcı olan input yapısının uygunluğunu doğrular.

## Vurgulama Şeması

Syntax vurgulayıcı, farklı renkler kullanarak aşağıdaki **beş token türünü** görsel olarak ayırt edecek şekilde yapılandırılmıştır:

- **Keywords (Anahtar Kelimeler)** – Mavi
- **Identifiers (Tanımlayıcılar)** – Siyah
- **Literals (Sabitler)** – Turuncu
- **Operators (Operatörler)** – Yeşil
- **Punctuation (Noktalama)** – Gri

Tkinter'daki `Text` widget'ı, uygulanan etiketlerle kodu işlemek için kullanılıyor. Kullanıcı yazdıkça, metin yeniden token'lanıyor ve anında güncelleniyor, böylelikle gerçek bir IDE benzeri ortamı simüle etmiş oluyoruz.

## GUI (Görsel Arayüz) İmplementasyonu

GUI, Python'un standart GUI araç takımı olan **Tkinter** kullanılarak oluşturulmuştur. Temel özellikleri:
- Kullanıcıların kod yazdığı tek bir `Text` input alanı
- `<<Modified>>` sanal olayı aracılığıyla gerçek zamanlı vurgulama (highlighting)
- `tag_add()` ve `tag_configure()` kullanılarak dinamik stillendirme

Tüm GUI değişiklikleri, nispeten ekonomik sistemlerde bile neredeyse gerçek zamanlı olarak gerçekleşir ve bu da responsive ve pürüzsüz bir kullanıcı deneyimi sağlar.

---

## Sonuç

Bu proje, resmi dilbilgisi ve sözcüksel ayrıştırma tekniklerini kullanarak sıfırdan bir syntax vurgulayıcı oluşturmanın hazır kütüphane kullanmadan uygulanabilirliğini gösteriyor. 