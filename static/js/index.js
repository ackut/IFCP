$(() => {
    var selected_subject = $('#subject');
    var selected_group = $('#group');

    selected_subject.change(() => {
        console.log(selected_subject.options[selected_subject.selectedIndex]);
    });
});