document.addEventListener('DOMContentLoaded', () => {
    
    // get_posts()
    
    // new post button
    document.querySelector('#post-button').addEventListener('click', make_post);
    document.querySelector('#new-content').onkeypress = (event) => {
        if (!event.shiftKey) {
            if (event.code === 'Enter') {
                make_post()
            }
        }
    };

});

function make_post() {
    document.querySelector('form').submit();
}

// async function make_post() {
//     const post_content = document.querySelector('#new-content');
//     const response = await fetch('/make_post', {
//         method: 'POST',
//         body: JSON.stringify({
//             content: post_content.value
//         })
//     });
//     const result = await response.json();
//     console.log(result);
//     post_content.value = "";
//     get_posts();
//     return false;
// };

// async function get_posts() {
//     const response = await fetch('get_posts');
//     if (response.ok) {
//         const result = await response.json()
//         document.querySelector('#posts').innerHTML = ''
//         // trying to use results outside of the async function returns a promise.
//         // to use it outside of this funcition, use .then() at the function call.
//         result.forEach(element => {
//             create_post_div(element)
//         });
//         return result
//     }
// }

// function create_post_div(post) {
//     const newDiv = document.createElement('div')
//     newDiv.setAttribute('id', post.id)
//     newDiv.setAttribute('class', 'post-div')

//     const pUser = document.createElement('p')
//     pUser.innerHTML = `User: ${post.user}`

//     const pContent = document.createElement('p')
//     pContent.setAttribute('class', 'border')
//     pContent.innerHTML = `Content: ${post.content}`

//     const pTimestamp = document.createElement('p')
//     pTimestamp.innerHTML= `${post.timestamp}`

//     const pLikes = document.createElement('p')
//     pLikes.innerHTML = `Likes: ${post.likes}`

//     newDiv.appendChild(pUser)
//     newDiv.appendChild(pContent)
//     newDiv.appendChild(pTimestamp)
//     newDiv.appendChild(pLikes)
//     document.querySelector('#posts').appendChild(newDiv)
// }