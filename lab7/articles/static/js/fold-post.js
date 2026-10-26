document.addEventListener("DOMContentLoaded", function() {
    var foldBtns = document.getElementsByClassName("fold-button");
    for (var i = 0; i < foldBtns.length; i++) {
        foldBtns[i].addEventListener("click", function(event) {
            // Используем currentTarget для надежности
            var post = event.currentTarget.closest('.one-post');
            post.classList.toggle('folded');
            
            if (post.classList.contains('folded')) {
                event.currentTarget.innerHTML = "развернуть";
            } else {
                event.currentTarget.innerHTML = "свернуть";
            }
        });
    }
});