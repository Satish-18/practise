// Book Constructor
function Book(title,author,isbn){
	this.title = title;
	this.author = author;
	this.isbn = isbn;
}


// UI Constructor
function UI(){}

// Add book to list
UI.prototype.addBookToList = function(book){
	const list = document.getElementById('book-list');

	// Create book element
	const row = document.createElement('tr');
	row.innerHTML = `
	<td>${book.title}</td>
	<td>${book.author}</td>
	<td>${book.isbn}</td>
	<td><a href='#' class='delete'>x</a></td>
	`;
	list.appendChild(row);
}

//show alert
UI.prototype.showAlert = function(messege,className){
	// create div
	const div = document.createElement('div');

	// add class
	div.className = `alert ${className}`;
	// add text
	div.appendChild(document.createTextNode(messege));
	// Get parent
	const container = document.querySelector('.container');
	// Get form
	const form  = document.querySelector('#book-form');
	// insert alert
	container.insertBefore(div,form);
	// Time out after 3 sec
	setTimeout(function(){
		document.querySelector('.alert').remove();
	},3000);

}

// Delete book
UI.prototype.deleteBook = function(target){
	if(target.className === 'delete'){
		target.parentElement.parentElement.remove();
	}

}

// Clear fields
UI.prototype.clearFields = function(){
	document.getElementById('title').value = '';
	document.getElementById('author').value = '';
	document.getElementById('isbn').value = '';
}


// Event Listeners
document.getElementById('book-form').addEventListener('submit',
	function(e){
 	// Get form values
	const title = document.getElementById('title').value,
		  author = document.getElementById('author').value,
		  isbn = document.getElementById('isbn').value
	
	// Instantiate book
	const book= new Book(title,author,isbn);

	// Instantiate UI
	const ui = new UI();


	// Validate
	if(title=== '' || author === '' || isbn === ''){
		// Error alert
		ui.showAlert('Please fill in all the fields','error');
		}else{

			// Add to book list
			ui.addBookToList(book);

			// show sucess
			ui.showAlert('Book added!','success');

			// Clear fields
			ui.clearFields(); 
		}

	e.preventDefault();
});

// Event listener for delete
document.getElementById('book-list').addEventListener('click',
	function(e){
		// Instantiate UI
		const ui = new UI();
		// Delete book
		ui.deleteBook(e.target);

		// show messeges
		ui.showAlert('Book removed','success')
		e.preventDefault();
});