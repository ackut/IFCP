
// Запрет перетягивания ссылок и изображений.
['a', 'img'].forEach((item) => {
    const elementList = document.querySelectorAll(item);

    if (elementList) {
        elementList.forEach((item) => {
            item.setAttribute('draggable', 'false');
        });
    };
});