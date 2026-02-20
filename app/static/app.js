// Base API URL (keep empty for same-origin: localhost / GKE service)
const API = "";


// ==========================
// Utility
// ==========================

function show(data) {
    document.getElementById("response").textContent =
        JSON.stringify(data, null, 2);
}


// ==========================
// Data APIs
// ==========================

async function addUser() {

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    const res = await fetch(API + "/api/data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, email })
    });

    const data = await res.json();
    show(data);
}


async function fetchUsers() {

    const res = await fetch(API + "/api/data");
    const data = await res.json();

    document.getElementById("users").textContent =
        JSON.stringify(data, null, 2);
}


// ==========================
// Query API
// ==========================

async function runQuery() {

    const query = document.getElementById("query").value;

    const res = await fetch(API + "/api/query", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ query })
    });

    const data = await res.json();

    document.getElementById("queryResult").textContent =
        JSON.stringify(data, null, 2);
}


// ==========================
// Metrics APIs
// ==========================

// Legacy Buttons (if still used)
function call200() {
    callMetric("/api/metrics/200");
}

function call400() {
    callMetric("/api/metrics/400");
}

function call500() {
    callMetric("/api/metrics/500");
}


// New Generic Button Handler
function callApi(endpoint) {
    callMetric(endpoint);
}


async function callMetric(url) {

    try {

        const res = await fetch(API + url);

        const data = await res.json();

        show(data);

    } catch (err) {

        show({
            error: "Metric API failed",
            details: err.toString()
        });
    }
}


// ==========================
// Volume APIs
// ==========================

async function writeVolume() {

    try {

        const res = await fetch(API + "/api/volume/write");
        const data = await res.json();

        show(data);

    } catch (err) {

        show({
            error: "Write volume failed",
            details: err.toString()
        });
    }
}


async function readVolume() {

    try {

        const res = await fetch(API + "/api/volume/read");
        const data = await res.json();

        document.getElementById("volumeData").textContent =
            JSON.stringify(data, null, 2);

    } catch (err) {

        document.getElementById("volumeData").textContent =
            "Error: " + err.toString();
    }
}
