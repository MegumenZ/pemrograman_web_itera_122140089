import { Link } from "react-router-dom";
import useBookStats from "../../hooks/useBookStats";
import "./Stats.css";

const Stats = () => {
  const { total, owned, reading, toBuy } = useBookStats();

  return (
    <div>
      <header>
        <h1>Statistik Buku</h1>
        <nav>
          <Link to="/">Kembali ke Beranda</Link>
        </nav>
      </header>

      <ul>
        <li>Total Buku: {total}</li>
        <li>Dimiliki: {owned}</li>
        <li>Sedang Dibaca: {reading}</li>
        <li>Ingin Dibeli: {toBuy}</li>
      </ul>
    </div>
  );
};

export default Stats;
