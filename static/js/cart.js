const addCartBtn = document.getElementsByClassName("add-cart-button");


for (let i = 0; i < addCartBtn.length; i++) {
    addCartBtn[i].addEventListener("click", function () {

        const productId = this.dataset.product;
        const action = this.dataset.action;


        if (user === "Anonymous") {
            console.log("user not logged in");

        } else {
            updateUserOrder(productId, action)

        }
    })

}
const updateUserOrder = (productId, action) => {
    console.log("user :", user)
    console.log("user logged in");

    const url = "/update_item/"

    fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({"productId": productId, "action": action})
    })
        .then(response => {
            return response.json()
        })

        .then(data => {
            location.reload()
            console.log("data : ", data) });

}
