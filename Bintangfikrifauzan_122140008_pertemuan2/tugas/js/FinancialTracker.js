class FinancialTracker {
    /**
     * Inisialisasi financial tracker
     */
    constructor() {
        this.transactions = [];
        this.budget = 0;
        this.chart = null;
        this.loadFromLocalStorage();
        this.setupEventListeners();
        this.renderTransactions();
        this.updateSaldo();
        this.updateBudgetDisplay();
        this.renderChart();
    }
    
    /**
     * Memuat data dari localStorage
     */
    loadFromLocalStorage() {
        try {
            // Load transactions
            const savedTransactions = localStorage.getItem('transactions');
            if (savedTransactions) {
                const parsedTransactions = JSON.parse(savedTransactions);
                this.transactions = parsedTransactions.map(t => 
                    new Transaction(t.id, t.amount, t.description, t.category, t.type, t.date)
                );
            }
            
            // Load budget
            const savedBudget = localStorage.getItem('budget');
            if (savedBudget) {
                this.budget = parseFloat(savedBudget);
                document.getElementById('budgetAmount').value = this.budget;
            }
        } catch (error) {
            console.error('Error loading data from localStorage:', error);
            this.transactions = [];
            this.budget = 0;
        }
    }
    
    /**
     * Menyimpan data ke localStorage
     */
    saveToLocalStorage() {
        try {
            localStorage.setItem('transactions', JSON.stringify(this.transactions));
            localStorage.setItem('budget', this.budget.toString());
        } catch (error) {
            console.error('Error saving to localStorage:', error);
        }
    }
    
    /**
     * Menyiapkan event listeners
     */
    setupEventListeners() {
        // Form submission for new transactions
        const transactionForm = document.getElementById('transactionForm');
        transactionForm.addEventListener('submit', this.handleNewTransaction.bind(this));
        
        // Button to clear all transactions
        const clearBtn = document.getElementById('clearBtn');
        clearBtn.addEventListener('click', this.clearAllTransactions.bind(this));
        
        // Budget form submission
        const budgetForm = document.getElementById('budgetForm');
        budgetForm.addEventListener('submit', this.handleBudgetUpdate.bind(this));
    }
    
    /**
     * Penanganan event untuk transaksi baru
     * @param {Event} e - Event form submission
     */
    handleNewTransaction(e) {
        e.preventDefault();
        
        // Get form values
        const amount = parseFloat(document.getElementById('amount').value);
        const description = document.getElementById('description').value;
        const category = document.getElementById('category').value;
        const type = document.getElementById('type').value;
        
        if (amount <= 0) {
            alert('Jumlah harus lebih dari 0');
            return;
        }
        
        // Create new transaction
        const transaction = new Transaction(
            Date.now().toString(),
            amount,
            description,
            category,
            type,
            new Date()
        );
        
        // Add to array and save
        this.transactions.unshift(transaction);
        this.saveToLocalStorage();
        
        // Update UI
        this.renderTransactions();
        this.updateSaldo();
        this.updateBudgetDisplay();
        this.renderChart();
        
        // Reset form
        transactionForm.reset();
    }
    
    /**
     * Menghapus semua transaksi
     */
    clearAllTransactions() {
        if (confirm('Apakah kamu yakin ingin menghapus semua transaksi?')) {
            this.transactions = [];
            this.saveToLocalStorage();
            this.renderTransactions();
            this.updateSaldo();
            this.updateBudgetDisplay();
            this.renderChart();
        }
    }
    
    /**
     * Penanganan event untuk update budget
     * @param {Event} e - Event form submission
     */
    handleBudgetUpdate(e) {
        e.preventDefault();
        const budgetAmount = parseFloat(document.getElementById('budgetAmount').value) || 0;
        this.budget = budgetAmount;
        this.saveToLocalStorage();
        this.updateBudgetDisplay();
        alert('Budget berhasil disimpan!');
    }
    
    /**
     * Menghitung saldo saat ini
     * @return {number} Saldo total
     */
    calculateSaldo() {
        return this.transactions.reduce((saldo, transaction) => {
            if (transaction.type === 'income') {
                return saldo + transaction.amount;
            } else {
                return saldo - transaction.amount;
            }
        }, 0);
    }
    
    /**
     * Memperbarui tampilan saldo
     */
    updateSaldo() {
        const saldoDisplay = document.getElementById('saldoDisplay');
        const currentSaldo = this.calculateSaldo();
        
        saldoDisplay.textContent = new Intl.NumberFormat('id-ID', { 
            style: 'currency', 
            currency: 'IDR',
            minimumFractionDigits: 0,
            maximumFractionDigits: 0
        }).format(currentSaldo);
        
        // Change color based on balance
        if (currentSaldo < 0) {
            saldoDisplay.className = 'saldo-display saldo-negative';
        } else {
            saldoDisplay.className = 'saldo-display saldo-positive';
        }
    }
    
    /**
     * Render daftar transaksi
     */
    renderTransactions() {
        const transactionsList = document.getElementById('transactionsList');
        
        // Clear existing list
        transactionsList.innerHTML = '';
        
        if (this.transactions.length === 0) {
            transactionsList.innerHTML = '<p style="text-align: center; padding: 20px;">Belum ada transaksi</p>';
            return;
        }
        
        // Add each transaction to the list
        this.transactions.forEach(transaction => {
            const transactionElement = document.createElement('div');
            transactionElement.className = `transaction-item transaction-${transaction.type}`;
            
            // Use template literal for dynamic rendering
            transactionElement.innerHTML = `
                <div class="transaction-date">${transaction.formattedDate}</div>
                <div class="transaction-desc">
                    <strong>${transaction.description}</strong>
                    <div>${transaction.category}</div>
                </div>
                <div class="transaction-amount">
                    ${transaction.type === 'income' ? '+' : '-'} ${transaction.formattedAmount}
                </div>
                <button class="btn-danger" data-id="${transaction.id}">×</button>
            `;
            
            // Add delete functionality
            const deleteBtn = transactionElement.querySelector('button');
            deleteBtn.addEventListener('click', () => this.deleteTransaction(transaction.id));
            
            transactionsList.appendChild(transactionElement);
        });
    }
    
    /**
     * Menghapus transaksi tertentu
     * @param {string} id - ID transaksi yang akan dihapus
     */
    deleteTransaction(id) {
        this.transactions = this.transactions.filter(t => t.id !== id);
        this.saveToLocalStorage();
        this.renderTransactions();
        this.updateSaldo();
        this.updateBudgetDisplay();
        this.renderChart();
    }
    
    /**
     * Render grafik keuangan
     */
    renderChart() {
        const ctx = document.getElementById('financeChart').getContext('2d');
        
        // Prepare data for the chart
        const monthlyData = this.getMonthlyData();
        
        // If chart exists, destroy it first
        if (this.chart) {
            this.chart.destroy();
        }
        
        // Create new chart
        this.chart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: monthlyData.map(d => d.month),
                datasets: [
                    {
                        label: 'Pemasukan',
                        backgroundColor: '#4cc9f0',
                        data: monthlyData.map(d => d.income)
                    },
                    {
                        label: 'Pengeluaran',
                        backgroundColor: '#f72585',
                        data: monthlyData.map(d => d.expense)
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: (value) => {
                                return 'Rp ' + new Intl.NumberFormat('id').format(value);
                            }
                        }
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: (context) => {
                                let label = context.dataset.label || '';
                                if (label) {
                                    label += ': ';
                                }
                                if (context.parsed.y !== null) {
                                    label += new Intl.NumberFormat('id-ID', {
                                        style: 'currency',
                                        currency: 'IDR',
                                        minimumFractionDigits: 0
                                    }).format(context.parsed.y);
                                }
                                return label;
                            }
                        }
                    }
                }
            }
        });
    }
    
    /**
     * Mendapatkan data bulanan untuk chart
     * @return {Array} Array data bulanan
     */
    getMonthlyData() {
        const months = {};
        
        // Initialize current month and maybe previous month
        const now = new Date();
        const currentMonthKey = `${now.getFullYear()}-${now.getMonth() + 1}`;
        months[currentMonthKey] = { income: 0, expense: 0, month: this.getMonthName(now.getMonth()) };
        
        // Process each transaction
        this.transactions.forEach(transaction => {
            const date = new Date(transaction.date);
            const monthKey = `${date.getFullYear()}-${date.getMonth() + 1}`;
            
            // Initialize month if not exists
            if (!months[monthKey]) {
                months[monthKey] = {
                    income: 0,
                    expense: 0,
                    month: this.getMonthName(date.getMonth())
                };
            }
            
            // Add amount to appropriate type
            if (transaction.type === 'income') {
                months[monthKey].income += transaction.amount;
            } else {
                months[monthKey].expense += transaction.amount;
            }
        });
        
        // Convert to array and sort by month
        return Object.values(months).slice(-3); // Show only last 3 months
    }
    
    /**
     * Mendapatkan nama bulan dari indeks
     * @param {number} monthIndex - Indeks bulan (0-11)
     * @return {string} Nama bulan
     */
    getMonthName(monthIndex) {
        const monthNames = [
            'Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun',
            'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'
        ];
        return monthNames[monthIndex];
    }
    
    /**
     * Memperbarui tampilan budget
     */
    updateBudgetDisplay() {
        const budgetContainer = document.getElementById('budgetContainer');
        const budgetBar = document.getElementById('budgetBar');
        const budgetUsed = document.getElementById('budgetUsed');
        const budgetTotal = document.getElementById('budgetTotal');
        
        if (this.budget <= 0) {
            budgetContainer.style.display = 'none';
            return;
        }
        
        budgetContainer.style.display = 'block';
        
        // Calculate current month expenses
        const now = new Date();
        const currentMonthExpenses = this.transactions
            .filter(t => {
                const transDate = new Date(t.date);
                return t.type === 'expense' && 
                       transDate.getMonth() === now.getMonth() &&
                       transDate.getFullYear() === now.getFullYear();
            })
            .reduce((sum, t) => sum + t.amount, 0);
        
        // Update progress bar
        const percentage = Math.min((currentMonthExpenses / this.budget) * 100, 100);
        budgetBar.style.width = `${percentage}%`;
        
        // Change color based on percentage
        if (percentage >= 90) {
            budgetBar.className = 'budget-bar danger';
        } else if (percentage >= 75) {
            budgetBar.className = 'budget-bar warning';
        } else {
            budgetBar.className = 'budget-bar';
        }
        
        // Update text
        budgetUsed.textContent = new Intl.NumberFormat('id-ID', { 
            style: 'currency', 
            currency: 'IDR',
            minimumFractionDigits: 0,
            maximumFractionDigits: 0
        }).format(currentMonthExpenses);
        
        budgetTotal.textContent = 'dari ' + new Intl.NumberFormat('id-ID', { 
            style: 'currency', 
            currency: 'IDR',
            minimumFractionDigits: 0,
            maximumFractionDigits: 0
        }).format(this.budget);
    }
}