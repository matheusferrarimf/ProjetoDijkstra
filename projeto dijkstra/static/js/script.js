document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("form-caminho");

    form.addEventListener("submit", function(event) {
        const cidade1 = document.getElementById("cidade1").value.trim();
        const cidade2 = document.getElementById("cidade2").value.trim();

        if (cidade1 === "" || cidade2 === "") {
            alert("Por favor, preencha ambos os campos de cidade.");
            event.preventDefault();  // Impede o envio do formulário
        }
    });
});
document.getElementById('mostrar-grafo').addEventListener('click', function() {
    var grafoContainer = document.getElementById('grafo-container');
    if (grafoContainer.style.display === 'none') {
        grafoContainer.style.display = 'block';
    } else {
        grafoContainer.style.display = 'none';
    }
});
