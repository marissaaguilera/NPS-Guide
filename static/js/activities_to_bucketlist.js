//Adding items to a bucketlist

$(document).ready(function(){

    for (let park in parks) {
        console.log({{ park.park_name }})

    };



    $('#search-bar').mdbAutocomplete({
        data: park.park_name
    });
});

