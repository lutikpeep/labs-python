var groupmates = [
    { 
        "name": "Марина", 
        "surname": "Иванова", 
        "group": "ПИС-1", // Добавили группу
        "marks": [3, 4, 5] 
    },
    { 
        "name": "Пётр", 
        "surname": "Сидоров", 
        "group": "ПИС-2", 
        "marks": [3, 3, 5] 
    },
    { 
        "name": "Вася", 
        "surname": "Колобков", 
        "group": "ПИС-1", 
        "marks": [5, 4, 4] 
    }
];

var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length) str = str + ' ';
    return str;
};

var printStudents = function(students) {
    console.log(rpad("Имя", 15), rpad("Фамилия", 15), rpad("Группа", 8), rpad("Оценки", 20));
    for (var i = 0; i < students.length; i++) {
        console.log(rpad(students[i]['name'], 15), rpad(students[i]['surname'], 15), rpad(students[i]['group'], 8), rpad(students[i]['marks'], 20));
    }
    console.log('\n');
};

// Фильтр по группе
var filterByGroup = function(group) {
    var filtered = groupmates.filter(function(s) { return s.group === group; });
    printStudents(filtered);
};

// Фильтр по среднему баллу
var filterByAverage = function(minAvg) {
    var filtered = groupmates.filter(function(s) {
        var sum = 0;
        for (var i = 0; i < s.marks.length; i++) sum += s.marks[i];
        var avg = sum / s.marks.length;
        return avg > minAvg;
    });
    printStudents(filtered);
};

// Выводим всех студентов
printStudents(groupmates);

var selectedGroup = prompt("Введите группу для фильтрации:");
if (selectedGroup) {
    filterByGroup(selectedGroup);
}

var minAverage = parseFloat(prompt("Введите минимальный средний балл:"));
if (!isNaN(minAverage)) {
    filterByAverage(minAverage);
}