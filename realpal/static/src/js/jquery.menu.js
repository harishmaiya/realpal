document.addEventListener('scroll', function (event) {
    var position = $(this).scrollTop();

    $('.hw-container section').each(function() {
        var target = $(this).offset().top;
        var id = $(this).attr('id');

        if (position >= target) {
            $('#sub-nav a').removeClass('active');
            $('a[href*="'+id+'"]').addClass('active');
        }
    });

    var start = 400;

    scrollpos = $('.how-works .time-path .scroll.timeline').offset().top;
    diff = start - scrollpos;
    perc = diff / 2000 * 100;
    hei = 86 * perc / 100;
    $('.how-works .time-path .scroll.timeline').css({'height': hei+'%'});


    if (scrollpos < 400){
        if (!$('.no1').hasClass('active'))
            $('.no1').addClass('active');
    } else {
        $('.no1').removeClass('active');
    }

     if (scrollpos < 100){
        if (!$('.no2').hasClass('active'))
            $('.no2').addClass('active');
    } else {
        $('.no2').removeClass('active');
    }


    if (scrollpos < -310){
        if (!$('.no3').hasClass('active'))
            $('.no3').addClass('active');
    } else {
        $('.no3').removeClass('active');
    }

    if (scrollpos < -840){
        if (!$('.no4').hasClass('active'))
            $('.no4').addClass('active');
    } else {
        $('.no4').removeClass('active');
    }

    if (scrollpos < -1240){
        if (!$('.no5').hasClass('active'))
            $('.no5').addClass('active');
    } else {
        $('.no5').removeClass('active');
    }

}, true /*Capture event*/);
