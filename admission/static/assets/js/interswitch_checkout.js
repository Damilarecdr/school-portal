//load isw payment page

//callback function that gets triggered on payment success or failure
function paymentCallback(response){
    swapcontent('return_url',response,'Interswitch');
    
    /*if(response != null){
        alert(response.desc);
        alert(response);
        console.log(response);
    
        
    }
    */

}

    