function poll_tmp(id){
    $.ajax({
      url: "/temperature",
    }).done(function(data) {
      data = JSON.parse(data);
      tbody = $("#"+id).find("tbody");
      tbody.find(".auto-update").remove();
      for(var key in data){
        tbody.append("<tr class='auto-update'><td class='key'>"+key+"</td><td class='value'>"+data[key]+"</td></tr>");
      };
    });
}

function update_sensors(id){
  poll_tmp(id);
  setInterval(function(){
    poll_tmp(id);
  }, 1000);
}
