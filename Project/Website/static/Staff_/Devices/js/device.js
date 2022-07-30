// Disconnect table
$(function() {
    $('table.ListFormTable').each(function() {
      var currentPage = 0;
      var numPerPage = 6;
      var $table = $(this);
      $table.bind('repaginate', function() {
        $table.find('tbody tr').hide().slice(currentPage * numPerPage, (currentPage + 1) * numPerPage).show();
      });
      $table.trigger('repaginate');
      var numRows = $table.find('tbody tr').length;
      var numPages = Math.ceil(numRows / numPerPage);
      var $pager = $('<div class="pager"></div>');
      var $previous = $('<span class="previous">&#8249;</spnan>');
      var $next = $('<span class="next">&#8250;</spnan>');

      for (var page = 0; page < numPages; page++) {
        $('<span class="page-number"></span>').text(page + 1).bind('click', {
          newPage: page
        }, function(event) {
          currentPage = event.data['newPage'];
          $table.trigger('repaginate');
          $(this).addClass('active').siblings().removeClass('active');
        }).appendTo($pager).addClass('clickable');
      }
      $pager.insertAfter($table).find('span.page-number:first').addClass('active');
      $previous.insertBefore('span.page-number:first');
      $next.insertAfter('span.page-number:last');
  
      $next.click(function(e) {
        $previous.addClass('clickable');
        $pager.find('.active').next('.page-number.clickable').click();
      });
      $previous.click(function(e) {
        $next.addClass('clickable');
        $pager.find('.active').prev('.page-number.clickable').click();
      });
      $table.on('repaginate', function() {
        $next.addClass('clickable');
        $previous.addClass('clickable');
  
        setTimeout(function() {
          var $active = $pager.find('.page-number.active');
          if ($active.next('.page-number.clickable').length === 0) {
            $next.removeClass('clickable');
          } else if ($active.prev('.page-number.clickable').length === 0) {
            $previous.removeClass('clickable');
          }
        });
      });
      $table.trigger('repaginate');
    });
  });




// Alert table
$(function() {
    $('table.alertTable').each(function() {
      var currentPage = 0;
      var numPerPage = 6;
      var $table = $(this);
      $table.bind('repaginate', function() {
        $table.find('tbody tr').hide().slice(currentPage * numPerPage, (currentPage + 1) * numPerPage).show();
      });
      $table.trigger('repaginate');
      var numRows = $table.find('tbody tr').length;
      var numPages = Math.ceil(numRows / numPerPage);
      var $pager = $('<div class="pager"></div>');
      var $previous = $('<span class="previous">&#8249;</spnan>');
      var $next = $('<span class="next">&#8250;</spnan>');

      for (var page = 0; page < numPages; page++) {
        $('<span class="page-number_2"></span>').text(page + 1).bind('click', {
          newPage: page
        }, function(event) {
          currentPage = event.data['newPage'];
          $table.trigger('repaginate');
          $(this).addClass('active').siblings().removeClass('active');
        }).appendTo($pager).addClass('clickable');
      }
      $pager.insertAfter($table).find('span.page-number_2:first').addClass('active');
      $previous.insertBefore('span.page-number_2:first');
      $next.insertAfter('span.page-number_2:last');
  
      $next.click(function(e) {
        $previous.addClass('clickable');
        $pager.find('.active').next('.page-number_2.clickable').click();
      });
      $previous.click(function(e) {
        $next.addClass('clickable');
        $pager.find('.active').prev('.page-number_2.clickable').click();
      });
      $table.on('repaginate', function() {
        $next.addClass('clickable');
        $previous.addClass('clickable');
  
        setTimeout(function() {
          var $active = $pager.find('.page-number_2.active');
          if ($active.next('.page-number_2.clickable').length === 0) {
            $next.removeClass('clickable');
          } else if ($active.prev('.page-number_2.clickable').length === 0) {
            $previous.removeClass('clickable');
          }
        });
      });
      $table.trigger('repaginate');
    });
  });