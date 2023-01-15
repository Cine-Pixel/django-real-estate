var map = L.map('map').setView([41.724, 44.790], 11);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var marker = L.marker([0, 0]).addTo(map);
map.on("click", onMapClick);


function onMapClick(e) {
    const lat = e.latlng.lat;
    const lng = e.latlng.lng;
    const address = document.getElementById("address").value;
    selectAddress(lat, lng, address);
}

function showAddress(addresses) {
    const results = document.querySelector("#results");
    results.innerHTML = " ";
    if (addresses.length > 0) {
        addresses.forEach(element => {
            addressHtml = `
            <div class="results" onClick="selectAddress(${element.lat}, ${element.lon}, '${element.display_name}')">
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


function selectAddress(lat, lng, adr) {
    const address = document.getElementById("id_address");
    const longitude = document.getElementById("id_longitude");
    const latitude = document.getElementById("id_latitude");
    map.flyTo([lat, lng], 16);
    marker.setLatLng([lat, lng]);

    address.value = adr;
    longitude.value = lng;
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
