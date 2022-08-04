import {make_post, edit_post} from './funcs.js';

document.addEventListener('DOMContentLoaded', () => {
    
    // new post button and enter key listeners
    document.querySelector('#post-button').addEventListener('click', make_post);
    document.querySelector('#new-content').onkeypress = (event) => {
        if (!event.shiftKey) {
            if (event.code === 'Enter') {
                make_post()
            }
        }
    };

    const edit_buttons = document.querySelectorAll('#edit_post');
    edit_buttons.forEach(button => button.addEventListener('click', edit_post));


});