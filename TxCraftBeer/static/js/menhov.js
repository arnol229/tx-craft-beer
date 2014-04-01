$(".menu").on('hover', function(e){
				if (e.type == "mouseenter"){
					$(this).children().css("display", true)
				}
				else{
					$(this).children().css("display", none)
				}
			});