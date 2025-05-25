function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username,
            password
        })
    })
        .then(async response => {
            const data = await response.json();
            if (response.ok) {
                Toastify({
                    text: data.message,
                    backgroundColor: "green",
                    duration: 3000,
                    gravity: "top",
                    position: "center",
                    stopOnFocus: true,
                }).showToast();
            } else {
                Toastify({
                    text: data.detail || "Erro no login",
                    backgroundColor: "red",
                    duration: 3000,
                    gravity: "top",
                    position: "center",
                    stopOnFocus: true,
                }).showToast();
            }
        })
        .catch(error => {
            console.error("Erro:", error);
            Toastify({
                text: "Erro ao conectar com a API.",
                backgroundColor: "red",
                duration: 3000,
                gravity: "top",
                position: "center",
                stopOnFocus: true,
            }).showToast();
        });
}
