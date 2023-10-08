export default function cleanSet(set, startString) {
  if (startString === '' || startString === null || typeof (startString) !== 'string') {
    return '';
  }
  const list = [];
  for (const word of set) {
    if (word !== undefined && word.startsWith(startString)) {
      const newString = word.replace(startString, '');
      list.push(newString);
    }
  }
  return list.join('-');
}
