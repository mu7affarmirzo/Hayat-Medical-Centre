'use strict'
const togglePassword = document.getElementById('togglePassword');
const passwordInput = document.getElementById('floatingPassword');
const loginButton = document.getElementById('loginButton');

if(togglePassword){
togglePassword.addEventListener('click', function () {
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
});
}



// loginButton.addEventListener('click', function () {
//     window.location.href = '/Main/index.html';
// });

const checkItem = document.querySelectorAll('#check_item')
const checkItemId = document.querySelectorAll('#check_id')
const checkItemIdSel = document.querySelector('#check_id-selected')

checkItem.onclick = () => {
    checkItemIdSel.textContent = checkItemId.textContent;
    console.log(checkItem)
}