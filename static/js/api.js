function create_post(details) {

    return $.ajax({
        method: 'POST',
        url: `${baseUrl}/api/create_post/`,
        data: details,
        dataType: 'JSON'
    });
}

function get_post() {

    return $.ajax({
        method: 'GET',
        url: `${baseUrl}/api/get_post/`,
        dataType: 'JSON'
    });
}