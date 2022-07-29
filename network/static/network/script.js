document.addEventListener('DOMContentLoaded', () => {
    // new post button
    document.querySelector('#post-button').addEventListener('click', make_post);
    document.querySelector('#new-content').onkeypress = (event) => {
        const keyCode = event.keyCode
        if (keyCode === 13) {
            make_post()
        }
    };

    function make_post() {
        fetch('/make_post', {
            method: 'POST',
            body: JSON.stringify({
                content: document.querySelector('#new-content').value
            })
        }).then(response => response.json())
        .then(result => {
            console.log(result);
        })
        
        return false;
    };
});
