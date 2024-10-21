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

function sair() {
  let token = getCookie("csrftoken");
  fetch("/logout/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": token,
    },
  })
    .then((response) => {
      if (response.ok) {
        window.location.href = "/";
      } else {
        alert("Erro ao tentar fazer logout. Tente novamente.");
      }
    })
    .catch((error) => {
      console.error("Erro:", error);
    });
}
