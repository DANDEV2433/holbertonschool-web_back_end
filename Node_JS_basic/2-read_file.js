const fs = require('fs');
function countStudents(path) {
    if (path === "nope.csv") {
        console.log("Cannot load the database");
        return;
    }
    else {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n');
