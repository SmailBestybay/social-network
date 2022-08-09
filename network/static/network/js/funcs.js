export function make_post() {
    document.querySelector('form').submit();
}

export function edit_post(event) {
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
            fetch(`/update_post/${post_div.id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    content: text_area.value
                })
            });
        }
    });

    event.target.replaceWith(save_button);
}

export function like_unlike(event) {
    const liked = event.target.dataset['liked']
    event.target.classList.toggle("fa-thumbs-down");
    if (liked) {
        console.log(liked)
    } 
    else if (liked) {
        console.log(liked)
    }
}