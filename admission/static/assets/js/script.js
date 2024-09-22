$(function(){
	
	var note = $('#note222'),
		ts = new Date(2013, 9, 24),
		newYear = true;
	
	if((new Date()) > ts){
		// The new year is here! Count towards something else.
		// Notice the *1000 at the end - time must be in milliseconds
		//ts = (new Date()).getTime() + 10*24*60*60*1000;
		newYear = false;
	}
		
	$('#countdown222').countdown({
		timestamp	: ts,
		callback	: function(days, hours, minutes, seconds){
			
			var message = "";
			
			message += days + " day" + ( days==1 ? '':'s' ) + ", ";
			message += hours + " hour" + ( hours==1 ? '':'s' ) + ", ";
			message += minutes + " minute" + ( minutes==1 ? '':'s' ) + " and ";
			message += seconds + " second" + ( seconds==1 ? '':'s' ) + " <br />";
			
			if(newYear){
				message += "left until the new year!";
			}
			else {
				message += "left to 10 days from now!";
			}
			
			note.html(message);
		}
	});
	
});

function countdown(id1,id2,d,m,y){
	var id1="#"+id1,id2="#"+id2;
	var note = $(id2),
                
		ts = new Date(y, m-1, d),
		newYear = true;
	
	if((new Date()) > ts){
		// The new year is here! Count towards something else.
		// Notice the *1000 at the end - time must be in milliseconds
		//ts = (new Date()).getTime() + 10*24*60*60*1000;
		newYear = false;
	}
		
	$(id1).countdown({
		timestamp	: ts,
		callback	: function(days, hours, minutes, seconds){
			
			var message = "<font color=''><strong>";
			
			message += days + " day" + ( days==1 ? '':'s' ) + ", ";
			message += hours + " hour" + ( hours==1 ? '':'s' ) + ", ";
			message += minutes + " minute" + ( minutes==1 ? '':'s' ) + " and ";
			message += seconds + " second" + ( seconds==1 ? '':'s' ) + " ";
			
			if(newYear){
				message += "left!";
			}
			else {
				message += "left!";
			}
			message +="</strong></font>";
			note.html(message);
		}
	});
	
}
