const search = document.getElementById('search');
const submit = document.getElementById('submit');
const random = document.getElementById('random');
const mealsEl = document.getElementById('meals');
const result_heading = document.getElementById('result-heading');
const single_mealEl = document.getElementById('single-meal');
const latest = document.getElementById('latest')


// Search meal and fetch api
function searchMeal(e) {
    e.preventDefault();

    // Clear single meal
    single_mealEl.innerHTML = ''

    // Get search term
    const term = search.value;

    // Check for empty
    if(term.trim()) {
        fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${term}`)
        .then(res => res.json())
        .then(data => {
            result_heading.innerHTML = `<h2>Search result for '${term}':</h2>`;
            if(data.meals == null) {
                result_heading.innerHTML = `<p> There are no search result. Try again!</p>`;
            } else {
                mealsEl.innerHTML = data.meals.map(meal =>`
                        <div class="meal">
                        <img src="${meal.strMealThumb}" alt="${meal.strMeal}"/>
                        <div class="meal-info" data-mealID = "${meal.idMeal}">
                        <h3>${meal.strMeal}</h3>
                        </div>
                        </div>
                    `)
                .join('');
            }
        });

        // Clear search text

        search.value = '';
    } else {
        console.log('plese enter the word')
    }
}

// Fetch meal by ID
function getMealByID(mealID) {
    fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${mealID}`)
    .then(res => res.json())
    .then(data => {
        const meal = data.meals[0];
        addMealToDOM(meal);
    });
}

// Fetch random meal from API
function getRandomMeal() {
    // Clear meals and heading
    mealsEl.innerHTML = '';
    result_heading.innerHTML = '';
     fetch(`https://www.themealdb.com/api/json/v1/1/random.php`)
     .then(res => res.json())
     .then( data => {
        const meal = data.meals[0];
        addMealToDOM(meal);
     })
}

// Show the latest meals
function showLatestMeal() {
    fetch('https://www.themealdb.com/api/json/v1/1/latest.php')
    .then(res => res.json())
    .then(data => {
    result_heading.innerHTML = `<h2>Lastest Foods:</h2>`;
     mealsEl.innerHTML = data.meals.map(meal =>`
                        <div class="meal">
                        <img src="${meal.strMealThumb}" alt="${meal.strMeal}"/>
                        <div class="meal-info" data-mealID = "${meal.idMeal}">
                        <h3>${meal.strMeal}</h3>
                        </div>
                        </div>
                    `)
                .join('');
}

// Add meal to dom
function addMealToDOM(meal) {
    const ingredients = [];

    for(let i=1; i <=20; i++){
        if(meal[`strIngredient${1}`]) {
            ingredients.push(`${meal[`strIngredient${i}`]} - ${meal[`strIngredient${i}`]}`);
        } else{
            break;
        }
    }
    single_mealEl.innerHTML =  `
    <div class="single-meal">
        <h1>${meal.strMeal}</h1>
        <img src="${meal.strMealThumb}"/>
        <div class="single-meal-info">
        ${meal.strCategory ? `<p>${meal.strCategory}</p>` : ''}
        ${meal.strArea ? `<p>${meal.strArea}</p>` : ''}
        </div>
        <div class="main">
        <p>${meal.strInstructions}</p>
        <h2>Ingredients</h2>
        <ul>
        ${ingredients.map(ing => `<li>${ing}</li>`).join('')}
        </ul>
    </div>
    `;
}

// event listener
submit.addEventListener('click', searchMeal );
random.addEventListener('click', getRandomMeal );

mealsEl.addEventListener('click', e=> {
    const mealInfo = e.path.find(item => {
        if(item.classList) {
            return item.classList.contains('meal-info');
        } else {
            return false;
        }
    });

    if(mealInfo) {
        const mealID = mealInfo.getAttribute('data-mealID');
        getMealByID(mealID);
    }

    showLatestMeal();
});