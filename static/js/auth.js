// function authUser() {
//     $('auth-form').submit(function (e) {
//         var $form = $(this);
//         $.ajax({
//             url: $form.attr('action'),
//             type: $form.attr('method'),
//             data: $form.serialize()
//         }).done(function () {
//             console.log('success');
//         }).fail(function () {
//             console.log('fail');
//         });
//         e.preventDefault();
//     });
// }