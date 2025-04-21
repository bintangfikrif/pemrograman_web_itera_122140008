import React, { useContext, useState } from 'react';
import BookContext from '../../context/BookContext';
import BookForm from '../BookForm/BookForm';
import './BookList.css';

function BookList() {
  const { filteredBooks, deleteBook } = useContext(BookContext);
  const [editingBook, setEditingBook] = useState(null);

  const handleEdit = (book) => {
    setEditingBook(book);
  };

  const handleCancelEdit = () => {
    setEditingBook(null);
  };

  const statusLabels = {
    milik: 'Dimiliki',
    baca: 'Sedang Dibaca',
    beli: 'Ingin Dibeli'
  };

  if (editingBook) {
    return <BookForm bookToEdit={editingBook} onCancel={handleCancelEdit} />;
  }

  if (filteredBooks.length === 0) {
    return (
      <div className="book-list-empty">
        <p>Tidak ada buku yang ditemukan.</p>
      </div>
    );
  }

  return (
    <div className="book-list">
      {filteredBooks.map(book => (
        <div key={book.id} className={`book-card status-${book.status}`}>
          <div className="book-content">
            <h3 className="book-title">{book.title}</h3>
            <p className="book-author">Penulis: {book.author}</p>
            <p className="book-status">Status: {statusLabels[book.status]}</p>
            {book.notes && <p className="book-notes">Catatan: {book.notes}</p>}
          </div>
          <div className="book-actions">
            <button 
              className="btn-edit" 
              onClick={() => handleEdit(book)}
              aria-label="Edit buku"
            >
              Edit
            </button>
            <button 
              className="btn-delete" 
              onClick={() => deleteBook(book.id)}
              aria-label="Hapus buku"
            >
              Hapus
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}

export default BookList;