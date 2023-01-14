var map = L.map('map').setView([41.724, 44.790], 11);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
map.on("click", onMapClick);

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}

function showAddress(addresses) {
    const results = document.querySelector("#results");
    results.innerHTML = " ";
    if (addresses.length > 0) {
        addresses.forEach(element => {
            addressHtml = `
            <div class="results" onClick="selectAddress(${element.lon}, ${element.lat}, '${element.display_name}')">
                ${element.display_name}
            </div>
            `
            results.innerHTML += addressHtml
        });
    }
    else {
        results.innerHTML = "<p style='color: red;'>Not found</p>";
    }
}

function selectAddress(lon, lat, adr) {
    const address = document.getElementById("id_address");
    const longitude = document.getElementById("id_longitude");
    const latitude = document.getElementById("id_latitude");

    address.value = adr;
    longitude.value = lon;
    latitude.value = lat;
}

function findAddress() {
    const address = document.querySelector("#address");

    const url = "https://nominatim.openstreetmap.org/search?format=json&limit=3&q=" + address.value;
    fetch(url)
        .then(response => response.json())
        .then(data => showAddress(data))
        .catch(err => console.log(err));
}
