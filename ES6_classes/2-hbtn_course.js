export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('name must be a String.');
    }
    if (typeof length !== 'number') {
      throw new TypeError('length must be a Number.');
    }
    if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
      throw new TypeError('students must be an array of Strings.');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(newname) {
    if (typeof newname !== 'string') {
      throw new TypeError('name must be a String.');
    }
    this._name = newname;
  }

  get length() {
    return this._length;
  }

  set length(newlength) {
    if (typeof newlength !== 'number') {
      throw new TypeError('length must be a Number.');
    }
    this._length = newlength;
  }

  get students() {
    return this._students;
  }

  set students(newstudent) {
    if (!Array.isArray(newstudent) || !newstudent.every((student) => typeof student === 'string')) {
      throw new TypeError('students must be an array of Strings.');
    }
    this._students = newstudent;
  }
}
