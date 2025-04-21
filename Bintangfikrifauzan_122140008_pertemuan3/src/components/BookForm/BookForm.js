import React, { useState, useContext, useEffect } from 'react';
import PropTypes from 'prop-types';
import BookContext from '../../context/BookContext';
import './BookForm.css';

function BookForm({ bookToEdit, onCancel }) {
  const { addBook, editBook } = useContext(BookContext);
  const [formData, setFormData] = useState({
    title: '',
    author: '',
    status: 'milik',
    notes: ''
  });
  const [errors, setErrors] = useState({});

  // If editing a book, populate form with book data
  useEffect(() => {
    if (bookToEdit) {
      setFormData({
        title: bookToEdit.title || '',
        author: bookToEdit.author || '',
        status: bookToEdit.status || 'milik',
        notes: bookToEdit.notes || ''
      });
    }
  }, [bookToEdit]);

  const validateForm = () => {
    const newErrors = {};
    if (!formData.title.trim()) newErrors.title = 'Judul buku wajib diisi';
    if (!formData.author.trim()) newErrors.author = 'Penulis buku wajib diisi';
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    
    // Clear error when user starts typing
    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: null
      }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!validateForm()) return;
    
    if (bookToEdit) {
      editBook(bookToEdit.id, formData);
    } else {
      addBook(formData);
    }
    
    // Reset form
    setFormData({
      title: '',
      author: '',
      status: 'milik',
      notes: ''
    });
    
    if (onCancel) onCancel();
  };

  return (
    <div className="book-form-container">
      <h2>{bookToEdit ? 'Edit Buku' : 'Tambah Buku Baru'}</h2>
      <form onSubmit={handleSubmit} className="book-form">
        <div className="form-group">
          <label htmlFor="title">Judul Buku:</label>
          <input
            type="text"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleChange}
            className={errors.title ? 'error' : ''}
          />
          {errors.title && <span className="error-text">{errors.title}</span>}
        </div>
        
        <div className="form-group">
          <label htmlFor="author">Penulis:</label>
          <input
            type="text"
            id="author"
            name="author"
            value={formData.author}
            onChange={handleChange}
            className={errors.author ? 'error' : ''}
          />
          {errors.author && <span className="error-text">{errors.author}</span>}
        </div>
        
        <div className="form-group">
          <label htmlFor="status">Status:</label>
          <select
            id="status"
            name="status"
            value={formData.status}
            onChange={handleChange}
          >
            <option value="milik">Dimiliki</option>
            <option value="baca">Sedang Dibaca</option>
            <option value="beli">Ingin Dibeli</option>
          </select>
        </div>
        
        <div className="form-group">
          <label htmlFor="notes">Catatan (opsional):</label>
          <textarea
            id="notes"
            name="notes"
            value={formData.notes}
            onChange={handleChange}
            rows="3"
          />
        </div>
        
        <div className="form-actions">
          <button type="submit" className="btn-submit">
            {bookToEdit ? 'Simpan Perubahan' : 'Tambah Buku'}
          </button>
          {onCancel && (
            <button type="button" className="btn-cancel" onClick={onCancel}>
              Batal
            </button>
          )}
        </div>
      </form>
    </div>
  );
}

BookForm.propTypes = {
  bookToEdit: PropTypes.shape({
    id: PropTypes.number,
    title: PropTypes.string,
    author: PropTypes.string,
    status: PropTypes.string,
    notes: PropTypes.string
  }),
  onCancel: PropTypes.func
};

export default BookForm;