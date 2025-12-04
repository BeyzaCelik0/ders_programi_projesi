const API_BASE_URL = "http://127.0.0.1:8000";

document.addEventListener('DOMContentLoaded', () => {
    // 1. Token Kontrolü
    const token = localStorage.getItem('access_token');
    if (!token) {
        // Token yoksa kullanıcıyı login sayfasına gönder
        alert("Oturum süresi doldu veya yetkiniz yok.");
        window.location.href = 'index.html';
        return; // İşlemi durdur
    }

    // 2. Dashboard verisini çekme
    fetchDashboardData(token);
});

async function fetchDashboardData(token) {
    try {
        const response = await fetch(`${API_BASE_URL}/api/dashboard/summary`, {
            method: 'GET',
            headers: {
                // Yetkilendirme için token'ı 'Bearer' formatında gönder
                'Authorization': `Bearer ${token}`
            }
        });

        const data = await response.json();

        if (response.ok) {
            // Veri başarıyla çekildi, DOM'a yerleştir
            updateDashboard(data);
        } else {
            // Yetkilendirme hatası (örn: Token geçersiz)
            alert(`Yetkilendirme hatası: ${data.detail || 'Tekrar giriş yapınız.'}`);
            localStorage.removeItem('access_token');
            window.location.href = 'index.html';
        }

    } catch (error) {
        console.error('Dashboard veri çekme hatası:', error);
        alert("Dashboard verileri yüklenirken bir hata oluştu.");
    }
}

function updateDashboard(data) {
    // Verileri HTML'deki ilgili alanlara yerleştirir
    document.getElementById('welcome-user').textContent = data.username || 'Kullanıcı';
    document.getElementById('user-role').textContent = data.role || 'Rol Bilgisi Yok';
    document.getElementById('department-name').textContent = data.section || 'Bölüm Bilgisi Yok';
    document.getElementById('total-courses-count').textContent = data.total_courses || '0';
    document.getElementById('unplaced-courses-count').textContent = data.unplaced_courses || '0';
    document.getElementById('next-step-message').textContent = data.message || '';
}