function myFunction() {
  var input, filter, table, tr, td, i, txtValue, show;
  input = document.getElementById("search-index");
  filter = input.value.toUpperCase();
  table = document.getElementById("tblindex");
  tr = table.getElementsByTagName("tr");
 
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      //  show.style.display = "";
      }
    }
  }
}

function myFun() {
var getfilter, filtervalue, filtertext, xii, ble , see;
xii = document.getElementsByClassName("xii-index");
see = document.getElementsByClassName("see-index");
ble = document.getElementsByClassName("ble-index");
getfilter = document.getElementById("gradefilter");
filtervalue = e.value;
filtertext = e.options[e.selectedIndex].text;

if (filtervalue == "8"){
xii.style.display = "none";
see.style.display = "none";

} else if(filter value == "hehe"){
ble.style.display = "";
xii.style.display = "";
see.style.display = "";
} else if(filtervalue == "10") {
ble.style.display = "none";
xii.style.display = "none";

} else if(filtervalue == "12"){
see.style.display = "none";
ble.style.display = "none";

} else{
xii.style.display = "none";
ble.style.display = "none";
see.style.display = "none";
}


}