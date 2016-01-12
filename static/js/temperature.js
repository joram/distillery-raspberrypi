function poll_tmp(id){
    $.ajax({
      url: "/temperature",
    }).done(function(data) {
      data = JSON.parse(data);
      table = '<table>';
      for(var key in data){
        value = data[key];
        table += "<tr><td>"+key+"</td><td>"+value+"</td></tr>";
      };
      table += "</table>";
      document.getElementById(id).innerHTML = table;
    });
}

function update_temparture_table(id){
  poll_tmp(id);
  setInterval(function(){
    poll_tmp(id);
  }, 5000);
}
