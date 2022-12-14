function tab(but_tab, hidden_block_tab) {
  	/*проверяем на событие нажатия на кнопку которыю вы передаёте в качестве параметра*/
    but_tab.addEventListener("click", function() {
      	/*если у блока с контентом есть класс "hidden_block"*/
        if(hidden_block_tab.classList.contains('hidden_block')) {
          	/*удаляем класс "hidden_block"*/
            hidden_block_tab.classList.remove('hidden_block');
          	/*ставим класс "visible_block"*/
            hidden_block_tab.classList.add('visible_block');
        }
      	/*если у блока с контентом есть класс "visible_block"*/
        else if(hidden_block_tab.classList.contains('visible_block')) {
            hidden_block_tab.classList.remove('visible_block');
            hidden_block_tab.classList.add('hidden_block');
        }
    });
}

/*находим элемент кнопку*/
let download_more = document.querySelector('.container_for_tab .but_for_tab');
/*находим элемент блока со скрытым контентом*/
let hidden_list = document.querySelector('.container_for_tab .tab_content');

/*запускаем функцию и передаём в неё параметры*/
tab(download_more, hidden_list);