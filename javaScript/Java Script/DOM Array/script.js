const main = document.getElementById('main')
const addUserBtn = document.getElementById('add_user')
const doubleBtn = document.getElementById('double_money')
const showMillionearsBtn = document.getElementById('show_millionaires')
const sortBtn = document.getElementById('sort')
const calculateBtn = document.getElementById('calculate_wealth')

let data = [];
getRandomUser();
getRandomUser();
getRandomUser();

// Fetch random user and add money
async function getRandomUser() {
    const res = await fetch('https://randomuser.me/api');
    const data = await res.json();
    const user = data.results[0];

    const newUser = {
        name: `${user.name.first} ${user.name.last}`, money: Math.floor(Math.random() * 1000000)
    };
    addData(newUser);
}

// Double everyones money
function doubleMoney() {
    data = data.map((user) => {
        return {...user, money: user.money * 2};
    });

    updateDOM();
}

// Sort everyone by money
function sortByMoney() {
    data.sort((a,b) => b.money - a.money);

    updateDOM();
}

// Show only millioniear
function showMillionears() {
    data = data.filter(user => user.money > 1000000);
    updateDOM();
}

// Calculate entire wealth
function totalWealth() {
    const total = data.reduce((acc, user) => (acc =+ user.money), 0);

    const welthEl = document.createElement('div');
    welthEl.innerHTML = `<h3>Total Wealth: <strong>${formatMoney(total)}</strong></h3>`;
    main.appendChild(welthEl);
}

// Add new obj to data arr
function addData(obj) {
    data.push(obj);

    updateDOM();
}

// Update DOM
function updateDOM(providedData = data) {

    // Clear main div
    main.innerHTML  = `<h2><strong>Person</strong>Wealth</h2>`;

    providedData.forEach(item => {
        const element = document.createElement('div');
        element.classList.add('person');
        element.innerHTML = `<strong>${item.name}</strong> ${formatMoney(item.money)}`;
        main.appendChild(element);
    });
}

function formatMoney(number) {
    return '$' + number.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
}

// Event listener

addUserBtn.addEventListener('click',getRandomUser);
doubleBtn.addEventListener('click',doubleMoney);
sortBtn.addEventListener('click',sortByMoney);
showMillionearsBtn.addEventListener('click',showMillionears);
calculateBtn.addEventListener('click',totalWealth);