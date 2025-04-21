import { useContext, useMemo } from 'react';
import BookContext from '../context/BookContext';

function useBookStats() {
  const { books } = useContext(BookContext);

  const stats = useMemo(() => {
    const total = books.length;
    const owned = books.filter(book => book.status === 'milik').length;
    const reading = books.filter(book => book.status === 'baca').length;
    const wishlist = books.filter(book => book.status === 'beli').length;

    // Calculate most recent additions
    const recentBooks = [...books]
      .sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt))
      .slice(0, 5);

    return {
      total,
      owned,
      reading,
      wishlist,
      recentBooks
    };
  }, [books]);

  return stats;
}

export default useBookStats;