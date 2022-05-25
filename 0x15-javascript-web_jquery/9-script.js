$.get('https://fourtonfish.com/hellosalut/?lang=fr', { hello: 'Salut' }, function (data) {
  $('#hello').append(data.hello);
});
