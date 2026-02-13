document.addEventListener("DOMContentLoaded", function () {

    // CREATE USER
    document.getElementById("createBtn").addEventListener("click", async function () {

        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;

        const res = await fetch("/users", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({name, email})
        });

        const data = await res.json();
        document.getElementById("userResult").innerText = "User ID: " + data.id;
    });

    // TRANSLATE
    document.getElementById("translateBtn").addEventListener("click", async function () {

        const user_id = parseInt(document.getElementById("user_id").value);
        const source_text = document.getElementById("source_text").value;
        const source_lang = document.getElementById("source_lang").value;
        const target_lang = document.getElementById("target_lang").value;

        const res = await fetch("/translate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({user_id, source_text, source_lang, target_lang})
        });

        const data = await res.json();

        document.getElementById("translateResult").innerText =
            "Translation:\n" + data.translated_text +
            "\n\nGrammar Score: " + data.grammar_score;
    });

    // IMPROVE
    document.getElementById("improveBtn").addEventListener("click", async function () {

        const text = document.getElementById("improve_text").value;

        const res = await fetch("/ai/improve", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({text})
        });

        const data = await res.json();

        document.getElementById("improveResult").innerText = data.result;
    });

// User form fill karta hai
// JavaScript value read karta hai
// ↓
// fetch() call hota hai
// ↓
// Browser HTTP POST request banata hai
// ↓
// Request jaati hai:
//    http://127.0.0.1:8000/users
// ↓
// Uvicorn request receive karta hai
// ↓
// FastAPI route match karta hai @app.post("/users")
// ↓
// Schema validate hota hai
// ↓
// CRUD DB me save karta hai
// ↓
// Response JSON ban kar wapas aata hai
// ↓
// Browser response receive karta hai
// ↓
// JS UI update karta hai

// FastAPI return
// ↓
// Python object
// ↓
// JSON serialization
// ↓
// HTTP response
// ↓
// Uvicorn send
// ↓
// Browser receive
// ↓
// fetch() resolve
// ↓
// res.json()
// ↓
// JavaScript object
// ↓
// DOM update
// ↓
// User sees result


});

