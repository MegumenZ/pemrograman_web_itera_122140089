import { useState } from "react";
import PropTypes from "prop-types";
import { useBooks } from "../../context/BookContext";
import BookForm from "../BookForm/BookForm";
import "./BookList.css";

const BookList = ({ filter, search }) => {
  const { books, deleteBook } = useBooks();
  const [editBook, setEditBook] = useState(null);

  const filteredBooks = books.filter((book) => {
    const matchesStatus = filter === "semua" || book.status === filter;
    const matchesSearch =
      book.title.toLowerCase().includes(search.toLowerCase()) ||
      book.author.toLowerCase().includes(search.toLowerCase());
    return matchesStatus && matchesSearch;
  });

  return (
    <div>
      <h2>Daftar Buku</h2>
      {editBook && (
        <BookForm editData={editBook} onFinish={() => setEditBook(null)} />
      )}
      {filteredBooks.length === 0 ? (
        <p>Tidak ada buku ditemukan.</p>
      ) : (
        <ul>
          {filteredBooks.map((book) => (
            <li key={book.id}>
              <strong>{book.title}</strong> - {book.author} ({book.status})
              <button onClick={() => setEditBook(book)}>Edit</button>
              <button onClick={() => deleteBook(book.id)}>Hapus</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

BookList.propTypes = {
  filter: PropTypes.string.isRequired,
  search: PropTypes.string.isRequired,
};

export default BookList;
