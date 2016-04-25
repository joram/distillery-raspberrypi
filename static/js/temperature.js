function poll_tmp(id){
    $.ajax({
      url: "/temperature",
    }).done(function(data) {
      data = JSON.parse(data);
      tbody = $("#"+id).find("tbody");
      tbody.find(".auto-update").remove();
      
      var keys = []
      for(var key in data) keys.push( key );
      keys.sort();

      // forgive me father, for I have sined with ugly code.
      for (var i = 0; i < keys.length; i++) {      
        var key=keys[i];
        var value = data[key]; 
        tbody.append("<tr class='auto-update'><td class='key'>"+key+"</td><td class='value'>"+value+"</td></tr>");
      };
    });
}

function update_sensors(id){
  poll_tmp(id);
  setInterval(function(){
    poll_tmp(id);
  }, 1000);
}
