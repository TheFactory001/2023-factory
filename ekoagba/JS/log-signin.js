// DOM elements
const signupForm = document.getElementById("signupForm");
const loginForm = document.getElementById("loginForm");
const otpForm = document.getElementById("otpForm");
const showLoginBtn = document.getElementById("showLogin");
const showSignupBtn = document.getElementById("showSignup");
const resendOtpBtn = document.getElementById("resendOtp");
const otpMessage = document.getElementById("otpMessage");

// Store generated OTP
let currentOtp = "";
let currentVerificationMethod = "";

// Toggle between forms
showLoginBtn.addEventListener("click", (e) => {
  e.preventDefault();
  signupForm.classList.add("hidden");
  otpForm.classList.add("hidden");
  loginForm.classList.remove("hidden");
});

showSignupBtn.addEventListener("click", (e) => {
  e.preventDefault();
  loginForm.classList.add("hidden");
  otpForm.classList.add("hidden");
  signupForm.classList.remove("hidden");
});

// Generate OTP
function generateOTP() {
  return Math.floor(100000 + Math.random() * 900000).toString();
}

// Simulate sending OTP
function sendOTP(to, method) {
  currentOtp = generateOTP();
  console.log(`OTP sent to ${to} via ${method}: ${currentOtp}`);
  alert(`Your OTP is: ${currentOtp} ${method}`);
}

// Handle signup form submission
signupForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const email = document.getElementById("signupEmail").value;
  const phone = document.getElementById("signupPhone").value;
  const verificationMethod = document.querySelector(
    'input[name="verificationMethod"]:checked'
  ).value;

  currentVerificationMethod = verificationMethod;

  if (verificationMethod === "email") {
    sendOTP(email, "email");
  } else {
    sendOTP(phone, "SMS");
  }

  signupForm.classList.add("hidden");
  otpForm.classList.remove("hidden");
});

// Handle login form submission
loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const email = document.getElementById("loginEmail").value;
  const password = document.getElementById("loginPassword").value;

  // Here you would typically validate against a backend
  alert("Login successful!");
});

// Handle OTP verification
otpForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const enteredOtp = document.getElementById("otp").value;

  if (enteredOtp === currentOtp) {
    alert("OTP verified successfully! Account created.");
    // Reset and show login form
    otpForm.classList.add("hidden");
    loginForm.classList.remove("hidden");
    signupForm.reset();
    otpForm.reset();
  } else {
    otpMessage.textContent = "Invalid OTP. Please try again.";
    otpMessage.classList.add("error");
  }
});

// Handle OTP resend
resendOtpBtn.addEventListener("click", () => {
  const email = document.getElementById("signupEmail").value;
  const phone = document.getElementById("signupPhone").value;

  if (currentVerificationMethod === "email") {
    sendOTP(email, "email");
  } else {
    sendOTP(phone, "SMS");
  }

  otpMessage.textContent = "New OTP sent!";
  otpMessage.classList.remove("error");
});
