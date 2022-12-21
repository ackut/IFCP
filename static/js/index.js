$(() => {
    var selected_subject = $('#subject');
    var selected_group = $('#group');

    selected_subject.change(() => {
        console.log($("#subject option:selected").val());
    });

    selected_group.change(() => {
        composeTable($("#group option:selected").val());
    });
});


const STUDENTS1 = [
    'Ворошилов Даниил',
    'Зельский Владислав',
    'Васенёв Кирилл',
    'Коневцов Иван',
    'Куценко Андрей',
    'Кривулин Фёдор',
    'Вылегжанин Илья',
    'Федотов Андрей',
    'Райхерт Дмитрий',
    'Алексеев Илья',
    'Касьянов Михаил',
    'Финченко Кирилл',
    'Калайтанов Алексей'
]


const STUDENTS2 = [
    'Студент Студентов',
    'Студент Студентов',
    'Студент Студентов',
    'Студент Студентов',
    'Студент Студентов',
    'Студент Студентов',
    'Студент Студентов',
    'Студент Студентов',
    'Студент Студентов',
    'Студент Студентов',
    'Студент Студентов',
]


function composeTable(asd) {
    var table_box = $('#table-box');
    var table = $('#table');
    
    if (asd == 1) {
        table.remove();
        table_box.append('<table id="table"></table>');
        var table = $('#table');
        STUDENTS1.forEach(student => {
            table.append(`<tr><td>${student}</td></tr>`);
        });
    }

    if (asd == 2) {
        table.remove();
        table_box.append('<table id="table"></table>');
        var table = $('#table');
        STUDENTS2.forEach(student => {
            table.append(`<tr><td>${student}</td></tr>`);
        });
    }

    var tr = Array.from($('tr'));

    tr.forEach(tra => {
        i = 0
        while (i < 30) {
            i += 1
            tra.append('   |   3');
        }
    });
}


function sendAjax(data) {
    $.ajax({
        type: "get",
        url: "",
        data: data,
        dataType: "json",
        contentType: 'application/json',
        success: function (response) {
            ajaxHandler(response);
        }
    });
}


function ajaxHandler(response) {
    console.log(response);
}