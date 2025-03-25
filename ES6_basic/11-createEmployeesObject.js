export default function createEmployeesObject(departmentName = String, employees = Array) {
  return {
    [departmentName]: employees,
  };
}
