document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById('genre_name');
    input.addEventListener('keyup', get_value);

});

function get_value(event){
    const val = event.target.value;
    const url = "/apiGenreList/?name=" + val;
    fetch(url).then(response => response.json()).then(data => {
        const lista = document.getElementById('lista');
        lista.innerText = ""
        data.forEach( row => {
                li = document.createElement('li')
                li.dataset.id = row.id;
                li.innerText = row.name;
                lista.appendChild(li)
        });
    }).catch(error => {console.log(error)});
}