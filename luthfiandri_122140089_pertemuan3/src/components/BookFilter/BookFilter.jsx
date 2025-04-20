import PropTypes from "prop-types";
import "./BookFilter.css";

const BookFilter = ({ filter, setFilter, search, setSearch }) => {
  return (
    <div>
      <input
        type="text"
        placeholder="Cari buku..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <select value={filter} onChange={(e) => setFilter(e.target.value)}>
        <option value="semua">Semua</option>
        <option value="milik">Dimiliki</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="beli">Ingin Dibeli</option>
      </select>
    </div>
  );
};

BookFilter.propTypes = {
  filter: PropTypes.string.isRequired,
  setFilter: PropTypes.func.isRequired,
  search: PropTypes.string.isRequired,
  setSearch: PropTypes.func.isRequired,
};

export default BookFilter;
