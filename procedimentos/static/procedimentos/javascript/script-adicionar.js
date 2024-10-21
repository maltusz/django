function toggleModal(stt) {
  modal = document.getElementById("modal");
  fade = document.getElementById("modal-overlay");
  if (stt == true) {
    modal.innerHTML += `
    <div class="modal-header">
        <h1>Procedimento adicionado com sucesso!</h1>
    </div>
    <div class="modal-body">
        <p>Deseja adicionar mais algum procedimento?</p>
    </div>
    <div class="modal-footer">
        <a style="background-color:#f17ea1 !important; width: 47%; border-style:none" class="btn btn-success" href="/">TELA INICIAL</a>
        <a style="background-color:#90ee80 !important; width: 47%; border-style:none" class="btn btn-primary" href="/adicionar">ADICIONAR</a>
    </div>`;
    modal.classList.toggle("hide");
    fade.classList.toggle("hide");
  } else {
    modal.innerHTML += `
    <div class="modal-header">
        <h1>Houve um erro ao tentar salvar o procedimento!</h1>
    </div>
    <div class="modal-body">
        <p>Por favor, tente novamente:</p>
    </div>
    <div class="modal-footer">
        <a href="/adicionar">ADICIONAIS</a>
    </div>`;
    modal.classList.toggle("hide");
    fade.classList.toggle("hide");
  }
}

function toggleSpinner() {
  let s = document.getElementById("spinner-container");
  if (s.classList.contains("hide")) {
    s.classList.toggle("hide");
  } else {
    s.classList.toggle("hide");
  }
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function adicionar() {
  toggleSpinner();
  let nome = document.getElementById("name").value;
  let procedimento = document.getElementById("procedimento").value;
  let valor = document.getElementById("valor").value;
  let date = document.getElementById("date").value;
  let dentista = document.getElementById("dentista").value;

  let token = getCookie("csrftoken");
  fetch("/adicionar/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": token,
    },
    body: JSON.stringify({ name: nome, procedimento: procedimento, valor: valor, date: date, dentista: dentista }),
  })
    .then((response) => response.json())
    .then((data) => {
      toggleSpinner();
      if (data.status == true) {
        toggleModal(true);
        console.log("Sucesso:", data.message);
      } else {
        toggleModal(false);
        console.log("Erro", data.error);
      }
    })
    .catch((error) => {
      console.log("Erro:", error);
    });
}
