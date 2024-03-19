function inputChanged(event) {
    fetch('/sum?n=' + event.target.value )
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById("result").value = data["sum"];
        });
}





