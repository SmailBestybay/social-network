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

function make_post() {
    document.querySelector('form').submit();
}

function edit_post(event) {
    const post_div = event.target.parentElement;
    const content = post_div.querySelector('#content');
    const text_area = document.createElement('textarea');
    text_area.innerHTML = content.innerHTML;
    content.innerHTML = '';
    content.append(text_area);

    const save_button = document.createElement('button');
    save_button.setAttribute('class' , 'btn btn-outline-primary mb-2')
    save_button.innerHTML = 'Save';
    const edit_button = event.target;

    save_button.addEventListener('click', (event) => {

        if (!text_area.value) {
            alert('Post must not be empty')
        } else {
            content.innerHTML = text_area.value;
            text_area.remove();
            save_button.replaceWith(edit_button);
            fetch(`update_post/${post_div.id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    content: text_area.value
                })
            });
        }
    });

    event.target.replaceWith(save_button);

}
