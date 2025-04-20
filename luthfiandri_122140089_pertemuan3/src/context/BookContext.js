import { createContext, useContext, useEffect, useState } from "react";
import PropTypes from "prop-types";
import useLocalStorage from "../hooks/useLocalStorage";

const BookContext = createContext();

export const BookProvider = ({ children }) => {
  const [storedBooks, setStoredBooks] = useLocalStorage("books", []);
  const [books, setBooks] = useState(storedBooks);

  useEffect(() => {
    setStoredBooks(books);
  }, [books]);

  const addBook = (book) => {
    setBooks((prev) => [...prev, { ...book, id: Date.now() }]);
  };

  const editBook = (updatedBook) => {
    setBooks((prev) =>
      prev.map((book) => (book.id === updatedBook.id ? updatedBook : book))
    );
  };

  const deleteBook = (id) => {
    setBooks((prev) => prev.filter((book) => book.id !== id));
  };

  return (
    <BookContext.Provider value={{ books, addBook, editBook, deleteBook }}>
      {children}
    </BookContext.Provider>
  );
};

BookProvider.propTypes = {
  children: PropTypes.node.isRequired,
};

export const useBooks = () => useContext(BookContext);
