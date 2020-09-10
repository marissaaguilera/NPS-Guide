//Saving and updating the date for an activitiy


$('.save-order-btn').on('click', (evt) =>{
    evt.preventDefault();
    const itemID = $(evt.target).val();
    const dateInput = $(`#date-${itemID}`).val();
    const formValues = {'item_id':itemID, 'order-date': dateInput} 


    // const formValues = $(evt.target).serialize();
    $.post(`/saving-order`, formValues, (res) => {
        console.log(res.status, res.date)
        $(`#${res.item_id}`).html(res.date);
    });
}); 

