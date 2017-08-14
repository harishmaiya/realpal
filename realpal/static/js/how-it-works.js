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
            
        } else {
            
            $(".sub-nav").removeClass("fixed");
        };
       
       // coloring the first circle
       
       if ($(this).scrollTop() >= 650) {
            
            $(".no1").addClass("active-l");
            
        }else{
            
            $(".no1").removeClass("active-l")
            
        }
       
       // coloring the second circle
       
       if ($(this).scrollTop() >= 1015) {
            
            $(".no2").addClass("active-r");
            
        }else{
            
            $(".no2").removeClass("active-r ")
            
        }
       
       //coloring the third circle
       
       if ($(this).scrollTop() >= 1200) {
            
            $(".no3").addClass("active-l");
            
        }else{
            
            $(".no3").removeClass("active-l")
            
        }
       
       // coloring the timeline while scolling
       
       var percent = ($(window).scrollTop() - $(".no1").offset().top)/3;
       
       
       console.log(percent + "%");
       
       $(".progress-bar").css( 'height', percent + "%" );

       
    });
});