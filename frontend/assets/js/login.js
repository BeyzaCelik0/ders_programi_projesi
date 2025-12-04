const API_BASE_URL = "http://127.0.0.1:8000"; // FastAPI sunucu adresi
const loginForm = document.getElementById('loginForm');
const errorMessage = document.getElementById('error-message');

if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault(); // Formun klasik submit işlemini engeller
        errorMessage.style.display = 'none'; // Önceki hataları gizler

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Form verisini URL-encoded formata dönüştürme
        const formData = new URLSearchParams();
        formData.append("username", username);
        formData.append("password", password);

        try {
            const response = await fetch(`${API_BASE_URL}/api/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: formData.toString()
            });

            const data = await response.json();

            if (response.ok) {
                // Başarılı giriş: Token'ı tarayıcıda sakla
                localStorage.setItem('access_token', data.access_token);

                // Dashboard sayfasına yönlendir
                window.location.href = 'dashboard.html';

            } else {
                // Hata mesajını göster
                errorMessage.textContent = data.detail || "Giriş başarısız oldu. Lütfen bilgileri kontrol edin.";
                errorMessage.style.display = 'block';
            }

        } catch (error) {
            console.error('Hata oluştu:', error);
            errorMessage.textContent = "Sunucuya bağlanılamadı. Uygulamanın çalıştığından emin olun.";
            errorMessage.style.display = 'block';
        }
    });
}