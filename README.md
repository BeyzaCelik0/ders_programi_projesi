1- Proje Mimarisi

Backend (API):
Kullanılan Teknolojiler: Python, FastAPI, JWT, PostgreSQL
Amaç: Kullanıcı yönetimi, güvenlik (Token tabanlı kimlik doğrulama), dashboard verisi sağlama.

Frontend (UI):
Kullanılan Teknolojiler: HTML, CSS, JavaScript (Fetch/AJAX)
Amaç: Login ekranı, rol bazlı dashboard gösterimi, API ile iletişim.

2-Uygulamayı Başlatma

Backend API'yi Başlatma: Terminal üzerinden aşağıdaki komutla backend'i başlatın:

uvicorn backend.main:app --host 0.0.0.0 --port 8000

Bu komut, FastAPI uygulamasının çalışmaya başlamasını sağlar.

3-Frontend Testi

Uygulama çalıştıktan sonra, ana giriş ekranına görüntülemek için tarayıcınızı aşağıdaki adrese yönlendirin:
http://127.0.0.1:8000/frontend/index.html

test için oluşturulan hesaplar
admin-123456
dean-123456
department_rep-123456

4-Backend API Testi 

1.adım: Login ol ve token al
$LOGIN_RESPONSE = Invoke-RestMethod -Method POST -Uri "http://127.0.0.1:8000/api/login" `
-ContentType "application/x-www-form-urlencoded" `
-Body "username=admin&password=123456"

$TOKEN = $LOGIN_RESPONSE.access_token

Write-Host "--- Başarılı Alınan Token ---"
Write-Host $TOKEN

2.adım: Token ile Yetkili Endpoint'i Test Et
$HEADERS = @{
    "Authorization" = "Bearer $($TOKEN)"
}
~~~~
Kullanıcı verisini çekme testi
Invoke-RestMethod -Method GET -Uri "http://127.0.0.1:8000/api/dashboard/summary" -Headers $HEADERS
