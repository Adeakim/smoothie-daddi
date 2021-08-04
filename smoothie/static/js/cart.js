var updateBtns = document.getElementsByClassName("update-cart");

for (var i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function (e) {
    e.preventDefault();
    var productId = this.dataset.product;
    var action = this.dataset.action;

    console.log("productId", productId, "action", action);
    console.log('User', user)

    if (user == 'AnonymousUser'){
        addCartItem(productId, action)
     }
     else{
        updateUserOrders(productId,action)
     }
  });

  function addCartItem(productId,action){
    console.log("User is not logged in ")
    if (action=='add'){
        if (cart[productId]==undefined){
            cart[productId] = {'quantity': 1}

        }else{
        cart[productId]['quantity'] +=1    
        }
    }
    if (action=='remove'){
        cart[productId]['quantity'] -=1  

        if ( cart[productId]['quantity']<=0){
            console.log("Remove Item")

            delete cart[productId]
        }
    }
    console.log('Cart:', cart)
    document.cookie = 'cart =' + JSON.stringify(cart) + ";domain;path=/"
    location.reload()

}

    function updateUserOrders(productId,action){
        console.log('User is logged in. Sending data')

        var url = '/update-item/'

        fetch(url,{
            method: 'POST',
            headers: {
                'Content-Type':'application/json',
                'x-CSRFToken' :csrftoken,
            },
            body:JSON.stringify({'productid':productId, 'action':action})
        })
        .then(response=>{
            return response.json()
        })
        .then (data=>{
            console.log('data:',data)
            location.reload()
        })

    }
    
}
