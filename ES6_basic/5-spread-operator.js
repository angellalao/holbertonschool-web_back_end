export default function concatArrays(array1, array2, string) {
  const array3 = [...string];
  array1 = [...array1, ...array2, ...array3];
  return array1;
}
