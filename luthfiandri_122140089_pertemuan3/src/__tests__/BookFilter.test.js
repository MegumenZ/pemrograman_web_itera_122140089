import { render, screen, fireEvent } from "@testing-library/react";
import BookFilter from "../components/BookFilter/BookFilter";

test("should change filter value", () => {
  const setFilter = jest.fn();
  const setSearch = jest.fn();

  render(
    <BookFilter
      filter="semua"
      setFilter={setFilter}
      search=""
      setSearch={setSearch}
    />
  );

  // Simulate selecting a filter
  const filterSelect = screen.getByRole("combobox");
  fireEvent.change(filterSelect, { target: { value: "baca" } });

  expect(setFilter).toHaveBeenCalledWith("baca");
});

test("should update search value", () => {
  const setFilter = jest.fn();
  const setSearch = jest.fn();

  render(
    <BookFilter
      filter="semua"
      setFilter={setFilter}
      search=""
      setSearch={setSearch}
    />
  );

  const searchInput = screen.getByPlaceholderText("Cari buku...");
  fireEvent.change(searchInput, { target: { value: "React" } });

  expect(setSearch).toHaveBeenCalledWith("React");
});
