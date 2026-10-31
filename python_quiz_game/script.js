
const questions = [
    {
        question: "Which keyword is used to check a condition?",
        answers: ["for", "if", "print", "input"],
        correct: 1
    },
    {
        question: "Which data type stores True or False?",
        answers: ["int", "str", "bool", "float"],
        correct: 2
    },
    {
        question: "What is the output of 5 + 3?",
        answers: ["2", "8", "15", "53"],
        correct: 1
    },
    {
        question: "Which loop runs while a condition is True?",
        answers: ["if", "break", "while", "pass"],
        correct: 2
    },
    {
        question: "Which symbol checks equality in Python?",
        answers: ["=", "==", "!=", "+"],
        correct: 1
    }
];

const welcomeScreen = document.getElementById("welcome-screen");
const quizScreen = document.getElementById("quiz-screen");
const resultScreen = document.getElementById("result-screen");

const nameInput = document.getElementById("player-name");
const startBtn = document.getElementById("start-btn");
const nextBtn = document.getElementById("next-btn");
const restartBtn = document.getElementById("restart-btn");

const questionElement = document.getElementById("question");
const answerButtons = document.getElementById("answer-buttons");
const questionCount = document.getElementById("question-count");
const timerElement = document.getElementById("timer");
const progressBar = document.getElementById("progress-bar");

let currentQuestion = 0;
let score = 0;
let playerName = "";
let timeLeft = 15;
let timer;

function shuffleQuestions() {
    questions.sort(() => Math.random() - 0.5);
}

startBtn.addEventListener("click", startQuiz);
nextBtn.addEventListener("click", nextQuestion);
restartBtn.addEventListener("click", restartQuiz);

function startQuiz() {

    playerName = nameInput.value.trim();

    if (playerName === "") {
        alert("Please enter your name!");
        return;
    }

    welcomeScreen.classList.add("hide");
    resultScreen.classList.add("hide");
    quizScreen.classList.remove("hide");

    currentQuestion = 0;
    score = 0;

    shuffleQuestions();
    showQuestion();
}

function showQuestion() {

    resetScreen();

    let question = questions[currentQuestion];

    questionElement.textContent = question.question;

    questionCount.textContent =
        `Question ${currentQuestion + 1} of ${questions.length}`;

    progressBar.style.width =
        ((currentQuestion + 1) / questions.length * 100) + "%";

    question.answers.forEach((answer, index) => {

        const button = document.createElement("button");

        button.textContent =
            String.fromCharCode(65 + index) + ". " + answer;

        button.addEventListener("click", () => selectAnswer(index, button));

        answerButtons.appendChild(button);
    });

    startTimer();
}

function resetScreen() {

    clearInterval(timer);

    nextBtn.classList.add("hide");
    answerButtons.innerHTML = "";

    timeLeft = 15;
    timerElement.textContent = "15 seconds";
}

function startTimer() {

    timerElement.textContent = timeLeft + " seconds";

    timer = setInterval(() => {

        timeLeft--;

        timerElement.textContent = timeLeft + " seconds";

        if (timeLeft <= 0) {
            clearInterval(timer);
            selectAnswer(-1, null);
        }

    }, 1000);
}

function selectAnswer(selectedIndex, selectedButton) {

    clearInterval(timer);

    const correctIndex = questions[currentQuestion].correct;

    const buttons = answerButtons.children;

    for (let i = 0; i < buttons.length; i++) {

        buttons[i].disabled = true;

        if (i === correctIndex) {
            buttons[i].classList.add("correct");
        }
    }

    if (selectedIndex === correctIndex) {

        score++;

    } else if (selectedButton !== null) {

        selectedButton.classList.add("wrong");

    }

    nextBtn.classList.remove("hide");
}

function nextQuestion() {

    currentQuestion++;

    if (currentQuestion < questions.length) {

        showQuestion();

    } else {

        showResult();
    }
}

function showResult() {

    quizScreen.classList.add("hide");
    resultScreen.classList.remove("hide");

    let percentage = (score / questions.length) * 100;

    document.getElementById("result-name").textContent =
        "Well done, " + playerName + "!";

    document.getElementById("final-score").textContent =
        score + " / " + questions.length;

    document.getElementById("percentage").textContent =
        percentage + "%";

    let feedback = "";

    if (percentage >= 80) {
        feedback = "Excellent performance!";
    } else if (percentage >= 60) {
        feedback = "Very good! Keep learning.";
    } else if (percentage >= 40) {
        feedback = "Good try! Practice more.";
    } else {
        feedback = "Don't give up! Try again.";
    }

    document.getElementById("feedback").textContent = feedback;
}

function restartQuiz() {

    resultScreen.classList.add("hide");
    welcomeScreen.classList.remove("hide");

    nameInput.value = "";
}
