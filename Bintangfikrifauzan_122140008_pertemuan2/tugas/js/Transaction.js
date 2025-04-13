class Transaction {
    /**
     * Membuat instance transaksi baru
     * @param {string} id - ID unik untuk transaksi
     * @param {number} amount - Jumlah uang
     * @param {string} description - Deskripsi transaksi
     * @param {string} category - Kategori transaksi
     * @param {string} type - Tipe transaksi (income/expense)
     * @param {Date} date - Tanggal transaksi
     */
    constructor(id, amount, description, category, type, date) {
        this.id = id;
        this.amount = amount;
        this.description = description;
        this.category = category;
        this.type = type;
        this.date = date;
    }
    
    /**
     * Mendapatkan jumlah dalam format mata uang Indonesia
     * @return {string} Jumlah diformat dalam Rupiah
     */
    get formattedAmount() {
        return new Intl.NumberFormat('id-ID', { 
            style: 'currency', 
            currency: 'IDR',
            minimumFractionDigits: 0,
            maximumFractionDigits: 0
        }).format(this.amount);
    }
    
    /**
     * Mendapatkan tanggal dalam format Indonesia
     * @return {string} Tanggal diformat dalam bahasa Indonesia
     */
    get formattedDate() {
        return new Date(this.date).toLocaleDateString('id-ID', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    }
}