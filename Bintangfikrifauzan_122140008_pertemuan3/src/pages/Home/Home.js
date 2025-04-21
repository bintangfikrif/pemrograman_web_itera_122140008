import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import BookForm from '../../components/BookForm/BookForm';
import BookList from '../../components/BookList/BookList';
import BookFilter from '../../components/BookFilter/BookFilter';
import './Home.css';

function Home() {
  const [showAddForm, setShowAddForm] = useState(false);

  return (
    <div className="home-page">
      <nav className="app-nav">
        <Link to="/" className="nav-link active">Daftar Buku</Link>
        <Link to="/stats" className="nav-link">Statistik</Link>
      </nav>
      
      <div className="page-content">
        <div className="page-header">
          <h2>Koleksi Buku Saya</h2>
          <button 
            className="btn-add"
            onClick={() => setShowAddForm(!showAddForm)}
          >
            {showAddForm ? 'Tutup Form' : 'Tambah Buku'}
          </button>
        </div>
        
        {showAddForm && (
          <BookForm onCancel={() => setShowAddForm(false)} />
        )}
        
        <BookFilter />
        <BookList />
      </div>
    </div>
  );
}

export default Home;