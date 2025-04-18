document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("extract-form");
    const input = document.getElementById("number-input");
    const messageDiv = document.getElementById("message");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const number = parseInt(input.value);

        try {
            const res = await fetch("/api/extract", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ number })
            });

            const data = await res.json();

            if (res.ok) {
                // Actualizar la celda visualmente
                const cell = document.querySelector(`.cell[data-number="${number}"]`);
                if (cell) {
                    cell.classList.add("extracted");
                }
                messageDiv.textContent = `✅ Número ${number} extraído con éxito.`;
                messageDiv.style.color = "#28a745";
                input.value = "";
            } else {
                messageDiv.textContent = data.error;
                messageDiv.style.color = "#d9534f";
            }
        } catch (err) {
            messageDiv.textContent = "Error en la conexión con el servidor.";
            messageDiv.style.color = "#d9534f";
        }
    });
});