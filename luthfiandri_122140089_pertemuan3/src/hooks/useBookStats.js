import { useMemo } from "react";
import { useBooks } from "../context/BookContext";

export default function useBookStats() {
  const { books } = useBooks();

  const stats = useMemo(() => {
    const total = books.length;
    const owned = books.filter((b) => b.status === "milik").length;
    const reading = books.filter((b) => b.status === "baca").length;
    const toBuy = books.filter((b) => b.status === "beli").length;

    return { total, owned, reading, toBuy };
  }, [books]);

  return stats;
}
