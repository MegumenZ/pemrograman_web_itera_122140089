import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { BookProvider } from "./context/BookContext";
import Home from "./pages/Home";
import Stats from "./pages/Stats";

export default function App() {
  return (
    <BookProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/stats" element={<Stats />} />
        </Routes>
      </Router>
    </BookProvider>
  );
}
