// var openNav = document.getElementById("openNav")
// var closeNav = document.getElementById("closeNav")

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}



// Get the necessary DOM elements
const themeSelect = document.getElementById('theme');
const fontSizeSelect = document.getElementById('font-size');
const saveAppearanceButton = document.getElementById('save-appearance');

// Load the user's saved appearance settings
loadAppearanceSettings();

// Add event listener for the "Save Changes" button
saveAppearanceButton.addEventListener('click', saveAppearanceSettings);

// Function to load the user's saved appearance settings
function loadAppearanceSettings() {
  // Check if the user's appearance settings are saved in the browser
  const savedTheme = localStorage.getItem('theme');
  const savedFontSize = localStorage.getItem('fontSize');

  // Set the selected options in the UI
  if (savedTheme) {
    themeSelect.value = savedTheme;
    updateTheme(savedTheme);
  }

  if (savedFontSize) {
    fontSizeSelect.value = savedFontSize;
    updateFontSize(savedFontSize);
  }
}

// Function to save the user's appearance settings
function saveAppearanceSettings() {
  const selectedTheme = themeSelect.value;
  const selectedFontSize = fontSizeSelect.value;

  // Save the settings in the browser's localStorage
  localStorage.setItem('theme', selectedTheme);
  localStorage.setItem('fontSize', selectedFontSize);

  // Update the appearance based on the selected settings
  updateTheme(selectedTheme);
  updateFontSize(selectedFontSize);
}

// Function to update the theme
function updateTheme(theme) {
  // Add your logic to update the theme here
  // For example, you can add/remove CSS classes to the body element
  document.body.classList.remove('light', 'dark');
  document.body.classList.add(theme);
}

// Function to update the font size
function updateFontSize(fontSize) {
  // Add your logic to update the font size here
  // For example, you can set the font-size property on the body element
  document.body.style.fontSize = fontSize === 'small' ? '14px'
    : fontSize === 'medium' ? '16px'
    : '18px';
}







// ADMIN DASHBOARD

// Simulate data retrieval
document.addEventListener("DOMContentLoaded", function() {
  const userCount = 1234;
  const signupCount = 57;
  const postCount = 891;

  // Update stats on the dashboard
  document.getElementById("user-count").textContent = userCount;
  document.getElementById("signup-count").textContent = signupCount;
  document.getElementById("post-count").textContent = postCount;
});


// USER MANAGEMENT

document.addEventListener("DOMContentLoaded", () => {
  const editButtons = document.querySelectorAll(".edit-btn");
  const deleteButtons = document.querySelectorAll(".delete-btn");

  editButtons.forEach(button => {
      button.addEventListener("click", () => {
          const row = button.parentNode.parentNode;
          const username = row.children[1].textContent;
          alert(`Edit user: ${username}`);
          // Additional code for editing user
      });
  });

  deleteButtons.forEach(button => {
      button.addEventListener("click", () => {
          const row = button.parentNode.parentNode;
          const username = row.children[1].textContent;
          if (confirm(`Are you sure you want to delete ${username}?`)) {
              row.remove();
              alert(`${username} has been deleted.`);
          }
          // Additional code for deleting user
      });
  });
});




document.addEventListener("DOMContentLoaded", () => {
  const approveButtons = document.querySelectorAll(".approve-btn");
  const rejectButtons = document.querySelectorAll(".reject-btn");
  const deleteButtons = document.querySelectorAll(".delete-btn");

  approveButtons.forEach(button => {
      button.addEventListener("click", () => {
          const row = button.closest("tr");
          const contentID = row.children[0].textContent;
          alert(`Content ID ${contentID} has been approved.`);
          // Update the row to reflect approval (optional)
          row.children[5].textContent = "Approved";
      });
  });

  rejectButtons.forEach(button => {
      button.addEventListener("click", () => {
          const row = button.closest("tr");
          const contentID = row.children[0].textContent;
          alert(`Content ID ${contentID} has been rejected.`);
          // Update the row to reflect rejection (optional)
          row.children[5].textContent = "Rejected";
      });
  });

  deleteButtons.forEach(button => {
      button.addEventListener("click", () => {
          const row = button.closest("tr");
          const contentID = row.children[0].textContent;
          if (confirm(`Are you sure you want to delete content ID ${contentID}?`)) {
              row.remove();
              alert(`Content ID ${contentID} has been deleted.`);
          }
      });
  });
});


// Dummy data for metrics and charts
const totalUsers = 5000;
const totalPosts = 15000;
const newUsersLast7Days = 200;

document.getElementById("total-users").textContent = totalUsers;
document.getElementById("total-posts").textContent = totalPosts;
document.getElementById("new-users").textContent = newUsersLast7Days;

// User Growth Line Chart
const userGrowthCtx = document.getElementById('userGrowthChart').getContext('2d');
const userGrowthChart = new Chart(userGrowthCtx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov'],
        datasets: [{
            label: 'User Growth',
            data: [500, 800, 1200, 1800, 2400, 3000, 3500, 4000, 4500, 4800, totalUsers],
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: true }
        },
        scales: {
            y: { beginAtZero: true }
        }
    }
});

// Post Activity Bar Chart
const postActivityCtx = document.getElementById('postActivityChart').getContext('2d');
const postActivityChart = new Chart(postActivityCtx, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov'],
        datasets: [{
            label: 'Posts Per Month',
            data: [200, 400, 600, 800, 1200, 1500, 1700, 1900, 2200, 2500, totalPosts / 10],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: true }
        },
        scales: {
            y: { beginAtZero: true }
        }
    }
});

// User Engagement Doughnut Chart
const engagementCtx = document.getElementById('engagementChart').getContext('2d');
const engagementChart = new Chart(engagementCtx, {
    type: 'doughnut',
    data: {
        labels: ['Likes', 'Comments', 'Shares', 'Reposts'],
        datasets: [{
            label: 'User Engagement',
            data: [5000, 2000, 1000, 500],
            backgroundColor: [
                'rgba(75, 192, 192, 0.6)',
                'rgba(153, 102, 255, 0.6)',
                'rgba(255, 159, 64, 0.6)',
                'rgba(54, 162, 235, 0.6)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { position: 'top' }
        }
    }
});



// EVENVTS AND CALENDAR

document.addEventListener("DOMContentLoaded", function() {
  const addEventButton = document.getElementById("addEventButton");
  const addEventModal = document.getElementById("addEventModal");
  const closeButton = document.querySelector(".close-button");
  const eventList = document.getElementById("eventList");
  const eventForm = document.getElementById("eventForm");

  // Open modal on button click
  addEventButton.addEventListener("click", () => {
      addEventModal.style.display = "flex";
  });

  // Close modal on clicking close button
  closeButton.addEventListener("click", () => {
      addEventModal.style.display = "none";
  });

  // Close modal when clicking outside the modal content
  window.addEventListener("click", (e) => {
      if (e.target == addEventModal) {
          addEventModal.style.display = "none";
      }
  });

  // Handle form submission to add new events
  eventForm.addEventListener("submit", (e) => {
      e.preventDefault();

      // Get form values
      const title = document.getElementById("eventTitle").value;
      const date = document.getElementById("eventDate").value;
      const description = document.getElementById("eventDescription").value;

      // Add event to the list
      const li = document.createElement("li");
      li.innerHTML = `<strong>${title}</strong> - ${date}<br><small>${description}</small>`;
      eventList.appendChild(li);

      // Clear form and close modal
      eventForm.reset();
      addEventModal.style.display = "none";
  });
});


document.addEventListener("DOMContentLoaded", function() {
  const newNotificationButton = document.getElementById("newNotificationButton");
  const newNotificationModal = document.getElementById("newNotificationModal");
  const closeButton = document.querySelector(".close-button");
  const notificationForm = document.getElementById("notificationForm");
  const notificationsList = document.getElementById("notificationsList");
  const messagesList = document.getElementById("messagesList");

  // Open modal on button click
  newNotificationButton.addEventListener("click", () => {
      newNotificationModal.style.display = "flex";
  });

  // Close modal on clicking close button
  closeButton.addEventListener("click", () => {
      newNotificationModal.style.display = "none";
  });

  // Close modal when clicking outside the modal content
  window.addEventListener("click", (e) => {
      if (e.target == newNotificationModal) {
          newNotificationModal.style.display = "none";
      }
  });

  // Handle form submission to add new notifications
  notificationForm.addEventListener("submit", (e) => {
      e.preventDefault();

      // Get form values
      const title = document.getElementById("notificationTitle").value;
      const message = document.getElementById("notificationMessage").value;

      // Add notification to the list
      const li = document.createElement("li");
      li.classList.add("notification-item");
      li.innerHTML = `<strong>${title}</strong><br>${message}`;
      notificationsList.appendChild(li);

      // Clear form and close modal
      notificationForm.reset();
      newNotificationModal.style.display = "none";
  });

  // Simulate fetching user messages
  const messages = [
      { sender: "User1", content: "Hello, I need help with my account." },
      { sender: "User2", content: "Can you assist me with posting?" },
  ];

  messages.forEach(message => {
      const messageDiv = document.createElement("div");
      messageDiv.classList.add("message-item");
      messageDiv.innerHTML = `<strong>${message.sender}:</strong> ${message.content}`;
      messagesList.appendChild(messageDiv);
  });
});




// STUDENT PROFILE


// Display a message alert when 'Send Message' button is clicked
function sendMessage() {
  alert("Message sent to John Doe!");
}

// Redirect to a more detailed activity page when 'View All Activities' button is clicked
function viewMoreActivities() {
  alert("Loading full activity history...");
  // Replace this with actual navigation if necessary:
  // window.location.href = "/student-activities";
}

// Simulate loading of student profile data
document.addEventListener("DOMContentLoaded", function() {
  // Placeholder data can be fetched and updated here if using a backend
  const studentName = document.getElementById("studentName");
  const activityList = document.getElementById("activityList");

  // Update student name (example: loaded from a database)
  studentName.innerText = "Jane Smith";

  // Populate recent activities (replace with fetched data if available)
  activityList.innerHTML = `
      <li>Submitted Project Proposal - Nov 1, 2024</li>
      <li>Attended Networking Workshop - Oct 25, 2024</li>
      <li>Completed Data Science Course - Oct 15, 2024</li>
  `;
});






document.getElementById('send-button').addEventListener('click', function() {
    const content = document.getElementById('message-input').value;
    const receiver_id = document.getElementById('receiver_id').value;

    fetch('/send-message', {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
        },
        body: JSON.stringify({receiver_id, content}),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'Message sent') {
            loadMessages(receiver_id);
            document.getElementById('message-input').value = '';
        }
    });
});

function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

function loadMessages(receiver_id) {
    fetch('get-messages/${receiver_id}/')
    .then(response => response.json())
    .then(data => {
        const chatbox = document.getElementById('chat-box');
        chatbox.innerHTML = '';

        // Display the messages
        data.messages.forEach(msg => {
            const messageDiv = document.createElement('div');
            messageDiv.textContent = '${msg.sender}: ${msg.content}';
            chatbox.appendChild(messageDiv)
        });
    });
}