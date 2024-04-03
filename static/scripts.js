const BASE_URL = "/api/cupcakes";

async function listCupcakes() {
  const res = await axios.get(`${BASE_URL}`);

  for (let cupcake of res.data.cupcakes) {
    let newCupcake = generateCupcakeHTML(cupcake);

    $("#cupcakes_list_div").append(newCupcake);
  }
}

function generateCupcakeHTML(cupcake) {
  return `<div id="${cupcake.id}" class="cupcake_div">
                <img class="cupcake_img"
                 src="${cupcake.image}"
                alt="cupcake image">
                <ul class="cupcake_ul">
                    <li>${cupcake.flavor}</li>
                    <li>${cupcake.size}</li>
                    <li>${cupcake.rating}</li>
                    <button class="cupcake_delete">Delete</button>
                </ul>
            </div>`;
}

$("#cupcakes_list_div").on("click", ".cupcake_delete", async function (evt) {
  evt.preventDefault();
  let $cupcake = evt.target.closest("div");
  let cupcakeID = $cupcake.id;

  await axios.delete(`${BASE_URL}/${cupcakeID}`);
  $cupcake.remove();
});

listCupcakes();
