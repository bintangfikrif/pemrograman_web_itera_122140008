import React from 'react';
import { Link } from 'react-router-dom';
import useBookStats from '../../hooks/useBookStats';
import './Stats.css';

function Stats() {
  const stats = useBookStats();

  return (
    <div className="stats-page">
      <nav className="app-nav">
        <Link to="/" className="nav-link">Daftar Buku</Link>
        <Link to="/stats" className="nav-link active">Statistik</Link>
      </nav>
      
      <div className="page-content">
        <h2>Statistik Koleksi Buku</h2>
        
        <div className="stats-grid">
          <div className="stat-card">
            <h3>Total Buku</h3>
            <p className="stat-number">{stats.total}</p>
          </div>
          
          <div className="stat-card">
            <h3>Buku Dimiliki</h3>
            <p className="stat-number">{stats.owned}</p>
          </div>
          
          <div className="stat-card">
            <h3>Sedang Dibaca</h3>
            <p className="stat-number">{stats.reading}</p>
          </div>
          
          <div className="stat-card">
            <h3>Wishlist</h3>
            <p className="stat-number">{stats.wishlist}</p>
          </div>
        </div>
        
        <div className="recent-books">
          <h3>Buku Terbaru Ditambahkan</h3>
          
          {stats.recentBooks.length > 0 ? (
            <ul className="recent-list">
              {stats.recentBooks.map(book => (
                <li key={book.id} className="recent-item">
                  <strong>{book.title}</strong> oleh {book.author}
                </li>
              ))}
            </ul>
          ) : (
            <p>Belum ada buku yang ditambahkan.</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default Stats;