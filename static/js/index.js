const baseUrl = window.location.origin;

$(function() {
    var socket = io.connect(baseUrl);
    
    socket.on('insert_post', function(msg) {
        console.log('insert received');
        $('#postContainer').prepend(generate_block_post(msg));
    }).on('error', function(msg) {
        console.log(msg);
    }); 

    $('#createPostForm').on('submit', function(e) {
        e.preventDefault();

        socket.emit('create_post', {
            title: $(this).find('input#titleField').val(),
            body: $(this).find('textarea#contentField').val()
        }).on('error', function(msg) {
            console.log(msg);
        });
        console.log('post created');

        $(e.target).find('button[data-dismiss="modal"]').click();
    });
});

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