export default function getStudentIdsSum(listStudents) {
  const sumIds = listStudents.reduce((accumulator, current) => accumulator + current.id, 0);
  return sumIds;
}
