document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // archive and reply buttons
  document.querySelector('#archive-unarchive').addEventListener('click', archive_email);
  document.querySelector('#reply').addEventListener('click', reply_email);

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
    setTimeout(() => {
      load_mailbox('sent');
      window.localStorage.clear()
    })
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
  
  // fetch mailbox
  fetch(`emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    emails.forEach(email => {
      
      const element = document.createElement('div');
      if (email.read) {
        element.setAttribute('class', 'email-item-read')
      } else {
        element.setAttribute('class', 'email-item')
      }
      element.innerHTML = `<span class="sender">${email.sender}</span> 
      <span class="subject">${email.subject}</span> 
      <span class="timestamp">${email.timestamp}</span>`;
      element.addEventListener('click', function() {
        get_email(email.id)
      }); 
      document.querySelector('#emails-view').append(element);
    });
  });
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';

  
  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
}

async function fetchEmail(email_id) {
  let response = await fetch(`/emails/${email_id}`);
  let email = await response.json();
  window.localStorage.setItem('email', JSON.stringify(email));
  return email
}

function stringToBoolean(value){
  return (String(value).toLowerCase() === 'true');
}

function archive_email() {
  fetch(`/emails/${this.dataset.id}`, {
    method: 'PUT',
    body: JSON.stringify({
      archived: stringToBoolean(this.dataset.toArchive)
    })
  })
    .then(response => {
      if (response.ok) {
        setTimeout(() => {
    (load_mailbox('inbox'));
    (window.localStorage.clear());
  });
      } else {
        throw new Error(response.status)
      }
    })
    .catch(error => {
      window.alert(error);
    });

  
  return false
}

function reply_email() {
  let email = JSON.parse(window.localStorage.getItem('email'));
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-view').style.display = 'none';
  
  // Clear out composition fields
  document.querySelector('#compose-recipients').value = email.sender;

  // slice to check if RE: already exists
  let subject_element = document.querySelector('#compose-subject');
  if (email.subject.slice(0, 3) === 'Re:') {
    subject_element.value = email.subject;
  } else {
    subject_element.value = `Re: ${email.subject}`;
  }
  document.querySelector('#compose-body').value = `\nOn ${email.timestamp} ${email.sender} wrote: \n${email.body}`;
}

async function get_email(email_id) {
  
  // show email view and hide other views
  document.querySelector('#email-view').style.display = 'block';
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  
  // clear last email before loading again
  const children = document.querySelectorAll('.email-info > span')
  children.forEach(child => {
    child.innerHTML = '';
  })
  document.querySelector('#email-body').innerHTML = '';
  
  let email = await fetchEmail(email_id);
  
  // Render email
  document.querySelector('#from').innerHTML += `<strong>From:</strong> ${email.sender}`;
  document.querySelector('#to').innerHTML += `<strong>To:</strong> ${email.recipients}`;
  document.querySelector('#subject').innerHTML += `<strong>Subject:</strong> ${email.subject}`;
  document.querySelector('#timestamp').innerHTML += `<strong>Timestamp:</strong> ${email.timestamp}`;
  document.querySelector('#email-body').innerHTML += ` ${email.body}`;
  
  // archive button appearance and data setting
  const archive_button = document.querySelector('#archive-unarchive');
  if (email.archived) {
    archive_button.innerHTML = 'Unarchive'
    archive_button.dataset.toArchive = false
  } else {
    archive_button.innerHTML = 'Archive'
    archive_button.dataset.toArchive = true
  };
  archive_button.dataset.id = email_id;

  // email read request
  if (!email.read) {
    fetch(`/emails/${email.id}`, {
      method: 'PUT',
      body: JSON.stringify({
        read: true
      })
    })
  }
}