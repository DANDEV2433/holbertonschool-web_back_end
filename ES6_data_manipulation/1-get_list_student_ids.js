import getListStudents from './0-get_list_students';

export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  return getListStudents().map((student) => student.id);
}
