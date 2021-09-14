$(document).ready(function(){
    $(document).on('click', '.user-post-detail', function(){
        // $('.story-modal').empty();
        var postId = $(this).data('postid');
        $('.add-post-comment').attr('data-postid', postId);
        $.ajax({
            url: "post-detail/"+postId+"/",
            dataType: "json",
            success: function (data) {
                $('.story-modal-media img').attr('src', data.post_image);
                $('.post-header-detail img').attr('src', data.user_image);
                $('.post-header-detail .post-user-name').text(data.user_name);
                $('.story-content p').text(data.description);
                


                var result = data.comments.results,
                    comments = '';
                
                for (var i = 0; i < result.length; i++) {
                    var record = result[i];
                    comments +='<div class="flex flex-1 items-center space-x-2"> <img src="'+record.commenter_image+'" class="rounded-full w-8 h-8"> <div class="flex-1 p-2">'+record.comment+'</div> </div>'
                }
                
                $('.post-comments').empty().append(comments)
           }
          });
    });

    $(document).on('submit', '.add-post-comment', function(e){
        e.preventDefault();
        var post_id = $(this).data('postid'),
            formData = new FormData($(this)[0]);

        $.ajax({
            url:"add-comment/"+post_id+"/",
            method: 'POST',
            data: formData,
            contentType: false,
        	cache: false,
        	processData: false,
        	success: function(data){
                $(".add-post-comment").trigger("reset");
                
                var result = data.results,
                    comments = '';

                for (var i = 0; i < result.length; i++) {
                    var record = result[i];
                    comments +='<div class="flex flex-1 items-center space-x-2"> <img src="'+record.commenter_image+'" class="rounded-full w-8 h-8"> <div class="flex-1 p-2">'+record.comment+'</div> </div>'
                }
                $('.post-comments').empty().append(comments)
            }
        });
    });
});