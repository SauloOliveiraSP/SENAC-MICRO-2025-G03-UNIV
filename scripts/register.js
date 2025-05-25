function register() {
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;
    const cpf = document.getElementById("cpf").value;
    const cep = document.getElementById("cep").value;

    if (password !== confirmPassword) {
        Toastify({
            text: "As senhas não coincidem.",
            backgroundColor: "red",
            duration: 3000,
            gravity: "top",
            position: "center",
            stopOnFocus: true,
        }).showToast();
        return;
    }

    fetch("http://127.0.0.1:8000/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username,
            email,
            password,
            cpf,
            cep
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
                    text: data.detail || "Erro no registro",
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
