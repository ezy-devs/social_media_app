function submitForm(event) {
    event.preventDefault(); // Prevent form submission
    
    // Get form values
    const studentName = document.getElementById("studentName").value;
    const studentID = document.getElementById("studentID").value;
    const email = document.getElementById("email").value;
    const course = document.getElementById("course").value;
    const yearOfStudy = document.getElementById("yearOfStudy").value;
    const gpa = document.getElementById("gpa").value;
    const department = document.getElementById("department").value;
    const specialization = document.getElementById("specialization").value;
    const recentActivities = document.getElementById("recentActivities").value.split(',');

    // Create a student profile object
    const studentProfile = {
        name: studentName,
        id: studentID,
        email: email,
        course: course,
        yearOfStudy: yearOfStudy,
        gpa: gpa,
        department: department,
        specialization: specialization,
        activities: recentActivities
    };

    // Log the profile data (In a real application, send this to a server)
    console.log("Student Profile Saved:", studentProfile);

    // Show success message
    alert("Student profile saved successfully!");

    // Clear form
    document.getElementById("studentProfileForm").reset();
}
