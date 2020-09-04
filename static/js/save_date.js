//User profile page 


//create function with event listener when i save 
$('.bucketlist-save-form').on('submit', (evt) =>{
    alert('Hello');
    evt.preventDefault();
    const formValues = $(evt.target).serialize();
    $.post(`/saving-order`, formValues, (res) => {
        alert(res);

    });
}); 
    
    
    //serialize turns a form into a JS object that is ready to be handed off in AJAX
    //will gather key value pairs from my form 

    
    
    
    
//prevent default cancels event from defaulting to what html would do 
