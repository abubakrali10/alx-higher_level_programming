$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (data) {
    const myList = $('UL#list_movies');
    for (let i = 0; i < data.results.length; i++) {
      const listItem = $('<li></li>');
      listItem.text(data.results[i].title);
      myList.append(listItem);
    }
  }
});
