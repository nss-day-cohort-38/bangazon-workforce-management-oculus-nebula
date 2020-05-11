const infoDialog = document.querySelector(".infoDialog");
const message = document.querySelector(".infoDialog__message");
const closeDialog = document.querySelector(".closeDialog");

document.querySelector(".training_programs").addEventListener("click", (e) => {
  if (e.target.id.startsWith("detail")) {
    const id = e.target.id.split("--")[1];
    message.innerText = `You hit the details button with id of ${id}`;
    infoDialog.show();
  }
});

closeDialog.addEventListener("click", (e) => infoDialog.close());

window.addEventListener("keyup", (e) => {
  if (e.keyCode === 27) {
    infoDialog.close();
  }
});
