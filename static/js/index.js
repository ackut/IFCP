const STUDENTS = [
    'Зельский Владислав',
    'Ворошилов Даниил',
    'Финченко Кирилл',
    'Цатуров Артур',
    'Ходырев Николай',
    'Кублашвили Гиоргий',
    'Васенёв Кирилл',
    'Вылегжанин Илья',
    'Куценко Андрей',
    'Алексеев Илья',
    'Махмудов Ренад',
    'Голосной Максим',
    'Касьянов Михаил',
    'Коневцов Иван',
    'Федотов Андрей',
    'Орлов Павел',
    'Райхерт Дмитрий',
    'Умаров Азал',
    'Аспандиев Ибрагим',
    'Дранов Артём',
    'Кривулин Фёдор',
]


function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}


$(() => {
    var table = $('#table');
    var date = $('#date');

    ib = 0;
    while (31 > ib) {
        ib += 1
        date.append(`<td class="grey">${ib}</td>`);
    }

    i = 0;
    STUDENTS.forEach(student => {
        i += 1
        table.append(`<tr id="${i}"><td>${i}</td></tr>`);
        var tr = $(`#${i}`);
        tr.append(`<td class="grey std" id="student_${i}">${student}</td>`);

        ia = 0
        while (31 > ia) {
            ia += 1
            tr.append(`<td id="${i}"></td>`);
        }
    });
});