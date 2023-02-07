# speedtest
İnternet hız testi uygulaması. (Python)

Bu Python programı, internet hızını test etmek için "speedtest" modülünü kullanır. İlk olarak, program sunucuları listelemek için "speedtest" nesnesini oluşturur. 
Daha sonra, en iyi sunucuyu seçmek için "get_best_server()" metodunu çağırır. En iyi sunucunun bulunduğu ülke ve host adresi yazdırılır.

Sonra, "download()" ve "upload()" metodları çağrılarak indirme ve yükleme hızı testleri gerçekleştirilir. Sonuçların "results" özelliği kullanılarak "ping" süresi 
de alınır. Alınan sonuçlar, indirme hızı, yükleme hızı ve ping süresi olarak MBit/s ve ms cinsinden yazdırılır.

Son olarak, kullanıcıdan bir tuşa basması istenir ve "msvcrt" modülünün "getch()" metodu kullanılarak beklenir. Böylece program konsol ekranında sonuçları 
görüntüleyebilir.
