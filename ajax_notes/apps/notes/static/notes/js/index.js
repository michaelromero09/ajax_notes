$(document).ready(function(){
  console.log("\'ello \'ello \'ello");

  $('form.add-form').submit(function(e){
    console.log('butter')
    e.preventDefault();
    $.ajax({
      url: '/add_note',
      method: 'post',
      data: $(this).serialize(),
      success: function(serverResponse){
        console.log('Cool, man');
        $('.notes').html(serverResponse);
      }
    })
  })

  $('form.delete-form').submit(function(e){
    e.preventDefault();
    $.ajax({
      url: '/delete',
      method: 'post',
      data: $(this).serialize(),
      success: function(serverResponse){
        console.log('Successfully Deleted')
        $('.notes').html(serverResponse);
      }
    })
  })

  $('.edit').editable('http://localhost:8000/edit', { 
        submitdata : { csrfmiddlewaretoken : "{{ csrf_token }}"}
    });
})