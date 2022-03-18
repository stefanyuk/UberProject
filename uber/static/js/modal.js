$(document).ready(function (){
    showModal()
    closeModal()
});

function showModal (){
    $('[data-modal=consultation]').on('click', function (){
       $('.overlay').fadeIn('slow')
    });
}

function closeModal(){
    $('.modal__close').on('click', function (){
       $('.overlay').fadeOut()
    });
}
