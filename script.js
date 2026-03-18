// SIGNUP
function signup() {
    let user = document.getElementById("signupUser").value;
    let pass = document.getElementById("signupPass").value;

    localStorage.setItem("user", user);
    localStorage.setItem("pass", pass);

    alert("Signup successful!");
    window.location.href = "login.html";
}

// LOGIN
function login() {
    let user = document.getElementById("loginUser").value;
    let pass = document.getElementById("loginPass").value;

    let storedUser = localStorage.getItem("user");
    let storedPass = localStorage.getItem("pass");

    if (user === storedUser && pass === storedPass) {
        window.location.href = "dashboard.html";
    } else {
        alert("Invalid credentials");
    }
}

// LOGOUT
function logout() {
    window.location.href = "index.html";
}

// AI ANALYSIS
function analyze() {
    let q = document.getElementById("question").value.toLowerCase();
    let result = document.getElementById("result");

    if (q.includes("python") || q.includes("code")) {
        result.innerHTML = "👨‍💻 Python Expert ⭐⭐⭐⭐";
    }
    else if (q.includes("math")) {
        result.innerHTML = "🧠 Math Expert ⭐⭐⭐⭐⭐";
    }
    else if (q.includes("ai")) {
        result.innerHTML = "🤖 AI Specialist ⭐⭐⭐⭐⭐";
    }
    else {
        result.innerHTML = "🎓 General Mentor ⭐⭐⭐";
    }
}