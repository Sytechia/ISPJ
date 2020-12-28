var datas;
$.ajax({
    type: "GET",
    url: "/events",
    dataType: "json",
    success: function(data) {
		datas = data 
		console.log(data)
	},
	async: false,
    error: function(){
        alert("json not found");
    }
});

jQuery(document).ready(function(){
  jQuery('.datetimepicker').datepicker({
      timepicker: true,
      language: 'en',
      range: true,
      multipleDates: true,
		  multipleDatesSeparator: " - "
    });
});


	

(function () {    
    // ------------------------------------------------------- //
    // Calendar
	// ------------------------------------------------------ //
	// let events = 
	jQuery(function() {
		// page is ready
		jQuery('#calendar').fullCalendar({
			themeSystem: 'bootstrap4',
			// emphasizes business hours
			businessHours: false,
			defaultView: 'month',
			// event dragging & resizing
			editable: true,
			// header
			header: {
				left: 'title',
				center: 'month,agendaWeek,agendaDay',
				right: 'today prev,next'
			},
			events:datas,
			eventRender: function(event, element) {
				if(event.icon){
					element.find(".fc-title").prepend("<i class='fa fa-"+event.icon+"'></i>");
				}
			  },
			// dayClick: function() {
			// 	jQuery('#modal-view-event-add').modal();
			// },
			eventClick: function(event, jsEvent, view) {
			        jQuery('.event-icon').html("<i class='fa fa-"+event.icon+"'></i>");
					jQuery('.event-title').html(event.title);
					jQuery('.event-body').html(event.description);
					jQuery('.eventUrl').attr('href',event.url);
					jQuery('#modal-view-event').modal();
			},
		})
	});
  
})(jQuery);

