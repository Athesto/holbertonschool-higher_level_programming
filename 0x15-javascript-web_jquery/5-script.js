
function addItem () {
  $('ul.my_list').append('\n<li>Item</li>');
}

$('div#add_item').click(addItem);
