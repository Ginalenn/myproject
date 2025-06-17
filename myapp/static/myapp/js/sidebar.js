$(document).ready(function () {
  $('.open-btn').click(() => $('#side_nav').addClass('active'));
  $('.close-btn').click(() => $('#side_nav').removeClass('active'));

  $('.load-form').click(function (e) {
    e.preventDefault();
    const url = $(this).data('url');
    $('#dashboard-content').load(url);
  });
});
