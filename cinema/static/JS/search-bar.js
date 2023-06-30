function OpenClose_SearchBar(search_bar) {
    bar = document.getElementById('search_bar');
    bar.classList.toggle('hide');
    bar.classList.toggle('show');
}

function ShowHide_Menu(menu_without_search) {
    menu = document.getElementById('menu_without_search');
    menu.classList.toggle('show_menu');
    menu.classList.toggle('hide_menu');
}
