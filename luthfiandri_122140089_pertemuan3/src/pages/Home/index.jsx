import { useState } from "react";
import BookForm from "../../components/BookForm/BookForm";
import BookList from "../../components/BookList/BookList";
import BookFilter from "../../components/BookFilter/BookFilter";
import { Link } from "react-router-dom";
import './Home.css';

const Home = () => {
  const [filter, setFilter] = useState("semua");
  const [search, setSearch] = useState("");

  return (
    <div>
      <header>
        <h1>Manajemen Buku Pribadi</h1>
        <nav>
          <Link to="/stats">Lihat Statistik</Link>
        </nav>
      </header>

      <BookForm />
      <BookFilter
        filter={filter}
        setFilter={setFilter}
        search={search}
        setSearch={setSearch}
      />
      <BookList filter={filter} search={search} />
    </div>
  );
};

export default Home;
