const baseUrl = window.location.origin;

$(function() {
    var socket = io.connect(baseUrl);
    
    socket.on('connect', function() {
        socket.emit('request_load', 'User is connected')
    });
    
    socket.on('response_load', function(msg) {
        msg.forEach(function(post) {
            $('#postContainer').append(generate_block_post(post));
        });
    });
    
    socket.on('insert_post', function(msg) {
        console.log('insert recieved');
        $('#postContainer').prepend(generate_block_post(msg));
    });

    socket.on('unauthorized', function(msg) {
        console.log(msg);
    })

    $('#createPostForm').on('submit', function(e) {
        e.preventDefault();

        socket.emit('create_post', {
            title: $(this).find('input#titleField').val(),
            body: $(this).find('textarea#contentField').val()
        });

        $(e.target).find('button[data-dismiss="modal"]').click();
    });
})

function generate_block_post(post) {
    var block =
        `<div class="card border-0 rounded-0">
            <div class="card-body bg-primary">
                <h1 class="font-weight-bold m-0">${post['title']}</h1>
                <hr class="my-2">
                <h4 class="text-justify">${post['body']}</h4>
            </div>
        </div>`;

    return block;
}