document.addEventListener("DOMContentLoaded", function() {
    var foldBtns = document.getElementsByClassName("fold-button");
    for (var i = 0; i < foldBtns.length; i++) {
        foldBtns[i].addEventListener("click", function(event) {
            // Находим родительский блок статьи
            var post = event.target.closest('.one-post');
            // Переключаем класс folded
            post.classList.toggle('folded');
            
            // Меняем текст на кнопке
            if (post.classList.contains('folded')) {
                event.target.innerHTML = "развернуть";
            } else {
                event.target.innerHTML = "свернуть";
            }
        });
    }
});