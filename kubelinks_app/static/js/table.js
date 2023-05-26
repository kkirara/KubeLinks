const table = document.getElementById("table");
const columns = document.getElementById("columns");
const rows = table.getElementsByTagName("tr");
const headers = columns.getElementsByTagName("th");
const filters = {};

function applyFilters() {
  for (let i = 2; i < rows.length; i++) {
    const row = rows[i];
    let showRow = true;

    for (const field in filters) {
      const filterValue = filters[field].value.toLowerCase();
      const cell = row.querySelector(`td[data-field="${field}"]`);
      const cellValue = cell ? cell.textContent.toLowerCase() : "";

      if (filterValue !== "" && cellValue.indexOf(filterValue) === -1) {
        showRow = false;
        break;
      }
    }
    row.style.display = showRow ? "" : "none";
  }
}

function createFilterInput(header) {
  const field = header.getAttribute("data-field");
  const input = document.createElement("input");
  input.classList.add("form-control");
  input.classList.add("form-control-sm");
  input.type = "text";
  input.placeholder = "Filter...";
  input.addEventListener("input", applyFilters);
  filters[field] = input;
  return input;
}

function createFilterSelect(header) {
  const field = header.getAttribute("data-field");
  const valuesList = [
    ...new Set(
      Array.from(document.querySelectorAll(`td[data-field="${field}"]`)).map(
        (el) => el.textContent
      )
    ),
  ].sort();
  const select = document.createElement("select");
  select.classList.add("form-select");
  select.classList.add("form-select-sm");
  select.id = field;
  var option = document.createElement("option");
  option.value = "";
  option.text = "All";
  select.appendChild(option);

  for (var i = 0; i < valuesList.length; i++) {
    var option = document.createElement("option");
    option.value = valuesList[i];
    option.text = valuesList[i];
    select.appendChild(option);
  }
  select.addEventListener("change", applyFilters);
  filters[field] = select;
  return select;
}

function createFilterInputs() {
  const thead = document.querySelector("thead");
  const tr = document.createElement("tr");
  tr.id = "filter";
  tr.classList.add("d-none");
  for (let i = 0; i < columns.cells.length; i++) {
    const header = columns.cells[i];
    const field = header.getAttribute("data-field");
    const th = document.createElement("th");
    th.setAttribute("data-field", field);
    switch (header.getAttribute("data-filter-control")) {
      case "select":
        const select = createFilterSelect(header);
        th.appendChild(select);
        break;
      case "input":
        const input = createFilterInput(header);
        th.appendChild(input);
        break;
    }
    tr.appendChild(th);
  }
  thead.appendChild(tr);
}
function showFilter() {
  const filter = document.getElementById("filter");
  filter.classList.toggle("d-none");
}

function applySort(field, ascending) {
  const rowsArray = Array.prototype.slice.call(rows, 2); // Convert HTMLCollection to array, excluding the header row
  rowsArray.sort((a, b) => {
    const aValue = a.querySelector(`td[data-field="${field}"]`).textContent;
    const bValue = b.querySelector(`td[data-field="${field}"]`).textContent;
    return ascending
      ? aValue.localeCompare(bValue)
      : bValue.localeCompare(aValue);
  });

  for (let i = 0; i < rowsArray.length; i++) {
    table.tBodies[0].appendChild(rowsArray[i]);
  }
}

function toggleSortClass(header, ascending) {
  header.classList.toggle("sorted-none", false);
  header.classList.toggle("sorted-asc", ascending);
  header.classList.toggle("sorted-desc", !ascending);
}

function resetSortClasses() {
  for (let i = 0; i < headers.length; i++) {
    headers[i]
      .querySelector("div.sortable")
      .classList.remove("sorted-asc", "sorted-desc");
    headers[i].querySelector("div.sortable").classList.add("sorted-none");
  }
}

createFilterInputs();
resetSortClasses();
const showFilters = document.getElementsByClassName("show-filter");
for (let i = 0; i < showFilters.length; i++) {
  showFilters[i].addEventListener("click", showFilter);
}

for (let i = 0; i < headers.length; i++) {
  const field = headers[i].getAttribute("data-field");
  const divHeader = headers[i].querySelector("div.sortable");
  divHeader.addEventListener("click", function () {
    const ascending = !this.classList.contains("sorted-asc");
    resetSortClasses();
    toggleSortClass(this, ascending);
    applySort(field, ascending);
  });
}
