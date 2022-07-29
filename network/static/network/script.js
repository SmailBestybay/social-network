document.addEventListener('DOMContentLoaded', () => {
    // new post button
    document.querySelector('#post-button').addEventListener('click', make_post);
    document.querySelector('#new-content').onkeypress = (event) => {
        if (!event.shiftKey) {
            if (event.code === 'Enter') {
                make_post()
            }
        }
        
    };

    function make_post() {
        const post_content = document.querySelector('#new-content');
        fetch('/make_post', {
            method: 'POST',
            body: JSON.stringify({
                content: post_content.value
            })
        }).then(response => response.json())
        .then(result => {
            console.log(result);
        })
        post_content.value = "";
        
        return false;
    };
});
