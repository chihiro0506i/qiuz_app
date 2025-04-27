let questions = [];
let currentQuestionIndex = 0;
let score = 0;

const startButton = document.getElementById('start-btn');
const questionContainer = document.getElementById('question-container');
const questionElement = document.getElementById('question');
const choiceButtons = Array.from(document.getElementsByClassName('choice-btn'));
const resultContainer = document.getElementById('result-container');
const scoreElement = document.getElementById('score');

// スタートボタンを押したとき
startButton.addEventListener('click', startQuiz);

async function startQuiz() {
    const res = await fetch("/api/quizzes");
    const data = await res.json();

    // 外部APIなので "results" を取り出す！
    questions = data.results;

    currentQuestionIndex = 0;
    score = 0;

    startButton.classList.add('hide');
    resultContainer.classList.add('hide');
    questionContainer.classList.remove('hide');

    showQuestion();
}

function showQuestion() {
    if (currentQuestionIndex >= questions.length) {
        endQuiz();
        return;
    }

    const currentQuestion = questions[currentQuestionIndex];
    questionElement.innerHTML = decodeHTML(currentQuestion.question);

    // 正解 + 不正解をまとめる
    const choices = [...currentQuestion.incorrect_answers, currentQuestion.correct_answer];
    shuffleArray(choices);

    // ボタンに選択肢をセット
    choiceButtons.forEach((button, index) => {
        if (choices[index]) {
            button.classList.remove('hide');
            button.innerHTML = decodeHTML(choices[index]);
            button.onclick = () => selectAnswer(choices[index], currentQuestion.correct_answer);
        } else {
            button.classList.add('hide');
        }
    });
}

function selectAnswer(selectedChoice, correctChoice) {
    if (selectedChoice === correctChoice) {
        score++;
    }
    currentQuestionIndex++;
    showQuestion();
}

function endQuiz() {
    questionContainer.classList.add('hide');
    resultContainer.classList.remove('hide');
    scoreElement.innerText = `あなたのスコア: ${score} / ${questions.length}`;

    startButton.innerText = "もう一度プレイ";
    startButton.classList.remove('hide');
}

// 配列をシャッフルする関数（Fisher-Yatesアルゴリズム）
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

// HTMLエンティティをデコードする関数（&quot; → " など）
function decodeHTML(html) {
    const txt = document.createElement('textarea');
    txt.innerHTML = html;
    return txt.value;
}
