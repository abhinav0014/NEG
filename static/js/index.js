function indFunction() {
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
        
      
      }
    }
  }
}



$(document).ready(function() {
    function addRemoveClass(theRows) {
        theRows.removeClass("odd even");
        theRows.filter(":odd").addClass("odd");
        theRows.filter(":even").addClass("even");
    }
    var rows = $("table#myTable tr:not(:first-child)");
    addRemoveClass(rows);
    $("#dropdownField").on("change", function() {
        var selected = this.value;
        if (selected != "All") {
            rows.filter("[position=" + selected + "]").show();
            rows.not("[position=" + selected + "]").hide();
            var visibleRows = rows.filter("[position=" + selected + "]");
            addRemoveClass(visibleRows);
        } else {
            rows.show();
           addRemoveClass(rows);
        }
    });
});