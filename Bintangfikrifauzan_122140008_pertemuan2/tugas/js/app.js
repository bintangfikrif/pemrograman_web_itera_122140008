document.addEventListener('DOMContentLoaded', () => {
    // Gunakan async function untuk memastikan semua sudah dimuat
    const initApp = async () => {
        try {
            // Membuat instance baru FinancialTracker
            const tracker = new FinancialTracker();
            console.log('Aplikasi Tracker Keuangan Mahasiswa berhasil dimuat');
        } catch (error) {
            console.error('Error initializing app:', error);
        }
    };
    
    // Memulai aplikasi
    initApp();
});