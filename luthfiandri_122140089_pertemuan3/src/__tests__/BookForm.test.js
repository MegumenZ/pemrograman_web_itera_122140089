import { render, screen, fireEvent } from "@testing-library/react";
import BookForm from "../components/BookForm/BookForm";
import { BookProvider } from "../context/BookContext";

const setup = () => {
  render(
    <BookProvider>
      <BookForm />
    </BookProvider>
  );
};

test("should render form and add book", () => {
  setup();

  const titleInput = screen.getByPlaceholderText("Judul");
  const authorInput = screen.getByPlaceholderText("Penulis");
  const submitButton = screen.getByText("Tambah");

  fireEvent.change(titleInput, { target: { value: "React Basics" } });
  fireEvent.change(authorInput, { target: { value: "John Doe" } });

  fireEvent.click(submitButton);

  expect(titleInput.value).toBe("");
  expect(authorInput.value).toBe("");
});
