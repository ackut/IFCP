const STUDENTS = [
    'Zельский VладислаV',
    'VорошилоV Даниил',
    'Финченко Кирилл',
    'ЦатуроV Артур',
    'ХодыреV Николай',
    'КублашVили Гиоргий',
    'VасенёV Кирилл',
    'Vылегжанин Илья',
    'Куценко Андрей',
    'АлексееV Илья',
    'МахмудоV Ренад',
    'Голосной Максим',
    'КасьяноV Михаил',
    'КонеVцоV ИVан',
    'ФедотоV Андрей',
    'ОрлоV ПаVел',
    'Райхерт Дмитрий',
    'УмароV АZал',
    'АспандиеV Ибрагим',
    'ДраноV Артём',
    'КриVулин Фёдор',
]


function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}


$(() => {
    var table = $('#table');
    var date = $('#date');

    ib = 0;
    while (30 > ib) {
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
        while (30 > ia) {
            ia += 1
            tr.append(`<td id="${i}"></td>`);
        }
    });
});