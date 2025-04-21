import React, { useContext } from 'react';
import BookContext from '../../context/BookContext';
import './BookFilter.css';

function BookFilter() {
  const { filter, setFilter, searchTerm, setSearchTerm } = useContext(BookContext);

  const handleFilterChange = (e) => {
    setFilter(e.target.value);
  };

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  return (
    <div className="book-filter">
      <div className="search-container">
        <input
          type="text"
          placeholder="Cari judul atau penulis..."
          value={searchTerm}
          onChange={handleSearchChange}
          className="search-input"
        />
      </div>
      
      <div className="filter-container">
        <label htmlFor="status-filter">Filter berdasarkan status:</label>
        <select
          id="status-filter"
          value={filter}
          onChange={handleFilterChange}
          className="filter-select"
        >
          <option value="all">Semua Buku</option>
          <option value="milik">Dimiliki</option>
          <option value="baca">Sedang Dibaca</option>
          <option value="beli">Ingin Dibeli</option>
        </select>
      </div>
    </div>
  );
}

export default BookFilter;