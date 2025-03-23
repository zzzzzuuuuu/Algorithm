function another(my_string, index_list) {
  return index_list.map(i => my_string[i]).join('');
}

function another2(my_string, index_list) {
  return index_list.reduce((result, i) => result + my_string[i], '');
}