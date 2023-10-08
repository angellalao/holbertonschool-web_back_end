export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const newStudentList = studentList.filter((student) => student.location === city);
  // console.log(newStudentList);
  const studentGradesList = newStudentList.map((x) => {
    const matchingGrade = newGrades.find((grade) => grade.studentId === x.id);
    // console.log(matchingGrade);
    if (matchingGrade) {
      return { ...x, grade: matchingGrade.grade };
    }
    return { ...x, grade: 'N/A' };
  });
  return studentGradesList;
}
