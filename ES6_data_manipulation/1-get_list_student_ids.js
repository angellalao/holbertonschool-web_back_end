export default function getListStudentIds(arrayObjs) {
  if (!Array.isArray(arrayObjs)) {
    return [];
  }
  const newArray = arrayObjs.map((x) => x.id);
  return newArray;
}
