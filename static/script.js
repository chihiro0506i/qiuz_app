let quizzes = [];
let currentQuestionIndex = 0;
let score = 0;

document.getElementById('start-button').addEventListener('click', startQuiz);
document.getElementById('next-button').addEventListener('click', showNextQuestion);

async function startQuiz() {
    const response = await fetch('/api/quizzes');
    const data = await response.json();
    quizzes = data.quizzes;

    document.getElementById('start-button').style.display = 'none';
    document.getElementById('quiz-container').style.display = 'block';

    showQuestion();
}

function showQuestion() {
    const quiz = quizzes[currentQuestionIndex];
    document.getElementById('question').textContent = quiz.question;

    const choicesDiv = document.getElementById('choices');
    choicesDiv.innerHTML = '';

    for (let i = 1; i <= 4; i++) {
        const button = document.createElement('button');
        button.textContent = quiz['choice' + i];
        button.addEventListener('click', () => checkAnswer(i));
        choicesDiv.appendChild(button);
    }
}

function checkAnswer(selectedChoice) {
    const quiz = quizzes[currentQuestionIndex];
    if (selectedChoice === quiz.correct_choice) {
        alert('正解！');
        score++;
    } else {
        alert('不正解...');
    }
    document.getElementById('next-button').style.display = 'block';
}

function showNextQuestion() {
    currentQuestionIndex++;
    document.getElementById('next-button').style.display = 'none';

    if (currentQuestionIndex < quizzes.length) {
        showQuestion();
    } else {
        showResult();
    }
}

function showResult() {
    document.getElementById('quiz-container').style.display = 'none';
    document.getElementById('result-container').style.display = 'block';
    document.getElementById('score').textContent = `あなたのスコアは ${score} / ${quizzes.length} です！`;
}
