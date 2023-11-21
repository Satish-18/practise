const first = () => {
	const greet = 'Hi';
	const second = () => {
		const name = "bobby";
		alert(greet);
	}
	return second;
}
const newFunc = first();
newFunc();
//cosure -a function ran the function executed it's never going run 
// but it's going remenber that there are refrence to those variable
// so the child scope always has access to the parent scope

// curring 
const multiply = (a,b) => a+b;
const curriedMultiply = (a) => (b) => a * b;
const multiplyBy5 = curriedMultiply(5);

//compose 
const compose = (f, g) => (a) => f(g(a));
const sum = (num) => num + 1;
compose(sum, sum)(5);

// Avoiding side effects, functional purity
var a = 1;
function b() {
	a = 2;
}