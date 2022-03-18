window.addEventListener('DOMContentLoaded', () => {
    const menu = document.querySelector('.menu'),
    menuItem = document.querySelectorAll('.menu_item'),
    hamburger = document.querySelector('.hamburger');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('hamburger_active');
        menu.classList.toggle('menu_active');
    });

    menuItem.forEach(item => {
        item.addEventListener('click', () => {
            hamburger.classList.toggle('hamburger_active');
            menu.classList.toggle('menu_active');
        })
    })
})

$(document).ready(function (){
    sendFormDataOnSubmit()
})
function sendFormDataOnSubmit (){
    $(document).on('click', '.button', function () {
        const formData = gatherFormData()
        req = $.ajax({
            url: '/save-lead-data',
            type: 'POST',
            data: formData
        })

        req.done(function (data){
            if (typeof data === 'string'){
                $('.feed-form').html(data)
            } else {
                $('.overlay').hide()
                clearFormInput()
                $('.thanks__outer').fadeIn()
                setTimeout(() => {
                    $('.thanks__outer').fadeOut()
                }, 2500)
            }
        })
    })
}

function gatherFormData (){
    return {
        name: document.querySelector('.form__input.name').value,
        email: document.querySelector('.form__input.email').value,
        phone_number: document.querySelector('.form__input.phone').value,
        csrf_token: document.querySelector('#csrf_token').value,
        submit: true
    }
}

function clearFormInput () {
    document.querySelector('.form__input.name').value = ''
    document.querySelector('.form__input.email').value = ''
    document.querySelector('.form__input.phone').value = ''
}
