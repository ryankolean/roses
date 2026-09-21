/* Roses - concept site.
   One job: mark today's row in any hours list. Everything else is static HTML. */
(function () {
  'use strict';

  function markToday() {
    var today = String(new Date().getDay()); // 0 = Sunday
    var lists = document.querySelectorAll('.hours');
    for (var i = 0; i < lists.length; i++) {
      var rows = lists[i].querySelectorAll('li[data-day]');
      for (var j = 0; j < rows.length; j++) {
        if (rows[j].getAttribute('data-day') === today) {
          rows[j].classList.add('is-today');
        }
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', markToday);
  } else {
    markToday();
  }
})();
