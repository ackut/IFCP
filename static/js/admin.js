// ['#create_user'].forEach((item) => {
//     if (item) {
//         $(item).submit(function (e) {
//             e.preventDefault();
//             var form_data = $(this).serialize();
//             $.ajax({
//                 type: "POST", url: "", data: form_data,
//                 success: function () {
//                     document.querySelector(item).reset();
//                 }
//             });
//         });
//     };
// });