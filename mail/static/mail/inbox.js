document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
  
  // form submit
  document.querySelector('form').onsubmit = () => {
    // send email
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: document.querySelector('#compose-recipients').value,
          subject: document.querySelector('#compose-subject').value,
          body: document.querySelector('#compose-body').value
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
    });
    load_mailbox('sent');
    return false;
  }
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-view').style.display = 'none';
  
  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
  
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';

  
  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // fetch mailbox
  fetch(`emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      console.log(emails);
      
      // ... do something else with emails ...
      
      // for each email create div that displays sender, subject line, timestamp
      // if read it should appear with grey background. 
      emails.forEach(email => {
        
        const element = document.createElement('div');
        if (email.read) {
          element.setAttribute('class', 'email-item-read')
        } else {
          element.setAttribute('class', 'email-item')
        }
        element.innerHTML = `<span class="sender">${email.sender}</span> 
        <span class="body">${email.body}</span> 
        <span class="timestamp">${email.timestamp}</span>`;
        element.addEventListener('click', function() {
          get_email(email.id)
        }); 
        document.querySelector('#emails-view').append(element);
      });
  });
}

function get_email(email_id) {
  
  document.querySelector('#email-view').style.display = 'block';
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

  const children = document.querySelectorAll('.email-info > span')
  children.forEach(child => {
    child.innerHTML = '';
  })

  document.querySelector('#email-body').innerHTML = '';

  fetch(`/emails/${email_id}`)
  .then(response => response.json())
  .then(email => {
    // Print email
    console.log(email);
    document.querySelector('#from').innerHTML += `<strong>From:</strong> ${email.sender}`;
    document.querySelector('#to').innerHTML += `<strong>To:</strong> ${email.recipients}`;
    document.querySelector('#subject').innerHTML += `<strong>Subject:</strong> ${email.subject}`;
    document.querySelector('#timestamp').innerHTML += `<strong>Timestamp:</strong> ${email.timestamp}`;
    document.querySelector('#email-body').innerHTML += ` ${email.body}`;
    if (email.archived) {
      document.querySelector('#archive-unarchive').innerHTML = 'Unarchive'
    } else {
      document.querySelector('#archive-unarchive').innerHTML = 'Archive'
    };
  });

  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: true
    })
  })
}

