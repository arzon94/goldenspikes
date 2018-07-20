// (function(context) {
//
//     // utc_epoch comes from index.py
//     console.log('Current epoch in UTC is ' + context.utc_epoch);
//
// })(DMP_CONTEXT.get());
$(function(){
  $('.status').closest('p').hide()
  $('.category').closest('p').hide()

  var division = $('#id_division')
  division.on('change', function(){
    if(division.val()== 'd1'){
      $('#id_d2category').closest('p').hide(500)
      $('#id_d1category').closest('p').show(500)
      $('.status').closest('p').hide(500)
      $('#id_1status').closest('p').show(500)
    }
    else if(division.val()=='d2'){
      $('#id_d1category').closest('p').hide(500)
      $('#id_d2category').closest('p').show(500)
      $('.status').closest('p').hide(500)
    }
  })
  var category1 = $('#id_d1category')
  var category2 = $('#id_d2category')
  category2.on('change', function(){
    $('.status').closest('p').hide(500)
    if((category2.val()=='Publicity and Media Relations') || (category2.val()=='Print Communications') || (category2.val()=='Research') || (category2.val()=='Social Media') ){
      $('#id_1status').closest('p').show(500)
    }
    else if(category2.val()== 'Videos' || category2.val()== 'Interactive Communications'){
      $('#id_2status').closest('p').show(500)
    }
    else if(category2.val()=='Photography and Illustrations'){
      $('#id_3status').closest('p').show(500)
    }
    else if(category2.val()=='Writing'){
      $('#id_4status').closest('p').show(500)
    }
  })
})
