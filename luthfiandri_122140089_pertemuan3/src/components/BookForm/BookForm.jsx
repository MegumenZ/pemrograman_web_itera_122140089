import { useState, useEffect } from "react";
import PropTypes from "prop-types";
import { useBooks } from "../../context/BookContext";
import "./BookForm.css";

const BookForm = ({ editData, onFinish }) => {
  const { addBook, editBook } = useBooks();

  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [status, setStatus] = useState("milik");
  const [error, setError] = useState("");

  useEffect(() => {
    if (editData) {
      setTitle(editData.title);
      setAuthor(editData.author);
      setStatus(editData.status);
    }
  }, [editData]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title.trim() || !author.trim()) {
      setError("Judul dan penulis tidak boleh kosong");
      return;
    }

    const bookData = {
      id: editData?.id,
      title,
      author,
      status,
    };

    editData ? editBook(bookData) : addBook(bookData);
    setTitle("");
    setAuthor("");
    setStatus("milik");
    setError("");
    onFinish?.();
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>{editData ? "Edit Buku" : "Tambah Buku"}</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <input
        type="text"
        placeholder="Judul"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <input
        type="text"
        placeholder="Penulis"
        value={author}
        onChange={(e) => setAuthor(e.target.value)}
      />
      <select value={status} onChange={(e) => setStatus(e.target.value)}>
        <option value="milik">Dimiliki</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="beli">Ingin Dibeli</option>
      </select>
      <button type="submit">{editData ? "Simpan" : "Tambah"}</button>
    </form>
  );
};

BookForm.propTypes = {
  editData: PropTypes.object,
  onFinish: PropTypes.func,
};

export default BookForm;
