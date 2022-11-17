const btn0 = document.getElementById('view')
const btn1 = document.getElementById('add')

btn0.addEventListener('click', async () => {
        const response1 = await fetch(`http://localhost:5000/view`,{mode:'cors'});
        if(response1.status != 200) {
            alert("Server Down.");
        }
        else {
            $("#gable").find("tr:not(:first)").remove();
            var data = await response1.json();
            data.forEach(object => {
                var table = document.getElementById('gable');
                var tr = document.createElement('tr');
                tr.innerHTML = '<td>' + object.stuname + '</td>' +
                '<td>' + object.stureg + '</td>' +
                '<td>' + object.studob + '</td>';
                table.appendChild(tr);
            } );
        }
    }
);

btn1.addEventListener('click', async () => {
    const stuname = document.getElementById('stuname').value;
    const stureg = document.getElementById('stureg').value;
    const studob = document.getElementById('studob').value;
    let xhr = new XMLHttpRequest();
    let url = "http://localhost:5000/add";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify({"name":stuname,"reg":stureg,"dob":studob})); 
});