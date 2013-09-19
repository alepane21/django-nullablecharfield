(function($) {
	var NullableText = {
		'update_field_status': function ($obj) {
			var $isnull = $('#' + $obj.attr('id') + '_isnull');
			if ($obj.val().length > 0) {
				$isnull.removeAttr("checked");
			}
			if ($isnull.is(":checked")) {
				$obj.val('').attr('disabled', 'disabled').attr('readOnly', 'readOnly');
			} else {
				$obj.removeAttr('disabled').removeAttr('readOnly');
			}
		},
		'null_event': function (isnull_obj) {
			var id = $(isnull_obj).attr('id');
			NullableText.update_field_status($('#' + id.substring(0, id.length - 7)));
		},
		'input_event': function (obj) {
			NullableText.update_field_status($(obj));
		}
	};

	$(document).ready(function() {
		$('.nullable_text').each(function () {
			NullableText.update_field_status($(this));
		});
	});

	window.NullableText = NullableText;
})(django.jQuery);