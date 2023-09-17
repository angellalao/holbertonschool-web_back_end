export default function appendToEachArrayValue(array, appendString) {
  const list = [];
  for (const value of array) {
    const idx = appendString + value;
    list.push(idx);
  }
  return list;
}
