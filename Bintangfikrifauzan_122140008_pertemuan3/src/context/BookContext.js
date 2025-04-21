import React, { createContext, useState, useEffect } from 'react';
import useLocalStorage from '../hooks/useLocalStorage';

const BookContext = createContext();

export function BookProvider({ children }) {
  const [books, setBooks] = useLocalStorage('books', []);
  const [filteredBooks, setFilteredBooks] = useState([]);
  const [filter, setFilter] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');

  // Add a new book
  const addBook = (book) => {
    const newBook = {
      ...book,
      id: Date.now(),
      createdAt: new Date().toISOString()
    };
    setBooks([...books, newBook]);
  };

  // Edit a book
  const editBook = (id, updatedBook) => {
    setBooks(books.map(book => book.id === id ? { ...book, ...updatedBook } : book));
  };

  // Delete a book
  const deleteBook = (id) => {
    setBooks(books.filter(book => book.id !== id));
  };

  // Filter and search books
  useEffect(() => {
    let result = [...books];

    // Apply status filter
    if (filter !== 'all') {
      result = result.filter(book => book.status === filter);
    }

    // Apply search term
    if (searchTerm.trim() !== '') {
      const term = searchTerm.toLowerCase();
      result = result.filter(book => 
        book.title.toLowerCase().includes(term) ||
        book.author.toLowerCase().includes(term)
      );
    }

    setFilteredBooks(result);
  }, [books, filter, searchTerm]);

  return (
    <BookContext.Provider 
      value={{
        books,
        filteredBooks,
        filter,
        searchTerm,
        addBook,
        editBook,
        deleteBook,
        setFilter,
        setSearchTerm
      }}
    >
      {children}
    </BookContext.Provider>
  );
}

export default BookContext;