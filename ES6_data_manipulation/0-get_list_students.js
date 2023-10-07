export default function getListStudents() {
  const array = [];
  const Guillaume = { id: 1, firstName: 'Guillaume', location: 'San Francisco' };
  const James = { id: 2, firstName: 'James', location: 'Columbia' };
  const Serena = { id: 5, firstName: 'Serena', location: 'San Francisco' };
  array.push(Guillaume, James, Serena);
  return array;
}
