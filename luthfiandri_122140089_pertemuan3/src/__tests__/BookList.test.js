import { render, screen, fireEvent } from "@testing-library/react";
import BookList from "../components/BookList/BookList";
import { BookProvider } from "../context/BookContext";

const books = [
  { id: 1, title: "React Basics", author: "John Doe", status: "milik" },
  { id: 2, title: "Advanced React", author: "Jane Doe", status: "baca" },
];

const setup = (filter = "semua") => {
  render(
    <BookProvider>
      <BookList filter={filter} search="" />
    </BookProvider>
  );
};

test("should render book list and delete book", () => {
  setup();

  // Check if books are rendered
  expect(screen.getByText("React Basics")).toBeInTheDocument();
  expect(screen.getByText("Advanced React")).toBeInTheDocument();

  // Simulate delete
  const deleteButton = screen.getAllByText("Hapus")[0];
  fireEvent.click(deleteButton);

  // Check if the book was removed (for simplicity, we assume delete removes from screen)
  expect(screen.queryByText("React Basics")).not.toBeInTheDocument();
});
