$("input#searchtext").on('keyup', function(e){
				$.ajax({
					type:"GET",
					url: "search",
					data: $(this).serialize(),
					dataType: "json",
					success: function( data ){
						//eventually work in animation
						//for swapping main body with new results
						$("<body>").html(data.html)
					},
				});
			});