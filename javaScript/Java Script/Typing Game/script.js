const word = document.getElementById('word');
const text = document.getElementById('text');
const score = document.getElementById('score');
const timeEl = document.getElementById('time');
const endgameEl = document.getElementById('end-game');
const settingBtn = document.getElementById('settings-btn');
const settings = document.getElementById('settings');
const word = document.getElementById('settings-form');
const difficultySelect = document.getElementById('difficulty');

// list of words for game

const words = [
'end',
'happy',
'sad',
'angry'
];


// Init word
let randomWord;


// Init score
let score = 0;

//Init time
let time = 0;

// Generate random word from array
function getRandomWord() {
	return words[Math.floor(Math.random() * words.length)];
}

console.log(getRandomWord());



// Add word to DOM

function addWordToDON() {
	randomWord = getRandomWord();
	word.innerHTML = randomWord;
}

// Update score
function updateScore() {
	score++;
	scoreEl.innerHTML = score;
}


addWordToDON();

// Event listener

text.addEventListner('input',e => {
	const insertText = e.target.value;

	if(insertedText == randomWord) {
		addWordToDOM();

		// Clear
		e.target.value = '';
	}
});