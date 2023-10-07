export default function getStudentsByLocation(students, city) {
  const newStudents = students.filter((student) => student.location === city);
  return newStudents
}