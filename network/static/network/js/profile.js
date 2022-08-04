import {edit_post} from './funcs.js';

document.addEventListener('DOMContentLoaded', () => {
    
    const edit_buttons = document.querySelectorAll('#edit_post');
    edit_buttons.forEach(button => button.addEventListener('click', edit_post));

});