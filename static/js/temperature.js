function poll_tmp(id){
    $.ajax({
      url: "/temperature",
    }).done(function(data) {
      data = JSON.parse(data);
      html  = '';
      for(var key in data){
        html += "<div class='sensor col-xs-6'>"+key+"</div>";
        html += "<div class='value col-xs-6'>"+data[key]+"</div>";
      };
      document.getElementById(id).innerHTML = html;
    });
}

function update_sensors(id){
  poll_tmp(id);
  setInterval(function(){
    poll_tmp(id);
  }, 1000);
}
