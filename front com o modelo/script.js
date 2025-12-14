const form = document.getElementById("form-predict");
const resultado = document.getElementById("result");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const dados = {
    tamanho_m2: parseFloat(document.getElementById("tamanho").value),
    quartos: parseInt(document.getElementById("quartos").value ),
    banheiros: parseInt(document.getElementById("banheiros").value),
    ano: parseInt(document.getElementById("ano").value),
  };

  resultado.innerHTML = "Calculando...";

  try {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(dados),
    });

    const data = await response.json();

    resultado.innerHTML = `
    
      <strong>US$ ${data.preco_estimado.toLocaleString()}</strong>
    `;
  } catch (error) {
    resultado.innerHTML = "Erro ao conectar com a API";
  }
});
