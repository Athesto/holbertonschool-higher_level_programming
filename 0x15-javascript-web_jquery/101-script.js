const newElement = '\n<li>Item</li>';

function addElement () {
  console.log('hello');
  $('ul.my_list').append(newElement);
}

function removeElement () {
  console.log('delete');
  $('ul.my_list li:last-child').remove();
}

function clearList () {
  console.log('clear');
  $('ul.my_list').empty();
}

function loadedPage () {
  $('div#add_item').click(addElement);
  $('div#remove_item').click(removeElement);
  $('div#clear_list').click(clearList);
}

$(document).ready(loadedPage);
