/*global $, jQuery, alert */

$(document).ready(function () {

    //Sub-navbar navigation

    $(".sub-nav ul li a").click(function(){

        $(this).addClass("active");
        $(".sub-nav ul li a").not(this).removeClass("active");

    });

    //Sub-navbar getiing fixed

   $(window).scroll(function () {

       //fixing the navbar

        if ($(this).scrollTop() >= 600) {

            $(".sub-nav").addClass("fixed");

            $(".sub-nav").removeClass("back-beige");

        } else {

            $(".sub-nav").removeClass("fixed");

            $(".sub-nav").addClass("back-beige");
        };

       // coloring the first circle

       if ($(this).scrollTop() >= 650) {

            $(".no1").addClass("active-l");

        }else{

            $(".no1").removeClass("active-l")

        }

       // coloring the second circle

       if ($(this).scrollTop() >= 1148) {

            $(".no2").addClass("active-r");

        }else{

            $(".no2").removeClass("active-r ")

        }

       //coloring the third circle

       if ($(this).scrollTop() >= 1500) {

            $(".no3").addClass("active-l");

        }else{

            $(".no3").removeClass("active-l")

        }

       //coloring the forth circle

       if ($(this).scrollTop() >= 1900) {

            $(".no4").addClass("active-l");

        }else{

            $(".no4").removeClass("active-l")

        }

       //coloring the fifth circle

       if ($(this).scrollTop() >= 2300) {

            $(".no5").addClass("active-l");

        }else{

            $(".no5").removeClass("active-l")

        }

       // coloring the timeline while scolling

       var percent = ($(window).scrollTop() - $(".no1").offset().top)/17;


       $(".progress-bar").css( 'height', percent + "%" );


    });
});
